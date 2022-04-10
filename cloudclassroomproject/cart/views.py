from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from platformdirs import user_cache_dir
from main.models import UserProfile
from course.models import Course
from django.shortcuts import render, redirect
from .models import OrderItem, Order

# Create your views here.


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = UserProfile.objects.get(user=request.user)
    order = Order.objects.filter(user_profile=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required(login_url="main:signin")
def add_to_cart(request, course_id):
    user_profile = request.user.userprofile
    course = Course.objects.get(id=course_id)
    if course in user_profile.courses.all():
        messages.info(request, "You already signed up for this course.")
        return redirect("course:view_course", course.name)
    order_item, status = OrderItem.objects.get_or_create(course=course)
    order, status = Order.objects.get_or_create(
        user_profile=user_profile, is_ordered=False
    )
    order.items.add(order_item)
    if status:
        # generate a reference code
        order.ref_code = generate_order_id()
        order.save()
    messages.info(request, "Item added to cart.")
    return redirect("course:view_course", course.name)
