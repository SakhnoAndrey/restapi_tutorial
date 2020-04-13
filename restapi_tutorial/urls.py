"""restapi_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/snippets/", include("serialization.urls")),
    path("api/v2/snippets/", include("decorator_apiview.urls")),
    path("api/v3/snippets/", include("class_apiview.urls")),
    path("api/v4/snippets/", include("mixin_class.urls")),
    path("api/v5/snippets/", include("generic_class.urls")),
    path("api/v6/", include("auth_perm.urls")),
]
