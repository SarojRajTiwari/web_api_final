from rest_framework import serializers
from apis.accounts.models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        extra_kwargs = {
            "address":{"required":False},
            "dob":{"required":False}
        }
        fields = "address", "dob"


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = "username", "email", "first_name", "last_name", "role", "profile", "password" # profile is the related name given to theprofile instance of that user
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validate_data):
        print(validate_data)
        profile = validate_data.pop("profile")
        print(profile)
        password = validate_data.pop("password")
        print(validate_data)
        user =  User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        print(user)
        Profile.objects.create(**profile, user=user)
        print(Profile.objects.all())
        return user