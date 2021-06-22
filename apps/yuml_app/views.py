from django.shortcuts import render, HttpResponse

# Create your views here.
def yuml(request):
    return HttpResponse("This will be the dashboard for the yamlbuilder @app.route('/yuml').")