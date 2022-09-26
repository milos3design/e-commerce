from django.contrib import admin
from .models import User, Category, Listing, Bid, Comment

# Adds datetime to admin dashboard
class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Adds datetime to admin dashboard
class BidAdmin(admin.ModelAdmin):
    readonly_fields = ('bid_created',)

# Adds datetime to admin dashboard
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)