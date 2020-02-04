from django.contrib import admin

from furnitures_ru.models import (
									Group_ru, 
									Product_ru, 
									Main_Page_ru,
									AboutImage_ru,
									AboutBlog_ru,
									AboutDiplom_ru,
									StoreAddress_ru,
									CompanyInfo_ru,
									)
							

admin.site.register(Group_ru)
admin.site.register(Product_ru)
admin.site.register(Main_Page_ru)
admin.site.register(AboutImage_ru)
admin.site.register(AboutBlog_ru)
admin.site.register(AboutDiplom_ru)
admin.site.register(StoreAddress_ru)
admin.site.register(CompanyInfo_ru)