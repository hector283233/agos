from django.shortcuts import render
from django.http import HttpResponse


from .models import (
						Group, 
						Product, 
						Main_Page,
						AboutImage,
						AboutBlog,
						AboutDiplom,
						StoreAddress,
						CompanyInfo)

def index(request):
	productsBK = Product.objects.filter(product_group__group_type='BK').order_by('-pk')[:1]
	productsDG = Product.objects.filter(product_group__group_type='DG').order_by('-pk')[:1]
	productsAG = Product.objects.filter(product_group__group_type='AG').order_by('-pk')[:1]
	productsMB = Product.objects.filter(product_group__group_type='MB').order_by('-pk')[:1]
	productsDO = Product.objects.filter(product_group__group_type='DO').order_by('-pk')[:1]
	page_content = Main_Page.objects.all()[:1]
	company_info = CompanyInfo.objects.all()[:1]
	store_address = StoreAddress.objects.all()[:1]
	
	context = {'page_content': page_content,
			   'company_info': company_info,
			   'productsBK': productsBK, 
			   'productsDG': productsDG,
			   'productsAG': productsAG,
			   'productsMB': productsMB,
			   'productsDO': productsDO,
			   'store_address': store_address,}
	return render(request, "furnitures/index.html", context)

def products(request):
	productsBK = Product.objects.filter(product_group__group_type='BK').order_by('-pk')
	productsDG = Product.objects.filter(product_group__group_type='DG').order_by('-pk')
	productsAG = Product.objects.filter(product_group__group_type='AG').order_by('-pk')
	productsMB = Product.objects.filter(product_group__group_type='MB').order_by('-pk')
	productsDO = Product.objects.filter(product_group__group_type='DO').order_by('-pk')
	groupsBK = Group.objects.filter(group_type = 'BK')
	groupsDG = Group.objects.filter(group_type = 'DG')
	groupsAG = Group.objects.filter(group_type = 'AG')
	groupsMB = Group.objects.filter(group_type = 'MB')
	groupsDO = Group.objects.filter(group_type = 'DO')
	company_info = CompanyInfo.objects.all()[:1]
	store_address = StoreAddress.objects.all()[:1]
	
	context = {
			   'company_info': company_info,
			   'productsBK': productsBK, 
			   'productsDG': productsDG,
			   'productsAG': productsAG,
			   'productsMB': productsMB,
			   'productsDO': productsDO,
			   'groupsBK':groupsBK,
			   'groupsDG':groupsDG,
			   'groupsAG':groupsAG,
			   'groupsMB':groupsMB,
			   'groupsDO':groupsDO,
			   'store_address': store_address,
			   }
	return render(request, 'furnitures/products.html', context)

def products_agacgapylar(request):
	company_info = CompanyInfo.objects.all()[:1]
	groups = Group.objects.filter(group_type = 'AG')
	productsAG = Product.objects.filter(product_group__group_type='AG').order_by('product_group').order_by('-pk')
	store_address = StoreAddress.objects.all()[:1]
	context = {'productsAG':productsAG, 'groups':groups, 'company_info': company_info, 'store_address':store_address}
	return render(request, 'furnitures/products_agacgapylar.html', context)

def products_beylekiler(request):
	company_info = CompanyInfo.objects.all()[:1]
	groups = Group.objects.filter(group_type = 'BK')
	productsBK = Product.objects.filter(product_group__group_type='BK').order_by('product_group').order_by('-pk')
	store_address = StoreAddress.objects.all()[:1]
	context = {'productsBK':productsBK, 'groups':groups, 'company_info': company_info, 'store_address':store_address}
	return render(request, 'furnitures/products_beylekiler.html', context)

def products_demirgapylar(request):
	company_info = CompanyInfo.objects.all()[:1]
	groups = Group.objects.filter(group_type = 'DG')
	productsDG = Product.objects.filter(product_group__group_type='DG').order_by('product_group').order_by('-pk')
	store_address = StoreAddress.objects.all()[:1]
	context = {'productsDG':productsDG, 'groups':groups, 'company_info': company_info, 'store_address':store_address}
	return render(request, 'furnitures/products_demirgapylar.html', context)

def products_demironumler(request):
	company_info = CompanyInfo.objects.all()[:1]
	groups = Group.objects.filter(group_type = 'DO')
	productsDO = Product.objects.filter(product_group__group_type='DO').order_by('product_group').order_by('-pk')
	store_address = StoreAddress.objects.all()[:1]
	context = {'productsDO':productsDO, 'groups':groups, 'company_info': company_info, 'store_address':store_address}
	return render(request, 'furnitures/products_demironumler.html', context)

def products_mebeller(request):
	company_info = CompanyInfo.objects.all()[:1]
	groups = Group.objects.filter(group_type = 'MB')
	productsMB = Product.objects.filter(product_group__group_type='MB').order_by('product_group').order_by('-pk')
	store_address = StoreAddress.objects.all()[:1]
	context = {'productsMB':productsMB, 'groups':groups, 'company_info': company_info, 'store_address': store_address}
	return render(request, 'furnitures/products_mebeller.html', context)

def about(request):
	about_image = AboutImage.objects.all()[:1]
	company_info = CompanyInfo.objects.all()[:1]
	store_address = StoreAddress.objects.all()[:1]
	about_blog = AboutBlog.objects.all()
	about_diplom = AboutDiplom.objects.all()
	context = { 'company_info': company_info, 
				'store_address':store_address, 
				'about_image': about_image, 
				'about_blog':about_blog,
				'about_diplom':about_diplom}
	return render(request, 'furnitures/about.html', context)

def contact(request):
	store_address = StoreAddress.objects.all()
	company_info = CompanyInfo.objects.all()[:1]
	store_address = StoreAddress.objects.all()[:1]
	context = {'company_info': company_info, 'store_address':store_address, 'store_address':store_address}
	return render(request, 'furnitures/contact.html', context)