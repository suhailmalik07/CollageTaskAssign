from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Custom Imports
from .models import Task, User
from .forms import RegisterForm, StudentLoginForm, UserProfileForm, AssignTaskForm


class HomeView(ListView):
    model = Task


class UserProfileView(SuccessMessageMixin, UpdateView):
    form_class = UserProfileForm
    extra_context = {'title': 'Update', 'button_value': 'update'}
    success_message = "Your Profile has been updated successfully!"
    success_url = reverse_lazy('user-profile')

    def get_object(self):
        return self.request.user


class MyTaskView(LoginRequiredMixin, ListView):
    fields = '__all__'
    template_name = 'task/task_me.html'

    def get_queryset(self):
        queryset = Task.objects.filter(student=self.request.user)


class StudentRegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'task/user_form.html'
    extra_context = {"title": "student"}
    success_message = "Welcome Student! Your account has been created successfully, you can login now!"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.is_student = True
        return super().form_valid(form)


class TeacherRegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'task/user_form.html'
    extra_context = {"title": "teacher"}
    success_message = "Welcome Teacher! Your account has been created successfully, you can login now!"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.is_teacher = True
        return super().form_valid(form)


class AssignTaskView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = AssignTaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('home')
    success_message = "Task has been assigned to  %(student)s!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_teacher == True:
            return True
        return False


class TaskView(DetailView):
    model = Task
    fields = '__all__'


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['student', 'title', 'description', 'task_image']

    def test_func(self):
        task = self.get_object()
        if self.request.user.is_teacher == True and self.request.user == task.author:
            return True
        return False


class LoginFormView(SuccessMessageMixin, LoginView):
    success_message = "You've been logged in succesfully!"
