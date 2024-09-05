from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):

    date = datetime.today()

    return render(request, 'index.html', context={"date": date})
