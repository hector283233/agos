from django.shortcuts import render
from django.http import HttpResponse


from .models import (
					Group_ru, 
					Product_ru, 
					Main_Page_ru,
					AboutImage_ru,
					AboutBlog_ru,
					AboutDiplom_ru,
					StoreAddress_ru,
					CompanyInfo_ru,)

def index(request):
	productsBK = Product_ru.objects.filter(product_group__group_type='BK').order_by('-pk')[:1]
	productsDG = Product_ru.objects.filter(product_group__group_type='DG').order_by('-pk')[:1]
	productsAG = Product_ru.objects.filter(product_group__group_type='AG').order_by('-pk')[:1]
	productsMB = Product_ru.objects.filter(product_group__group_type='MB').order_by('-pk')[:1]
	productsDO = Product_ru.objects.filter(product_group__group_type='DO').order_by('-pk')[:1]
	page_content = Main_Page_ru.objects.all()[:1]
	company_info = CompanyInfo_ru.objects.all()[:1]
	store_address =StoreAddress_ru.objects.all()[:1]
	
	context = {'page_content': page_content, 
			   'productsBK': productsBK, 
			   'productsDG': productsDG,
			   'productsAG': productsAG,
			   'productsMB': productsMB,
			   'productsDO': productsDO,
			   'company_info':company_info,
			   'store_address':store_address,}
	return render(request, "furnitures_ru/index.html", context)

def products(request):
	productsBK = Product_ru.objects.filter(product_group__group_type='BK').order_by('-pk')
	productsDG = Product_ru.objects.filter(product_group__group_type='DG').order_by('-pk')
	productsAG = Product_ru.objects.filter(product_group__group_type='AG').order_by('-pk')
	productsMB = Product_ru.objects.filter(product_group__group_type='MB').order_by('-pk')
	productsDO = Product_ru.objects.filter(product_group__group_type='DO').order_by('-pk')
	groupsBK = Group_ru.objects.filter(group_type = 'BK')
	groupsDG = Group_ru.objects.filter(group_type = 'DG')
	groupsAG = Group_ru.objects.filter(group_type = 'AG')
	groupsMB = Group_ru.objects.filter(group_type = 'MB')
	groupsDO = Group_ru.objects.filter(group_type = 'DO')
	company_info = CompanyInfo_ru.objects.all()[:1]
	store_address =StoreAddress_ru.objects.all()[:1]
	
	context = {
			   'company_info':company_info,
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
			   'store_address':store_address,
			   }
	return render(request, 'furnitures_ru/products.html', context)

def products_agacgapylar(request):
	company_info = CompanyInfo_ru.objects.all()[:1]
	groups = Group_ru.objects.filter(group_type = 'AG')
	productsAG = Product_ru.objects.filter(product_group__group_type='AG').order_by('product_group').order_by('-pk')
	store_address = StoreAddress_ru.objects.all()[:1]
	context = {'productsAG':productsAG, 'groups':groups, 'company_info':company_info, 'store_address':store_address}
	return render(request, 'furnitures_ru/products_agacgapylar.html', context)

def products_beylekiler(request):
	company_info = CompanyInfo_ru.objects.all()[:1]
	groups = Group_ru.objects.filter(group_type = 'BK')
	productsBK = Product_ru.objects.filter(product_group__group_type='BK').order_by('product_group').order_by('-pk')
	store_address = StoreAddress_ru.objects.all()[:1]
	context = {'productsBK':productsBK, 'groups':groups, 'store_address':store_address, 'company_info':company_info}
	return render(request, 'furnitures_ru/products_beylekiler.html', context)

def products_demirgapylar(request):
	company_info = CompanyInfo_ru.objects.all()[:1]
	groups = Group_ru.objects.filter(group_type = 'DG')
	productsDG = Product_ru.objects.filter(product_group__group_type='DG').order_by('product_group').order_by('-pk')
	store_address = StoreAddress_ru.objects.all()[:1]
	context = {'productsDG':productsDG, 'groups':groups, 'company_info':company_info, 'store_address':store_address}
	return render(request, 'furnitures_ru/products_demirgapylar.html', context)

def products_demironumler(request):
	company_info = CompanyInfo_ru.objects.all()[:1]
	groups = Group_ru.objects.filter(group_type = 'DO')
	productsDO = Product_ru.objects.filter(product_group__group_type='DO').order_by('product_group').order_by('-pk')
	store_address = StoreAddress_ru.objects.all()[:1]
	context = {'productsDO':productsDO, 'groups':groups, 'company_info': company_info, 'store_address':store_address}
	return render(request, 'furnitures_ru/products_demironumler.html', context)

def products_mebeller(request):
	company_info = CompanyInfo_ru.objects.all()[:1]
	groups = Group_ru.objects.filter(group_type = 'MB')
	productsMB = Product_ru.objects.filter(product_group__group_type='MB').order_by('product_group').order_by('-pk')
	store_address = StoreAddress_ru.objects.all()[:1]
	context = {'productsMB':productsMB, 'groups':groups, 'company_info':company_info, 'store_address':store_address}
	return render(request, 'furnitures_ru/products_mebeller.html', context)

def about(request):
	about_image = AboutImage_ru.objects.all()[:1]
	company_info = CompanyInfo_ru.objects.all()[:1]
	store_address = StoreAddress_ru.objects.all()[:1]
	about_blog = AboutBlog_ru.objects.all()
	about_diplom = AboutDiplom_ru.objects.all()
	context = { 'company_info': company_info, 
				'store_address':store_address, 
				'about_image': about_image, 
				'about_blog':about_blog,
				'about_diplom':about_diplom}
	return render(request, 'furnitures_ru/about.html', context)

def contact(request):
	store_address = StoreAddress_ru.objects.all()
	company_info = CompanyInfo_ru.objects.all()[:1]
	store_address = StoreAddress_ru.objects.all()[:1]
	context = {'company_info': company_info, 'store_address':store_address, 'store_address':store_address}
	return render(request, 'furnitures_ru/contact.html', context)