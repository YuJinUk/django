from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>/', views.detail, name = 'detail'),
    # path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('dellete/<int:pk>/', views.dellete, name = 'dellete'),
    path('error/', views.error, name = 'error'),
    # path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
]
 