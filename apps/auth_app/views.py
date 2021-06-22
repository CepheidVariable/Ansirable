from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is to be the login landing page @auth_app.route('/').")