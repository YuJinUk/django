from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pp(request, name, c):
    product_price = {"라면": 980, "홈런볼": 1500, "칙촉": 2300, "식빵": 1800}
    for i in product_price:
        if name == i:
            check_value = product_price[i] * int(c)
            break
    else:
        check_value = -1
    if check_value == -1:
        context = {"name": name}
        return render(request, "price.html", context)
    else:
        context = {"name": name, "cnt": c, "price": check_value}
        return render(request, "index.html", context)
