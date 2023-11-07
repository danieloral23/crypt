from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ProfileView, PaymentHistoryView, WithdrawalRequestView


urlpatterns = [

    path('profile/', ProfileView.as_view(), name="profile"),
    path('payment/', PaymentHistoryView.as_view(), name="payment"),
    path('withdraw/', WithdrawalRequestView.as_view(), name="withdraw"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)