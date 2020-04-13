from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from auth_perm import views

urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns += [path("api-auth/", include("rest_framework.urls"))]

urlpatterns = format_suffix_patterns(urlpatterns)