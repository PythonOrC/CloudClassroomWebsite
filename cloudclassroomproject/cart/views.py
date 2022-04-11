from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import UserProfile
from course.models import Course
from django.shortcuts import render, redirect
from .models import Order
from cloudclassroomproject.settings import LOGIN_URL
import datetime
from .extras import generate_order_id
# Create your views here.


def get_user_pending_order(request):
    # get order for the correct user
    order = Order.objects.filter(user_profile=request.user.userprofile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        print(order)
        return order
    return []

def get_order_total(order):
    total = 0
    if order:
        for item in order:
            total += item.course.price
    return total


@login_required(login_url=LOGIN_URL)
def add_to_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    if Order.objects.filter(user_profile=request.user.userprofile, course=course).exists():
        messages.info(request, "You already signed up for this course.")
        return redirect("course:view_course", course.id)

    order = get_user_pending_order(request)
    if order:
        order_id = order[0].ref_code
    else:
        order_id = generate_order_id()
    order= Order.objects.create(user_profile=request.user.userprofile, course=course, ref_code = order_id)
    messages.info(request, "Item added to cart.")
    return redirect("course:view_course", course.id)

@login_required(login_url=LOGIN_URL)
def delete_from_cart(request, course_id):
    orders = get_user_pending_order(request)
    item_to_delete = orders.filter(course_id=course_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted.") 
    return redirect("cart:cart_detail")


@login_required(login_url=LOGIN_URL)
def cart_detail(request):
    order = get_user_pending_order(request)
    total = get_order_total(order)
    return render(request, "cart.html", {"order": order, "total": total})

@login_required(login_url=LOGIN_URL)
def checkout(request):
    order = get_user_pending_order(request)
    total = get_order_total(order)
    return render(request, "checkout.html", {"order": order, "total": total, "ref_code": order[0].ref_code})

@login_required(login_url=LOGIN_URL)
def process_payment(request, ref_code):
    # process the actual payment here
    return redirect("cart:update_records", ref_code)

@login_required(login_url=LOGIN_URL)
def update_transaction_records(request, ref_code):
    # update the transaction records
    order_to_update = Order.objects.filter(ref_code=ref_code)
    for item in order_to_update:
        item.is_ordered = True
        item.date_ordered = datetime.datetime.now()
        item.save()

    
    # user_profile = request.user.userprofile
    # order_courses = [item.course for item in order_items]
    # user_profile.courses.add(*order_courses)
    # user_profile.save()
    # TODO add the functionality to send an email to the customer
    messages.info(request, "Thank you! Your items have been ordered.")
    return redirect("account:account_overview")




