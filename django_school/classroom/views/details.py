from django.shortcuts import redirect, render
from django.views.generic import TemplateView




def about(request):
    return render(request, 'classroom/detail/about.html')

def contact(request):
    return render(request, 'classroom/detail/contact.html')
def what_we_do(request):
    return render(request, 'classroom/detail/what_we_do.html')
def case(request):
    return render(request, 'classroom/detail/cose.html')
