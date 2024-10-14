from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount

User=get_user_model()

@receiver(user_signed_up)
def google_user_profile(request,user,**kwargs):
    """
    Signal to populate the AppUser model or update it after a user signs up using Google
    """
    try:
       social_account=SocialAccount.objects.get(user=user)
       data=social_account.extra_data
       firstname=data.get("given_name", "")
       lastname=data.get('family_name',"")
       email=data.get("email","")

       user.firstname=firstname
       user.lastname=lastname
       user.email=email
       user.save()

    except SocialAccount.DoesNotExist:
        pass
