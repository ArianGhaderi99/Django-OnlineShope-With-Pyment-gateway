from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'pages/home.html',context={'test':1234})