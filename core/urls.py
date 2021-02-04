from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('insertion/', views.InsertionPageView.as_view(), name="insertion"),
    path('listing/', views.ListingPage, name="listing")
]