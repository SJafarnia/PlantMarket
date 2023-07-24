from django.contrib import admin
from django.urls import path, include
from .views import UserMainView, EditProfile, UserLogin, UserSignUp, FactorHistory, EditOrderQ,\
    FactorHistoryDetails, OrderListPay, AddAddress, UserAddresses, EditAddress, Profile, UserVerify, SendSms
urlpatterns = [
    path('', UserMainView.as_view(), name="user_main_page_url"),
    path('profile/', Profile.as_view(), name="user_profile_url"),
    path('login/', UserLogin.as_view(), name="login_url"),
    path('signup/', UserSignUp.as_view(), name="signup_url"),
    path('signup/v/<pk>', UserVerify.as_view(), name="verify_url"),
    path('signup/sres', SendSms.as_view(), name="send_sms_url"),
    path('factor/', FactorHistory.as_view()),
    path('factor/detail', FactorHistoryDetails.as_view()),
    path('factor/pay', OrderListPay.as_view(), name="factor_pay_url"),
    path('factor/pay/edit', EditOrderQ.as_view(), name="factor_edit_url"),
    path('credential/add-a/', AddAddress.as_view(), name="add_a_url"),
    path('credential/addresses', UserAddresses.as_view(), name="addresses_url"),
    path('credential/edit-a/<slug>', EditAddress.as_view(), name="edit_a_url"),
]