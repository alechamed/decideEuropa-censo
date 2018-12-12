from django.urls import path, include
from .views import CensusCreate, CensusDetail

urlpatterns = [
    path('', CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', CensusDetail.as_view(), name='census_detail'),
]
