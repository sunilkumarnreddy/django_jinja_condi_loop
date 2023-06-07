from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Nikky','age':10}
    return render(request,'wish.html',context=d)


def conditions(request):
    d={'a':24400,'b':3600,'c':400}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'ASHU'}
    return render(request,'loops.html',d)