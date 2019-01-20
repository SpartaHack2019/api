from django.urls import path
from . import views

urlpatterns = [
    path('<int:image_id>', views.download_image),
]