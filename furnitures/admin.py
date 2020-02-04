from django.contrib import admin

from furnitures.models import (
								Group, 
								Product, 
								Main_Page,
								AboutImage,
								AboutBlog,
								AboutDiplom,
								StoreAddress,
								CompanyInfo,
								)
							

admin.site.register(Group)
admin.site.register(Product)
admin.site.register(Main_Page)
admin.site.register(AboutImage)
admin.site.register(AboutBlog)
admin.site.register(AboutDiplom)
admin.site.register(StoreAddress)
admin.site.register(CompanyInfo)