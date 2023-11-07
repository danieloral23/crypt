from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import permissions, status, generics
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from .serializers import RegisterSerializer
from crypt_app.models import Profile


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permissions_classes = (permissions.AllowAny)


    def post(self, request, *args, **kwargs):
        serializer  = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):

            firstname = serializer.data["firstname"].upper()
            lastname = serializer.data["lastname"].upper()
            username = serializer.data["username"].lower()
            email = serializer.data["email"].lower()       
            phone = serializer.data["phone"]
            password = serializer.data["password"]

            user = User.objects.create_user(
                firstname=firstname,
                lastname=lastname,
                username=username,
                email=email,
                password=password
            )
            user.save()

            profile = Profile.objects.create(
                first_name=firstname,
                last_name=lastname,
                username=user,
                email=email,
                phone=phone
            )
            profile.save()

            return Response({"data":serializer.data, "status":status.HTTP_201_CREATED})
        
        else:
            return Response({
               "error": serializer.errors,
               "status": status.HTTP_400_BAD_REQUEST 
            })


