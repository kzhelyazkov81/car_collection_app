from django.urls import path, include

from car_collection_app.web.views import index, catalogue, \
    profile_create, profile_details, profile_edit, profile_delete, car_create, car_details, car_edit, car_delete

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('create/', car_create, name='car create'),
        path('int<id>/details/', car_details, name='car details'),
        path('int<id>/edit/', car_edit, name='car edit'),
        path('int<id>/delete/', car_delete, name='car delete'),
    ])),
)
