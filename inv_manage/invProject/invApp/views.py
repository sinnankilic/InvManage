from django.shortcuts import render, redirect,get_object_or_404 

from .models import Product
from .forms import ProductForm

# Create your views here.


#home view

def home_view(request):
      return render(request,'invApp/home.html')


#create view
def product_create_view(request):

      form=ProductForm()

      if request.method=="POST":
            form=ProductForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('product_list')
            
      return render(request, 'invApp/product_form.html',{'form':form})



#read view

def product_list_view(request):
      
      products=Product.objects.all()

      return render(request ,'invApp/product_list.html',{'products':products})


#update view

def product_update_view(request,product_id):

      product=Product.objects.get(product_id=product_id)

      if request.method=='POST':
            form=ProductForm(request.POST,instance=product)
            if form.is_valid():
                  form.save()

                  return redirect('product_list')
      
      else:
            form=ProductForm(instance= product)
      
      return render(request,'invApp/product_form.html',{'form':form})




#delete view

def product_delete_view(request,product_id):
      product=get_object_or_404(Product,product_id=product_id)
      if request.method=='POST':
            product.delete()
            return redirect('product_list')
      return render(request,'invApp/product_confirm_delete.html',{'product':product})

