
from django.urls import path

#now import the views.py file into this code
from . import views
from django.contrib import admin
from django.http import HttpResponse, request
#from .views import GeeksFormView
#from .views import geeks_view
#from .views import list_view
urlpatterns=[
  path('admin/', admin.site.urls),
  #path('', GeeksFormView.as_view()),
  #path('<pk>/delete/', GeeksDeleteView.as_view()),
  #path('<pk>/', GeeksDetailView.as_view()),
  #path('<pk>/update', GeeksUpdateView.as_view()),
  #path('', views.GeeksCreate.as_view() ),
  #path('<id>', views.detail_view),
  #path('<id>/update', views.update_view ),
  #path('<id>/delete', views.delete_view ),
  #path('', views.create_view),
  #path('', GeeksList.as_view()),
  #path('', views.list_view),
  #path('',views.index),
  #path('', geeks_view),
  path('',views.home_view, name='home_view'),
  #path('',views.formset_view, name='formset_view'),
  ]