from django.urls import path

from .views import SignUpView
from accounts.views import SignUpView, ActivateAccountView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
     path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
]