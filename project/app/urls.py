from django.urls import path
from .views import index_view, save_json


urlpatterns = [
    path('', index_view , name="index_view"),
    path('save_json/', save_json , name="save_json"),
]