from django.urls import path
from .views import PersonViewSet

urlpatterns = [
    path('person/', PersonViewSet.as_view({'post': 'create'}), name='person-create'),
]
