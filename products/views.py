from django.shortcuts import render, redirect, HttpResponse, reverse
from products import models
from products.forms import CategoryForm

# Create your views here.


def category_list(request):
	cate_obj = models.Category.objects.all()
	return render(request, 'products/category.html',{'cate_obj':cate_obj})

def category_add(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('products:category_list')
		else:
			return render(request, 'products/change.html', {'form': form})
	form = CategoryForm()
	return render(request, 'products/change.html', {'form': form})

def category_edit(request, pk):
	continent_obj = models.Category.objects.filter(id=pk).first()
	if not continent_obj:
		return HttpResponse('数据不存在')
	if request.method == 'GET':
		form = CategoryForm(instance=continent_obj)
		return render(request, 'products/change.html', {'form': form})
	form = CategoryForm(instance=continent_obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect('products:category_list')
	return render(request, 'products/change.html', {'form': form})

def category_del(request, pk):
	origin_url = reverse('products:category_list')
	if request.method == 'GET':
		return render(request, 'alarm.html', {'cancel': origin_url})
	models.Category.objects.filter(id=pk).delete()
	return redirect('products:category_list')
