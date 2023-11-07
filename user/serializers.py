from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import serializers 


""" Registration Serializer """ 
class RegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField(min_length=2, max_length=20, required=True)
    lastname = serializers.CharField(min_length=2, max_length=20, required=True)
    username = serializers.CharField(min_length=6, max_length=20, required=True)
    email = serializers.EmailField(min_length=8, max_length=60, required=True)
    phone = serializers.CharField(min_length=5, max_length=15, required=True)
    password = serializers.CharField( required=True)



    def validate_username(self, value):
        # check if username already exists 
        chk_username = User.objects.filter(username__iexact=value)

        if chk_username.count():
            raise serializers.ValidationError(f" username {value} is not available")

        # check username length 
        if len(value) < 4 or len(value) > 20:
            raise serializers.ValidationError("username must be between 4 to 20 characters")
        #check if username is empty 
        if value == " ":
            raise serializers.ValidationError("username can not be empty")

        return value


    def validate_email(self, value):

        # check if email exists 
        chk_email = User.objects.filter(email__iexact=value)

        if chk_email.count():
            raise serializers.ValidationError(f"email {value} is unavailable")

        #check email length 
        if len(value) < 8 or len(value) > 60:
            raise serializers.ValidationError("email must be between 6 to 60 characters")
        #check if email is empty 
        if value == " ":
            raise serializers.ValidationError("email cannot be empty")

        return value  

    def validate_password(self, value):
        if len(value) < 8 or len(value) > 30:
            raise serializers.ValidationError("password must not be less then 8 characters or greater than 30 characters.")
        
        return value 