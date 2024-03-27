from django.urls import path, include

from tasker.accounts.views import RegisterView, LoginView, \
        logout_user, ProfileDetailsView, ProfileUpdateView, ProfileDeleteView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile")
        ]),
    ),
)