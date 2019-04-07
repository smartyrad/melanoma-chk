# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from shopclues import *
from amazon_india import *
from amazon_global import *
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage




data = []


# Create your views here.


def pricecheck(request):
    return render(request, 'pricecheck/index.html', {})


def results(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'pricecheck/results.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'pricecheck/results.html')