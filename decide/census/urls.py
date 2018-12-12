from django.urls import path, include
from . import views

urlpatterns = [
    path('', CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', CensusDetail.as_view(), name='census_detail'),
]
