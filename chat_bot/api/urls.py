from django.urls import path
from . import views


urlpatterns = {
    path('', views.view_post, name='view_post'),
}
