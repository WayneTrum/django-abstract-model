from django.contrib import admin

from models import ResoldCommodity, NormalCommodity, Order

admin.site.register(ResoldCommodity)
admin.site.register(NormalCommodity)
admin.site.register(Order)
