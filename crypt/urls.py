from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('user.urls')),
    path('api/app/', include('crypt_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



                          


# {
#   "firstname":"mike",
#   "lastname":"den",
#   "username":"mikeden",
#   "email":"mikeden@email.com",
#   "phone":"0938484",
#   "password":"locodick"
# }


# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5OTU0ODI1MywiaWF0IjoxNjk4OTQzNDUzLCJqdGkiOiIxYmRmMGMwNDIxMjU0MjdmYjAxOTUyMmIxMzQ3OTAyZCIsInVzZXJfaWQiOjF9.QjvvLHwiheTiAgf-SmbC3TjciP4jJz59WA4Pz5VrFkk",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MjAyNjUzLCJpYXQiOjE2OTg5NDM0NTMsImp0aSI6IjlhZDc3ZmJmNGM4NTQ0Yzc5NTU3MTdiNzI5NWI1NjQzIiwidXNlcl9pZCI6MX0.i3GIGnENPTuTjBMljsIEwC1mheBHo4zidG35H_uqUJA"
# }