from django.shortcuts import render
from .models import Category, Shop, Review

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
