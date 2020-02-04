from django.db import models

class Group_ru(models.Model):
	TYPES = (
				('DG', 'Demir Gapylar'),
				('AG', 'Agaç Gapylar'),
				('MB', 'Mebeller'),
				('DO', 'Demir Önümler'),
				('BK', 'Beýlekiler'),
			)
	group_name			= models.CharField("Имя группы", max_length=128)
	group_type			= models.CharField("Тип группы", max_length=2, choices=TYPES)

	def __str__(self):
		return self.group_name
			

class Product_ru(models.Model):
	product_name		= models.CharField("Имя продукта", max_length=128)
	product_group		= models.ForeignKey(Group_ru, on_delete=models.SET_NULL, null=True, verbose_name="Группа")
	product_image 		= models.ImageField("Фото", upload_to = 'images/', default = 'images/default.jpg')
	product_description = models.TextField("Подробно", blank=True)
	is_new				= models.BooleanField("Новый", default=1)

	def __str__(self):
		return self.product_name

class Main_Page_ru(models.Model):
	img_slide1 			= models.ImageField("Слайд1", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide2 			= models.ImageField("Слайд2", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide3 			= models.ImageField("Слайд3", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide4 			= models.ImageField("Слайд4", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide5 			= models.ImageField("Слайд5", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide6 			= models.ImageField("Слайд6", upload_to = 'furnitures/images/', default = 'default.jpg')

	text_slide1 		= models.CharField("Слайд1 текст", blank=True, max_length=32)
	text_slide2 		= models.CharField("Слайд2 текст", blank=True, max_length=32)
	text_slide3 		= models.CharField("Слайд3 текст", blank=True, max_length=32)
	text_slide4 		= models.CharField("Слайд4 текст", blank=True, max_length=32)
	text_slide5 		= models.CharField("Слайд5 текст", blank=True, max_length=32)
	text_slide6 		= models.CharField("Слайд6 текст", blank=True, max_length=32)

	description_slide1 	= models.TextField("Слайд1 Подробно", blank=True)
	description_slide2 	= models.TextField("Слайд2 Подробно", blank=True)
	description_slide3 	= models.TextField("Слайд3 Подробно", blank=True)
	description_slide4 	= models.TextField("Слайд4 Подробно", blank=True)
	description_slide5 	= models.TextField("Слайд5 Подробно", blank=True)
	description_slide6 	= models.TextField("Слайд6 Подробно", blank=True)

	main_title	 		= models.CharField("Имя ", blank=True, max_length=64)

	about_main			= models.TextField('Подробно', blank=True)

	property1_title		= models.CharField("Имя Услуги1: ", blank=True, max_length=32)
	property1			= models.ImageField("Icon1", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property1		= models.TextField("Услуга1")

	property2_title		= models.CharField("Имя Услуги2: ", blank=True, max_length=32)
	property2			= models.ImageField("Icon2", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property2		= models.TextField("Услуга2")

	property3_title		= models.CharField("Имя Услуги3: ", blank=True, max_length=32)
	property3			= models.ImageField("Icon3", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property3		= models.TextField("Услуга3")


	# 8 sany ayratyn HARYTLAR, link yok (ya-ad hemmesi ahli harytlara gityar).

	dif_product1_img	= models.ImageField("Имя Продукта 1", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product1_txt	= models.CharField("Текст Продукции 1", blank=True, max_length=32)

	dif_product2_img	= models.ImageField("Имя Продукта 2", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product2_txt	= models.CharField("Текст Продукции 2:", blank=True, max_length=32)

	dif_product3_img	= models.ImageField("Имя Продукта 3", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product3_txt	= models.CharField("Текст Продукции 3", blank=True, max_length=32)

	dif_product4_img	= models.ImageField("Имя Продукта 4", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product4_txt	= models.CharField("Текст Продукции 4", blank=True, max_length=32)

	dif_product5_img	= models.ImageField("Имя Продукта 5", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product5_txt	= models.CharField("Текст Продукции 5", blank=True, max_length=32)

	dif_product6_img	= models.ImageField("Имя Продукта 6", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product6_txt	= models.CharField("Текст Продукции 6", blank=True, max_length=32)

	dif_product7_img	= models.ImageField("Имя Продукта 7", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product7_txt	= models.CharField("Текст Продукции 7", blank=True, max_length=32)

	dif_product8_img	= models.ImageField("Имя Продукта 8", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product8_txt	= models.CharField("Текст Продукции 8", blank=True, max_length=32)

	def __str__(self):
		return "Главная Страница"



class AboutImage_ru(models.Model):
	about_main_image	= models.ImageField("Фото о нас: ", upload_to = 'furnitures/about/', default = 'default.jpg')

	def __str__(self):
		return "Главное фото о нас"


class AboutBlog_ru(models.Model):
	blog_title			= models.CharField("Имя: ", max_length=32)
	blog_text			= models.TextField("Текст: ")
	blog_img			= models.ImageField("Фото: ", upload_to = 'furnitures/about/', default = 'default.jpg')
	
	def __str__(self):
		return self.blog_title

class AboutDiplom_ru(models.Model):
	diplom_txt			= models.CharField("Имя Сертификата:", max_length=32)
	diplom_img			= models.ImageField("Фото Сертификата", upload_to = 'furnitures/about/', default = 'default.jpg')
	
	def __str__(self):
		return self.diplom_txt


class StoreAddress_ru(models.Model):
	google_map_link		= models.TextField("Ссылка Google Карта")
	store_img			= models.ImageField("Фото Магазина", upload_to = 'furnitures/stores/', default='default.jpg')
	address_line1		= models.CharField("Аддресс Строка 1 : ", max_length=64)
	address_line2 		= models.CharField("Аддресс Строка 2 : ", blank=True, max_length=64)
	phone1				= models.CharField("Телефон 1 ", max_length=32)
	phone2				= models.CharField("Телефон 2 ", blank=True, max_length=32)
	phone3				= models.CharField("Телефон 3 ", blank=True, max_length=32)
	e_mail				= models.CharField("Email : ", blank=True, max_length=32)

	def __str__(self):
		return self.address_line2


class CompanyInfo_ru(models.Model):
	company_name 		= models.CharField("Имя Фирмы: ", max_length=32)
	company_logo		= models.ImageField("Логотип Фирмы: ", upload_to='furnitures/logo/', default='default.jpg')
	company_slogan		= models.CharField("Слоган Фирмы: ", max_length=128)

	def __str__(self):
		return self.company_name