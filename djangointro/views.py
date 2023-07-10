from django.shortcuts import render


def index (request):
    return render(request, 'index.html')
def innerpage (request):
    return render(request, 'inner-page.html')