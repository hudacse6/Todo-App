from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from tdapp.models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_item = Todo.objects.all().order_by('-date_added')
    return render(request, 'main/index.html', {'passing_todo_item': todo_item})


@csrf_exempt
def add_todo(request):
    # print(request.POST)
    show_date = timezone.now()
    show_text = request.POST['content']
    # print('Date is shown here...: ', show_date)
    # print('txt is shown here: ', show_content)
    create_txt = Todo.objects.create(date_added=show_date, text=show_text)
    # print(create_txt)
    # print(create_txt.id)
    # count_all_created_todo_item = Todo.objects.all().count()
    # print(count_all_created_todo_item)
    # return render(request, 'main/index.html')
    # ---- this is not working because after creating the text it will go this address but we need to go base address page
    return HttpResponseRedirect('/')


@csrf_exempt
def text_delete(request, todo_id):
    # print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')