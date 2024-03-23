from django.urls import path

from tasker.accounts.views import RegisterView, LoginView, DetailsProfileView, EditProfileView, \
    DeleteProfileView, logout_user

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('details/', DetailsProfileView.as_view(), name='details'),
    path('edit/', EditProfileView.as_view(), name='edit'),
    path('delete/', DeleteProfileView.as_view(), name='delete'),
)