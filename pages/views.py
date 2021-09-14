from django.shortcuts import render


# Create your views here.
def joyful(request):
    return render(request, 'index.html')
