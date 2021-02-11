from django.contrib import admin

from crud.models import Customer, Product, Sport, Team


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_doc', 'phone')


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Product, ProductAdmin)


class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Sport, SportAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Team, TeamAdmin)
