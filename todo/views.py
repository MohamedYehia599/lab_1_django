from django.shortcuts import render,HttpResponse
from .forms import task_form
my_list=[
    {
        'id':1,
        'name':'breakfast',
        'is_done':False,
        'description':'to eat your first meal'
    },
    {
        'id':2,
        'name':'attend lecture',
        'is_done':False,
        'description':'to attend the lecture '
    },
    {
        'id':3,
        'name':'make lab',
        'is_done':False,
        'description':'to make the lab '
    },
    {
        'id':4,
        'name':'launch',
        'is_done':False,
        'description':'to eat your second meal '
    }


]


def list(request):

    return render(request,'todo/home.html',context={'todo_list':my_list})

def show_details(request ,**kwargs):
    # print(kwargs.get('id'))
    id=int(kwargs.get('id'))
    task=my_list[id-1]


    return render(request,'todo/details.html',context={'task':task})
def delete_task(request,**kwargs):

    id = int(kwargs.get('id'))
    if(my_list[id-1].get('is_done')):

        my_list.pop(id-1)
        return list(request)
    else:
        return render(request,'todo/home.html',{'todo_list':my_list,'warning':'task cant be deleted unless it is done'})


# def render_form(request,**kwargs):
#     if(kwargs):
#         id = int(kwargs.get('id'))
#         task = my_list[id - 1]
#         return  render(request,'todo/todo_form.html',context={'task':task,'bool':True})
#     else:
#         return render(request, 'todo/todo_form.html', context={'bool': False})

def render_form(request,**kwargs):
    print('O7EHA')

def add_task(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = task_form(request.POST)  # A form bound to the POST data
        if form.is_valid():
            task={
            'id':form.cleaned_data['id'],
            'name' : form.cleaned_data['name'],
            'is_done': form.cleaned_data['is_done'],
            'description' : form.cleaned_data['description']
            }
            my_list.append(task)
            return list(request)

    form = task_form()
    return render(request, 'todo/task_form.html', {'form': form})


def edit_task(request,**kwargs):
    if request.method == 'POST':  # If the form has been submitted...
        form = task_form(request.POST)  # A form bound to the POST data
        if form.is_valid():
            task={
            'id':form.cleaned_data['id'],
            'name' : form.cleaned_data['name'],
            'is_done': form.cleaned_data['is_done'],
            'description' : form.cleaned_data['description']
            }
            id = int(kwargs.get('id'))
            my_list[id - 1]=task
            return list(request)

    form = task_form()
    return render(request, 'todo/task_form.html', {'form': form})