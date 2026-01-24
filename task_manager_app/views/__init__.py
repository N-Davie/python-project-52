from django.shortcuts import render
from . import user_views
from . import status_views
from . import task_views
from . import label_views
from . import misc_views

# ========================
# Home / Index
# ========================

def home(request):
    return render(request, 'task_manager_app/index.html')
