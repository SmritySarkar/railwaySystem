from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    return render(request, 'index.html')


def register(request):

    return render(request, 'register.html')


def signIn(request):

    return render(request, 'signIn.html')


def aboutUs(request):

    return render(request, 'aboutUs.html')


def userHome(request):

    return render(request, 'userHome.html')

def userAbout(request):

    return render(request, 'userAbout.html')

def reserve(request):

    return render(request, 'reserve.html')
