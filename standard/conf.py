from django.conf import settings

class PayPalSettingsError(Exception):
    """Raised when settings be bad."""
    

TEST = getattr(settings, "PAYPAL_TEST", True)


RECEIVER_EMAIL = settings.PAYPAL_RECEIVER_EMAIL


# API Endpoints.
POSTBACK_ENDPOINT = "https://www.paypal.com/cgi-bin/webscr"
SANDBOX_POSTBACK_ENDPOINT = "https://www.sandbox.paypal.com/cgi-bin/webscr"

# Images
IMAGE = getattr(settings, "PAYPAL_IMAGE", "http://images.paypal.com/images/x-click-but01.gif")
SUBSCRIPTION_IMAGE = "https://www.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif"
SANDBOX_IMAGE = getattr(settings, "PAYPAL_SANDBOX_IMAGE", "https://www.sandbox.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif")
SUBSCRIPTION_SANDBOX_IMAGE = "https://www.sandbox.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif"
BUY_BUTTON_CLASS =  getattr(settings, "PAYPAL_BUY_BUTTON_CLASS", None)
BUY_BUTTON_TEXT  =  getattr(settings, "PAYPAL_BUY_BUTTON_TEXT", "Buy now!")
