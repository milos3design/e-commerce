from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Category, Listing


def index(request):
    return render(request, "auctions/index.html", {
        "categories": Category.objects.all(),
        "listings": Listing.objects.filter(active=True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

    
@login_required
def create(request):
    # If POST method
    if request.method == "POST":
        # Get all needed data
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image_url = request.POST["image_url"]
        category = Category.objects.filter(category_item=request.POST["category"])[0]
        creator = request.user
        # created field is inserted automatically 

        # Create listing
        lst = Listing(title=title,description=description, price=price,
        image_url=image_url, category=category, creator=creator)
        # Save listing
        lst.save()
        # Redirect to that listing using reverse
        return HttpResponseRedirect(reverse("listing", args=(lst.id,)))

    else:
        return render(request,"auctions/create.html", {
            "categories": Category.objects.all()
        })

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing
    })


def categories(request):
    return render(request, "auctions/categories.html", {
        # Return all categories
        "categories": Category.objects.all(),
    })

def category(request, category):
    # Get the current category from the argument
    current = Category.objects.get(category_item=category)
    return render(request, "auctions/category.html", {
        # From all categories, get one that matches argument
        "category": Category.objects.get(category_item=category),
        # From all listings filter only those with category same as argument
        "listings": Listing.objects.filter(category=current)
    })