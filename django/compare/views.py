from django.shortcuts import render
from django.http import HttpResponse
from .models import CompareList,Result

def index(request):
    my_dict={'dic_compare':'This is from compare.'}
    #return HttpResponse("<em>compare</em>")
    return render(request,'index.html',context=my_dict)

def result(request):
    compareList=CompareList.objects.order_by('data')
    my_dict={'dic_compare':'This is from compare.'}
    return render(request,'index.html',context=my_dict)

# def school_info(request, centre_code):
# 	school = School.object.filter(centre_code=centre_code)
# 	name = school.centre_name
# 	return HttpResponse("You are look at school %s.".format(name))


# Create your views here.
