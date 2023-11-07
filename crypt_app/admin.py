from django.contrib import admin

from .models import Profile, PaymentHistory, WithdrawalRequest 


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email','phone']
    list_display_links = ['first_name', 'last_name', 'username','email']

admin.site.register(Profile, ProfileAdmin)

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ['plan_type','user','approved','date']
    list_display_links = ['plan_type','user','approved','date']

admin.site.register(PaymentHistory, PaymentHistoryAdmin)


class WithdrawalRequestAdmin(admin.ModelAdmin):
    list_display = ['amount','user','approved','date']
    list_display_links = ['amount','user','approved','date']

admin.site.register(WithdrawalRequest, WithdrawalRequestAdmin)