from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy 
from .models import Task


# Create your views here.





class RegisterView(FormView):
	form_class = UserCreationForm
	redirect_aunthenticated_user = True
	success_url = reverse_lazy('tasks')
	template_name = "mainapp/register.html"

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterView, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('tasks')
		return super(RegisterView, self).get(*args, **kwargs)




class LoginTask(LoginView):
	fields = "__all__"
	redirect_aunthenticated_user = True
	template_name = "mainapp/login.html"

	def get_success_url(url):
		return reverse_lazy('tasks')
	

#Use mixin to restrict content from unregistered users


class TaskList(LoginRequiredMixin, ListView):
	model = Task
	template_name = "mainapp/index.html"
	context_object_name = "taskee"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['taskee'] = context['taskee'].filter(user=self.request.user)
		context['count'] = context['taskee'].filter(completed=False).count()
		search = self.request.GET.get('search-area') or ''
		if search:
			context['taskee'] = context['taskee'].filter(title__icontains=search)
			(search)
		return context

class TaskDetail(LoginRequiredMixin, DetailView):
	model = Task
	template_name = "mainapp/detail.html"
	context_object_name = "detailobject"


class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task
	template_name = "mainapp/task_form.html"
	fields = [
		'title',
		'desc',
		'completed'
	]
	context_object_name = "createtask"
	success_url = reverse_lazy('tasks')

	def form_valid(self, form):
		form.instance.user = self.request.user 
		return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
	model= Task
	fields = [
		'title',
		'desc',
		'completed'
	]

	success_url = reverse_lazy('tasks')


class DeleteTask(LoginRequiredMixin, DeleteView):
	model = Task
	template_name = "mainapp/delete.html"
	success_url = reverse_lazy('tasks')
