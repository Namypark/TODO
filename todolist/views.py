from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'todolist/index.html')


@csrf_exempt
def add_item(request):
    from datetime import timezone
    content = request.POST('content')
    added_timezone = timezone.now()
    print(content)
    print(added_timezone)
    # base_url = "add_item/?add-item{}"
    return render(request, "todolist/index.html")
