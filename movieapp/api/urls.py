from django.urls import path
from .views import detailpage, homepage
urlpatterns = [
    path('all/', homepage, name='homepage'),
    path('<int:pk>/', detailpage, name='detailpage'),
]
