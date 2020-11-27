from django.urls import path

from rest_framework.routers import DefaultRouter

from user_center import views

router = DefaultRouter()
# router.register('', views.UserView.as_view())


urlpatterns = [
    path('source/', views.UserView.as_view()),
    path('test/', views.test_api),

    path('get_code/', views.get_code),
    path('login/', views.user_login),
    path('refresh_token/', views.refresh_token),
    path('register/', views.register)
]

urlpatterns += router.urls
