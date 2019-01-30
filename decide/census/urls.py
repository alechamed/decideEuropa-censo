from django.urls import path, include
from . import views
from .views import CensusCreate, CensusDetail, CensusFilter

urlpatterns = [
    path('list/<int:voting_id>/', CensusCreate.list),
    path('<int:voting_id>/', CensusDetail.as_view()),
    path('listUsers/', CensusFilter.listUsers),
    path('listActivo/', CensusFilter.listActivos),
    path('listStaff/', CensusFilter.listStaff),
    path('listSuperuser/', CensusFilter.listSuperuser)
#     path('', views.CensusCreate.as_view(), name='census_create'),
#     path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail')   
]
