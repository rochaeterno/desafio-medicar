"""medicar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from medicar.views import UserViewSet, ConsultaViewSet, AgendaListAPIView, EspecialidadesListAPIView, MedicosListAPIView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('agendas/', AgendaListAPIView.as_view(), name='agenda-list'),
    path('especialidades/', EspecialidadesListAPIView.as_view(),
         name='especialidades-list'),
    path('medicos/', MedicosListAPIView.as_view(), name='medicos-list'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns +=router.urls
