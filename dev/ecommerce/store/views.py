from django.shortcuts import render

from . models import Category,product
# Create your views here.

from django.shortcuts import get_list_or_404

def store(request):

    all_product=product.objects.all()

    context={'my_products':all_product}
    
    return render(request,'store\store.html',context)



def categories(request):
    all_categories=Category.objects.all

    return{'all_categories':all_categories}




def product_info(request,slug):
    Product = get_list_or_404(product,slug=slug)

    context = {'product':Product}

    return render(request,'product-info.html',context)