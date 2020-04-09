from django.urls import path
from serialization import views

urlpatterns = [
    path("", views.snippet_list),
    path("<int:pk>/", views.snippet_detail),
]
