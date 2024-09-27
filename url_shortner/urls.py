from django.urls import path 
from .views import index ,index_form 
from . import views
urlpatterns = [ 
	path('',views.index), 
	path('index_form/',views.index_form,name='index_form'), 
]
