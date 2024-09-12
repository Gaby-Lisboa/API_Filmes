from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import FilmesListCreateView, FilmesDetailView





urlpatterns = [
    path('filmes', views.listar_filmes),
    path('listarfilmes', views.FilmesViews.as_view()),
    path('filme/<int:pk>', views.FilmesDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('genero/<int:pk>', views.GeneroViews.as_view()),
    path('filmes/', FilmesListCreateView.as_view(), name='filme-list'),
    path('filmes/<int:pk>/', FilmesDetailView.as_view(), name='filme-detail'
         )
]
