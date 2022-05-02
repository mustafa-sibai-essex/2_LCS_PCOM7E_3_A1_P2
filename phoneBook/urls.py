from django.urls import path

from . import views

urlpatterns = [
    path('', views.phone_book, name='phone_book'),
    path('add', views.add_user, name='add'),
    path('userform', views.add_user_form_post, name='user_form_post'),
    path('sort/<str:attr>', views.sort_users, name='sort'),
    path('remove/<int:num>', views.remove_user, name='remove'),
    path('search', views.search_for_user, name='search'),
]
