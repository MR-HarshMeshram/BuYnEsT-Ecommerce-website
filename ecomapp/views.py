from math import ceil, prod
from django.shortcuts import render
from django.http import HttpResponse
from . models import product,Contact

# Create your views here.
def  index(request):
    # product_bac=product.objects.all()
    # print(product_bac)
    # n=len(product_bac)
    # number_of_slides=n//4+ceil((n/4)-(n//4))
    # dis={'numberofslides':number_of_slides,'product':product_bac,'ranges':range(1,number_of_slides)}
    # allprods=[[product_bac, range(1, number_of_slides),number_of_slides],
    #            [product_bac, range(1,number_of_slides),number_of_slides]]
    allprods=[]
    catprods= product.objects.values('catagory','id')
    cats={item['catagory'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(catagory=cat)
        n=len(prod)
        number_of_slides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,number_of_slides),number_of_slides])
    dis={'allproducts':allprods}
    return render(request,'index.html',dis)

def  about(request):
    return render(request,'about.html')
    

def  contact(request):
        if request.method=="POST":
           name = request.POST.get('name','')
           email =request.POST.get('email','')
           phone =request.POST.get('phone','')  
           add =request.POST.get('address','')
           pin =request.POST.get('pin','')
           comm =request.POST.get('commant','')
           print(name,email,phone,add,pin,comm)
           contact=Contact(name=name,email=email,phone=phone,add=add,comm=comm,pin=pin)
           contact.save()
           
        return render(request,'contact.html')

def  tracker(request):
        return render(request,'tracker.html')


def  search(requst):
    # return render(requst,'.html')
    return HttpResponse(' we are at search page')

def  productview(request,myid):
    productv=product.objects.filter(id=myid)
    return render(request,'productview.html',{'producth':productv[0]})

def  checkout(request):
    return render(request,'checkout.html')



