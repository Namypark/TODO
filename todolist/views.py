from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'todolist/index.html')


@csrf_exempt
def add_item(request):

    #! fix the content printing on the console
    content = request.POST.get('content')
    added_time = timezone.now()
    print(content)
    print(added_time)
    return render(request, "todolist/index.html")
