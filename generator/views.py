from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render (request, 'generator/home.html')

def about(request):
    return render (request, 'generator/about.html')

def password(request):
    thepassword = 'testing'
    characters = list('0123456')

        #if request.GET.get('uppercase'):
        #characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        #if request.GET.get('special'):
        #characters.extend(list('!@#$%^&*()'))"""

    if request.GET.get('numbers'):
        characters.extend(list('0123456'))

    length= int(request.GET.get('length',1))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render (request, 'generator/password.html', {'password':thepassword})

