from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cloudclassroomproject.settings import LOGIN_URL
from cart.models import Order
# Create your views here.


@login_required(login_url=LOGIN_URL)
def account_overview(request):
    orders = Order.objects.filter(user_profile=request.user.userprofile, is_ordered=True)
    return render(request, "profile.html", {"orders": orders})
