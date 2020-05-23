from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


def product_list(request):
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    product_list=paginator.get_page(page)
    context={"products":product_list}
    return render(request,'product/product_list.html',context)

def product_detail(request,slug):
    #product_detail=Product.objects.get(slug=slug)
    product_detail=get_object_or_404(Product,slug=slug)
    #product_detail=Product.objects.get(id=id)
    context={'productdetail':product_detail}
    return render(request,'product/product_detail.html',context)


"""def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/product_list.html', {'productslist': page_obj})"""



"""def index(request):
    user_list = Product.objects.all()
  #  print(user_list)
    page = request.GET.get('page')
 #   print(page)
    paginator = Paginator(user_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'product/product_list.html', { 'users': users })"""
