from django.contrib import admin
from .models import User, Category, Listing

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)