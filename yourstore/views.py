from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This Sarswat ka lowra page.")
def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')