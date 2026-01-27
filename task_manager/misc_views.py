from django.shortcuts import render
from django.http import HttpResponse
import rollbar

def home(request):
    return render(request, 'task_manager_app/index.html')

def rollbar_test(request):
    try:
        1 / 0
    except ZeroDivisionError:
        rollbar.report_exc_info()
    return HttpResponse("Тестовое событие отправлено в Rollbar")
