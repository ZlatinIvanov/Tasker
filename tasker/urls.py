from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasker.common.urls')),
    path('accounts/', include('tasker.accounts.urls')),
    path('tasks/', include('tasker.tasks.urls')),
    path('projects/', include('tasker.projects.urls')),

]
