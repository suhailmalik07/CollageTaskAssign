"""TaskManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

# Custom Imports
from .views import HomeView, StudentRegisterView, TeacherRegisterView, AssignTaskView,\
    TaskView, TaskUpdateView, UserProfileView, MyTaskView, LoginFormView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/student/', StudentRegisterView.as_view(),
         name='register-student'),
    path('register/teacher/', TeacherRegisterView.as_view(),
         name='register-teacher'),

    path('accounts/profile/', UserProfileView.as_view(), name='user-profile'),

    path('tasks/me', MyTaskView.as_view(), name='tasks-me'),

    path('assign-task/', AssignTaskView.as_view(), name='assign-task'),

    path('task/<int:pk>/', TaskView.as_view(), name='task'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='update-task'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
