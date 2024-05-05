from django.urls import path,include
from tasksapp.views import CreatePhotoView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'houses', HouseViewSet)
# router.register(r'house-images', HouseImageViewSet)
urlpatterns=[
    # path('create/',include(router.urls))
    path('create/',CreatePhotoView.as_view())
]