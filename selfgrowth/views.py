from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse(' About Deepaks singh')

def cantact(request):
    return HttpResponse(' cantact Deepaks singh')

