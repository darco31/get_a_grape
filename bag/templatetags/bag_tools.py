from django import template

register = template.Library()

@register.filter(name='calculate_subtotal')
def calculate_subtotal(price, quantity):
    """
    Tag to display the correct subtotal in the 
    shopping bag
    """
    return price * quantity
