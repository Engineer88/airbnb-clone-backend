from django.urls import path
from wishlists.views import Wishlists

urlpatterns = [
    path("", Wishlists.as_view()),
]
