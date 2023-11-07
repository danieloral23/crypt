from django.db import models
from django.contrib.auth import get_user_model 
User = get_user_model()



class Profile(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    account_balance = models.IntegerField(default=0.00)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.username.username


class PaymentHistory(models.Model):
    plan_type = models.CharField(max_length=50, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment")
    approved = models.BooleanField(default=False)
    payment_prove = models.FileField(upload_to="upload", null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.user.username


class WithdrawalRequest(models.Model):
    amount = models.CharField(max_length=30, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="withdraw")
    approved = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.user.username

