from rest_framework import permissions
from django.conf import settings

from apis.accounts.models import User

class IsNewsCreator(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        return bool(request.user and request.user.role in [i for i, j in User.ROLES if j in ['Admin', 'Journalist']])



class IsNewsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        print('------xxxxxxxxxxxxxxxxxxxxxx------xxxxxxxxxxxxxxxxxxxxxxx----------')
        print(self)
        print('----------------------')
        print(request)
        print('----------------------')
        print(view)
        print('-----xxxxxxxxxx-----------------')
        print(dir(view))
        print('-----xxxxxxxxxx-----------------')
        print(view.get_object().author)
        print('-------xxxxxxxxxxxxxxx---------------')
        print(request.user == view.get_object().author)
        print('-------xxxxxxxxxxxxxxx---------------')
        print(request.user)
        print('----------------------')
        # print(request.user.news_set.first().author)
        # print(request.user.news_set.all())
        # print(request.user.news_set.filter(author=request.user))
        
        return bool(request.user and request.user == view.get_object().author or request.user.role in [i for i, j in User.ROLES if j in ['Admin']] )
