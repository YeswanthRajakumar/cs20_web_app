from django.shortcuts import render
import datetime
from .models import Course


# Create your views here.

def home_page(request):
    today = datetime.datetime.now()

    data = {
        "username": "Yash",
        "date": str(today.date()),
        "time": str(today.time()),
        "courses": Course.objects.all()
    }
    return render(request, template_name='courses/index.html', context=data)




