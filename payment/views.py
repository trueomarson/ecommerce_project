import json
import stripe 
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from basket.basket import Basket


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.','')
    total = int(total)

    stripe.api_key = 'sk_test_51JVF0JK6v6fVXC6Sy3Hcr3HxH9kJm05fU8MRqhMzvI96NtJzoTMeQs0SwYyM2qHN91ZNYE65JtdHr8H53J65Wl5800l4kEOLeL'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='eur',
        metadata={'userid': request.user.id}
    )
    
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
