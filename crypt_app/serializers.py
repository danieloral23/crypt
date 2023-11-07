from rest_framework import serializers 

from .models import Profile, PaymentHistory, WithdrawalRequest 



class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['first_name','last_name','username','email','phone','account_balance']


class PaymentHistorySerializer(serializers.ModelSerializer):
    plan_type = serializers.CharField(required=False)
    user = serializers.CharField(required=False)
    # payment_prove = serializers.FileField(required=True)

    class Meta:
        model = PaymentHistory
        fields = ['plan_type','user','approved','date']


class WithdrawalRequestSerializer(serializers.ModelSerializer):
    amount = serializers.CharField(required=True)
    user = serializers.CharField(required=False)

    class Meta:
        model = WithdrawalRequest
        fields = ['amount','user','approved','date']

