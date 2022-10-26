from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('donos/new/', views.dono_create, name='new_dono'),
    path('donos/new/', views.NewDono.as_view(), name='new_dono'),
    path('donos', views.dono_index, name='index'),
    path('donos/<int:pk>/delete', views.DonoDelete.as_view(), name='dono_delete'),
    path('donos/<int:dono_id>/complete', views.dono_complete, name='dono_complete'),
    path('donos/<int:dono_id>/uncomplete', views.dono_uncomplete, name='dono_uncomplete'),
]