from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "cart"

urlpatterns = [
    path("add/<int:course_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:course_id>/", views.delete_from_cart, name="remove"),
    path("checkout/", views.checkout, name="checkout"),
    path("payment/<int:ref_code>", views.process_payment, name="payment"),
    path("update_records/<int:ref_code>", views.update_transaction_records, name="update_records"),
    path("order_history/", views.order_history, name="order_history"),
    path("", views.cart_detail, name="cart_detail"),
]
