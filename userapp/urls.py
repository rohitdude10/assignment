
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('change-password/', views.ChangePasswordView.as_view(),
         name='change-password'),
]
