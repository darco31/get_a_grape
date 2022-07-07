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
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeded
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle payment intent failed
        """
        return HttpResponse(
            content=f'Payment failed Webhook received: {event["type"]}',
            status=200
        )

