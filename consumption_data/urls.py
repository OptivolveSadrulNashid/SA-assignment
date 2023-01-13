from django.urls import path

from .views import EnergyViewSet

urlpatterns = [
    path('consumption_data', EnergyViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('consumption_data/<str:pk>', EnergyViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path('consumption_data/user_id/<str:user_id>', EnergyViewSet.as_view({
        'get': 'retrieve_by_user'
    }))
]
