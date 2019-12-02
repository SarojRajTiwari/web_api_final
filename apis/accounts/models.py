from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    ROLES = (("0", "Admin"), ("1", "Staff"), ("2", "Journalist"))
    role = models.CharField(choices=ROLES, max_length=1)
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "role", "first_name", "last_name"]

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), blank=True, null=True)