from django.contrib import admin

from .models import Category, Forex, Stock, Commodity, Crypto
admin.site.register(Category)
admin.site.register(Forex)
admin.site.register(Stock)
admin.site.register(Commodity)
admin.site.register(Crypto)



