from store.models import Category
from .basket import Basket

def basket(request):
    return{'categories': Category.objects.filter(level=0)}