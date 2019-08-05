from django.shortcuts import render
from webapp.models import Emp
from django.http import HttpResponse
# Create your views here.

def Emp_view(request):
    Emp_list=Emp.objects.all()
    my_dict={'elist':Emp_list}
    return render(request,'myapp/welcome.html',my_dict)