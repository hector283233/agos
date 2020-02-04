from django.db import models

class Group(models.Model):
	TYPES = (
				('DG', 'Demir Gapylar'),
				('AG', 'Agaç Gapylar'),
				('MB', 'Mebeller'),
				('DO', 'Demir Önümler'),
				('BK', 'Beýlekiler'),
			)
	group_name			= models.CharField("Gruppanyn ady", max_length=128)
	group_type			= models.CharField("Topary", max_length=2, choices=TYPES)

	def __str__(self):
		return self.group_name
			

class Product(models.Model):
	product_name		= models.CharField("Harydyň ady", max_length=128)
	product_group		= models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name="Gruppasy")
	product_image 		= models.ImageField("Haryt Suraty", upload_to = 'images/', default = 'images/default.jpg')
	product_description = models.TextField("Haryt Barada Giňişleýin Maglumat", blank=True)
	is_new				= models.BooleanField("Täzemi?", default=1)

	def __str__(self):
		return self.product_name

class Main_Page(models.Model):
	img_slide1 			= models.ImageField("Slayt1", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide2 			= models.ImageField("Slayt2", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide3 			= models.ImageField("Slayt3", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide4 			= models.ImageField("Slayt4", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide5 			= models.ImageField("Slayt5", upload_to = 'furnitures/images/', default = 'default.jpg')
	img_slide6 			= models.ImageField("Slayt6", upload_to = 'furnitures/images/', default = 'default.jpg')

	text_slide1 		= models.CharField("Slayt1 tekst", blank=True, max_length=32)
	text_slide2 		= models.CharField("Slayt2 tekst", blank=True, max_length=32)
	text_slide3 		= models.CharField("Slayt3 tekst", blank=True, max_length=32)
	text_slide4 		= models.CharField("Slayt4 tekst", blank=True, max_length=32)
	text_slide5 		= models.CharField("Slayt5 tekst", blank=True, max_length=32)
	text_slide6 		= models.CharField("Slayt6 tekst", blank=True, max_length=32)

	description_slide1 	= models.TextField("Slayt1 Giňişleýin", blank=True)
	description_slide2 	= models.TextField("Slayt2 Giňişleýin", blank=True)
	description_slide3 	= models.TextField("Slayt3 Giňişleýin", blank=True)
	description_slide4 	= models.TextField("Slayt4 Giňişleýin", blank=True)
	description_slide5 	= models.TextField("Slayt5 Giňişleýin", blank=True)
	description_slide6 	= models.TextField("Slayt6 Giňişleýin", blank=True)

	main_title	 		= models.CharField("Ady", blank=True, max_length=64)

	about_main 			= models.TextField("Giňişleýin", blank=True)

	property1_title		= models.CharField("Hyzmat Ady 1: ", blank=True, max_length=32)
	property1			= models.ImageField("Icon1", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property1		= models.TextField("Hyzmat1 Giňişleýin")

	property2_title		= models.CharField("Hyzmat Ady 2: ", blank=True, max_length=32)
	property2			= models.ImageField("Icon2", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property2		= models.TextField("Hyzmat2 Giňişleýin")

	property3_title		= models.CharField("Hyzmat Ady 3: ", blank=True, max_length=32)
	property3			= models.ImageField("Icon3", upload_to = 'furnitures/images/', default = 'default.jpg')
	text_property3		= models.TextField("Hyzmat3 Giňişleýin")


	# 8 sany ayratyn HARYTLAR, link yok (ya-ad hemmesi ahli harytlara gityar).

	dif_product1_img	= models.ImageField("Harydyň ady 1", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product1_txt	= models.CharField("Harytlar Teksti 1:", blank=True, max_length=32)

	dif_product2_img	= models.ImageField("Harydyň ady 2", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product2_txt	= models.CharField("Harytlar Teksti 2:", blank=True, max_length=32)

	dif_product3_img	= models.ImageField("Harydyň ady 3", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product3_txt	= models.CharField("Harytlar Teksti 3:", blank=True, max_length=32)

	dif_product4_img	= models.ImageField("Harydyň ady 4", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product4_txt	= models.CharField("Harytlar Teksti 4:", blank=True, max_length=32)

	dif_product5_img	= models.ImageField("Harydyň ady 5", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product5_txt	= models.CharField("Harytlar Teksti 5:", blank=True, max_length=32)

	dif_product6_img	= models.ImageField("Harydyň ady 6", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product6_txt	= models.CharField("Harytlar Teksti 6:", blank=True, max_length=32)

	dif_product7_img	= models.ImageField("Harydyň ady 7", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product7_txt	= models.CharField("Harytlar Teksti 7:", blank=True, max_length=32)

	dif_product8_img	= models.ImageField("Harydyň ady 8", upload_to = 'furnitures/images/', default = 'default.jpg')
	dif_product8_txt	= models.CharField("Harytlar Teksti 8:", blank=True, max_length=32)

	def __str__(self):
		return "Baş Sahypa"



class AboutImage(models.Model):
	about_main_image	= models.ImageField("Biz Barada Suraty: ", upload_to = 'furnitures/about/', default = 'default.jpg')

	def __str__(self):
		return "Biz Barada Ýokarky Surat"


class AboutBlog(models.Model):
	blog_title			= models.CharField("Ady: ", max_length=32)
	blog_text			= models.TextField("Teksti: ")
	blog_img			= models.ImageField("Suraty: ", upload_to = 'furnitures/about/', default = 'default.jpg')
	
	def __str__(self):
		return self.blog_title

class AboutDiplom(models.Model):
	diplom_txt			= models.CharField("Diplom Ady:", max_length=32)
	diplom_img			= models.ImageField("Diplom Suraty", upload_to = 'furnitures/about/', default = 'default.jpg')
	
	def __str__(self):
		return self.diplom_txt


class StoreAddress(models.Model):
	google_map_link		= models.TextField("Google Karta Link")
	store_img			= models.ImageField("Magazin Suraty", upload_to = 'furnitures/stores/', default='default.jpg')
	address_line1		= models.CharField("Address 1 setir : ", max_length=64)
	address_line2 		= models.CharField("Address 2 setir : ", blank=True, max_length=64)
	phone1				= models.CharField("Telefon 1 ", max_length=32)
	phone2				= models.CharField("Telefon 2 ", blank=True, max_length=32)
	phone3				= models.CharField("Telefon 3 ", blank=True, max_length=32)
	e_mail				= models.CharField("Email : ", blank=True, max_length=32)

	def __str__(self):
		return self.address_line2


class CompanyInfo(models.Model):
	company_name 		= models.CharField("Kärhananyň Ady: ", max_length=32)
	company_logo		= models.ImageField("Kärhana Logotip: ", upload_to='furnitures/logo/', default='default.jpg')
	company_slogan		= models.CharField("Kärhananyň Slogany: ", max_length=128)

	def __str__(self):
		return self.company_name