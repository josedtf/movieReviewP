from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Jose David Toro'})

#def About(request):
#    return HttpResponse('<h1>Welome to about page</h1>')