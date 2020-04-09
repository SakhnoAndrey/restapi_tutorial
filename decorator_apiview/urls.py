from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from decorator_apiview import views

urlpatterns = [
    path("", views.snippet_list),
    path("<int:pk>/", views.snippet_detail),
]
