import random
import string
from datetime import date
import datetime
from .models import Order
def generate_order_id():
    not_unique = True
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    while not_unique:
        rand_str = "".join([random.choice(string.digits) for i in range(3)])
        order_id = date_str + rand_str
        if not Order.objects.filter(ref_code=order_id).exists():
            not_unique = False
    return order_id