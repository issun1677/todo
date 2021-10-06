from django.urls import path

from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask, LoginTask, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [

	path('', TaskList.as_view(), name="tasks"),
	path('task/<int:pk>/', TaskDetail.as_view(), name='detailtask'),
	path('create-task/', TaskCreate.as_view(), name="createtask"),
	path('task-update/<int:pk>/', TaskUpdate.as_view(), name='updatetask'),
	path('task-delete/<int:pk>/', DeleteTask.as_view(), name='deletetask'),
	path('register/', RegisterView.as_view(), name="register"),
	path('login/', LoginTask.as_view(), name="login"),
	path('logout/', LogoutView.as_view(next_page='login'), name="logout")
]
