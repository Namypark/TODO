from .models import Todo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.order_by('added_date')
    return render(request, 'todolist/index.html',{
        "todo_items": todo_items
    })


@csrf_exempt
def add_item(request):

    #! fix the content printing on the console
    content = request.POST.get('content')
    added_time = timezone.now()
    created_object = Todo.objects.create(text=content, added_date=added_time)

    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
