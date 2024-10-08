from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include("restaurant.urls")),  # Ensure 'restaurant.urls' is in quotes
]