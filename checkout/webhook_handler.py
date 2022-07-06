""" Import for webhook handlers"""
from django.http import HttpResponse


class StripeWH_Handler:
    """
    Stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Unknown/generic and unexpected webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}'
        )
