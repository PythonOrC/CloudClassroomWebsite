from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cloudclassroomproject.settings import LOGIN_URL
from cart.models import Order
from django.shortcuts import redirect
# Create your views here.


@login_required(login_url=LOGIN_URL)
def account_overview(request):
    orders = Order.objects.filter(user_profile=request.user.userprofile, is_ordered=True)
    return render(request, "profile.html", {"orders": orders})

@login_required(login_url=LOGIN_URL)
def order_history(request):
    my_order_courses = Order.objects.filter(user_profile=request.user.userprofile, is_ordered=True)
    my_order_courses = my_order_courses.order_by("-date_ordered")
    index= -1
    my_orders_wrapped = []
    ref_codes = []
    ref_code = 0
    for order_course in my_order_courses:
        if order_course.ref_code == ref_code:
            my_orders_wrapped[index].append(order_course)
        else:
            index += 1
            ref_code = order_course.ref_code
            ref_codes.append(ref_code)
            my_orders_wrapped.append([order_course])
    my_orders = {}
    for i in range(len(my_orders_wrapped)):
        name = []
        cost = 0
        for order in my_orders_wrapped[i]:
            name.append(order.course)
            cost += order.course.price


        my_orders[ref_codes[i]] = [name, cost, my_orders_wrapped[i][0].date_ordered]


    print(my_orders_wrapped)
    print(ref_codes)
    print(my_orders)
    return render(request, "order-history.html", {"my_orders": my_orders, "ref_codes": ref_codes})