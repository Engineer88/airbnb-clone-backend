from django.urls import path
from experiences import views

urlpatterns = [
    path("perks/", views.Perks.as_view()),
    path("perks/<int:pk>", views.PerkDetail.as_view()),
]
