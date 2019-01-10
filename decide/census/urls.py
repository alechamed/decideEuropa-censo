from django.urls import path, include
<<<<<<< HEAD
from . import views


urlpatterns = [
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
=======
from .views import CensusCreate, CensusDetail

urlpatterns = [
    path('list/<int:voting_id>/', CensusCreate.list),
    path('<int:voting_id>/', CensusDetail.as_view()),
>>>>>>> EC1-FrontEnd
]
