from django.http import Http404
 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status, permissions

from .serializers import ProfileSerializer, PaymentHistorySerializer, WithdrawalRequestSerializer
from .models import Profile, PaymentHistory, WithdrawalRequest


class ProfileView(APIView):
    permissions_classes = (permissions.IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        profile = Profile.objects.filter(username=self.request.user)
        profile_serializer = self.serializer_class(profile, many=True)
        payment = PaymentHistory.objects.filter(user=self.request.user).order_by('-time')
        payment_serializer = PaymentHistorySerializer(payment, many=True)
        withdraw = WithdrawalRequest.objects.filter(user=self.request.user).order_by('-time')
        withdraw_serializer = WithdrawalRequestSerializer(withdraw, many=True)
        return Response({
            "profile":profile_serializer.data,
            "payment": payment_serializer.data,
            "withdraw": withdraw_serializer.data,
            "status":status.HTTP_200_OK
            })
    


class PaymentHistoryView(APIView):
    permissions_classes = (permissions.IsAuthenticated, )
    serializer_class = PaymentHistorySerializer


    # def get_object(self):
    #     return PaymentHistory.objects.filter(user=self.request.user).order_by('-date')
    

    # def get(self, request, format=None):
    #     payment = self.get_object()
    #     serializer = self.serializer_class(payment, many=True)
    #     return Response({
    #         "data":serializer.data 
    #     },status=status.HTTP_200_OK)
    

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = self.request.user)
            return Response({
                "data":serializer.data,
                "status":status.HTTP_201_CREATED
            })
        
        return Response({
            "data":serializer.errors,
            "status":status.HTTP_400_BAD_REQUEST
        })


class WithdrawalRequestView(APIView):
    permissions_classes = (permissions.IsAuthenticated, )
    serializer_class = WithdrawalRequestSerializer


    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = self.request.user)
            return Response({
                "data":serializer.data,
                "status":status.HTTP_201_CREATED
            })
        
        return Response({
            "message":serializer.errors,
            "status":status.HTTP_400_BAD_REQUEST
        })




        
