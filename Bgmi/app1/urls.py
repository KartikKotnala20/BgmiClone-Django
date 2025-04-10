from django.urls import path
from . import views
urlpatterns = [
  path('1',views.home),
  path('2',views.news),
  path('3',views.resp),
]