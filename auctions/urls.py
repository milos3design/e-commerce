from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("add_watch/<int:listing_id>", views.add_watch, name="add_watch"),
    path("remove_watch/<int:listing_id>", views.remove_watch, name="remove_watch"),
    path("watchlist", views.users_watchlist, name="users_watchlist"),
    path("create", views.create, name="create"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
