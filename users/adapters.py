import logging
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        email = sociallogin.account.extra_data.get('email')
        User = get_user_model()

        # Log for debugging
        logger.info(f"Checking if the email {email} is open for signup")

        if email:
            if User.objects.filter(email=email).exists() or SocialAccount.objects.filter(user__email=email).exists():
                raise ValidationError(
                    "An account with this email address already exists. Please log in instead."
                )

        return super().is_open_for_signup(request, sociallogin)
