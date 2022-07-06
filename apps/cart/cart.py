from django.conf import settings

from cart.views import Cart

__all__ = ['cart']

context_var = getattr(settings, 'EASYCART_CONTEXT_VAR', 'cart')


def cart(request):
    return {context_var: Cart(request)}