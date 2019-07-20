from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login

#Custom Imports
from .models import Task, User
from .forms import RegisterForm, StudentLoginForm, UserProfileForm

# Create your views here.

class HomeView(ListView):
    model = Task


class MyTaskView(ListView):
    model = Task


class UserProfileView(View):
    template_name = 'registration/user_form.html'

    def get(self, request):
        form_class = UserProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form_class, 'title': 'Update'})

    def post(self, request, *args, **kwargs):
        form_class = UserProfileForm(request.POST, instance=request.user)
        if form_class.is_valid():
            form_class.save()
            return redirect('user-profile')
        return render(request, self.template_name, {'form': form_class, 'title': 'Update'})


class StudentRegisterView(CreateView):
    template_name = 'registration/user_form.html'
    
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {"form": form, "title": "student"})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            studentform = form.save(commit=False)
            studentform.is_student = True
            studentform.save()
            return redirect('home')
        return render(request, self.template_name, {"form": form, "title": "student"})        


class TeacherRegisterView(CreateView):
    template_name = 'registration/user_form.html'
    
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {"form": form, "title": "teacher"})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            studentform = form.save(commit=False)
            studentform.is_teacher = True
            studentform.save()
            return redirect('home')
        return render(request, self.template_name, {"form": form, "title": "teacher"}) 


class AssignTaskView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    fields = ['student', 'title', 'description', 'task_image']
    success_url = '/'

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

