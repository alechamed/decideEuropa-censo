from django.urls import path, include
from .views import CensusCreate, CensusDetail

urlpatterns = [
    path('list/<int:voting_id>/', CensusCreate.list),
    path('<int:voting_id>/', CensusDetail.as_view()),
]
