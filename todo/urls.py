from django.urls import path
from .views import list,show_details,delete_task,add_task,edit_task
app_name='todo'
urlpatterns = [
    path('tasks/', list,name='list'),
    path('tasks/add',add_task, name='add_task'),
    path('tasks/<id>',show_details,name='show_details'),
    path('tasks/delete/<id>',delete_task,name='delete_task'),
    path('tasks/edit/<id>',edit_task,name='edit_task')

]
#
#