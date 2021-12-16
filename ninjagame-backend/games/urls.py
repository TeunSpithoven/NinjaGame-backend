from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateGameAPIView.as_view(), name='get_post_games'),
    path('<int:pk>/', views.UpdateAPIView.as_view(), name='update_game'),
]
