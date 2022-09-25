from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category_item = models.CharField(max_length=64)

    # Order categories alphabetically
    class Meta:
        ordering = ('category_item',)

    def __str__(self):
        return self.category_item


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=256, blank=True)
    category = models.ForeignKey(Category, default="Other", on_delete=models.SET_DEFAULT, related_name="categories")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_listings")
    created =  models.DateTimeField(auto_now_add=True, blank=True, null=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchers")
    active = models.BooleanField(default=True)
    bids=models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.id}  {self.title} ${self.price}"


class Bid(models.Model):
    bid_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_listings")
    bid = models.DecimalField(max_digits=6, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidders", default=0, blank=True, null=True)
    bid_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
"""
class Comment(models.Model):
    pass"""