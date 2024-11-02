from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("account_status/", views.index, name="account_status"),  # Account status page
    path("money_transfer/", views.money_transfer, name="money_transfer"),  # Money transfer page
    path("loan_app/", views.loan, name="loan_app"),  # Loan application page
    path("ewallet/", views.ewallet, name="ewallet"),  # E-wallet page
    path("online_pay/", views.online_pay, name="online_pay"),  # Online payment page
    path("settings/", views.settings, name="settings"),  # Settings page
    path("edit_details/", views.edit_details, name="edit_details"),  # Edit account details
    path("delete_account/", views.delete_account, name="delete_account"),  # Delete account
]
