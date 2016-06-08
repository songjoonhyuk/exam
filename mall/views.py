from django.shortcuts import render, redirect
from .models import Category, Shop, Review
from mall.forms import ShopForm

# Create your views here.

def index(request):
	category_list = Category.objects.all()
	shop_list = Shop.objects.all()
	review_list = Review.objects.all()
	return render(request, 'mall/index.html', {
		'shop_list':shop_list,
		'category_list':category_list,
		'review_list':review_list,
		})

def category_detail(request, pk):
	category = Category.objects.get(pk=pk)
	return render(request, 'mall/category_detail.html', {'category':category, })

def shop_detail(request, category_pk, pk):
	shop = Shop.objects.get(pk=pk)
	return render(request, 'mall/shop_detail.html', {'shop':shop, })

def shop_new(request, category_pk, pk):
	if request.method == 'POST':
		form = ShopForm(request.POST, request.FILES)
		if form.is_valid():
			shop = form.save()
			return redirect('mall:shop_detail', category_pk, shop.pk)
	else:
		form = ShopForm()
	return render(request, 'mall/shop_new.html', {'form':form,})