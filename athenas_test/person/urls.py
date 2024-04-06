from django.urls import path
from .views import PersonViewSet

urlpatterns = [
    path('', PersonViewSet.as_view({'post': 'create'}), name='person-create'),
    path('/list', PersonViewSet.as_view({'get': 'get_list'}), name='person-get-list'),
    path('/<uuid:person_id>', PersonViewSet.as_view({'put': 'update', 'delete': 'delete'}), name='person'),
]
