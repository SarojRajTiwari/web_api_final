from django.contrib import admin
from django.conf import settings
from apis.accounts.models import User

admin.site.register(User)
# admin.site.register('settings.AUTH_USER_MODEL')