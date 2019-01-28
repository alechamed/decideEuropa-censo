from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import (
        HTTP_201_CREATED as ST_201,
        HTTP_204_NO_CONTENT as ST_204,
        HTTP_400_BAD_REQUEST as ST_400,
        HTTP_401_UNAUTHORIZED as ST_401,
        HTTP_409_CONFLICT as ST_409
)

from base.perms import UserIsStaff
from .models import Census
from django.shortcuts import render


class CensusCreate(generics.ListCreateAPIView):
    permission_classes = (UserIsStaff,)

    def create(self, request, *args, **kwargs):
        voting_id = request.data.get('voting_id')
        voters = request.data.get('voters')
        try:
            for voter in voters:
                census = Census(voting_id=voting_id, voter_id=voter)
                census.save()
        except IntegrityError:
            return Response('Error try to create census', status=ST_409)
        return Response('Census created', status=ST_201)

    def list(self, request, *args, **kwargs):
        voting_id = request.GET.get('voting_id')
        voters = Census.objects.filter(voting_id=voting_id).values_list('voter_id', flat=True)
        return Response({'voters': voters})


class CensusDetail(generics.RetrieveDestroyAPIView):

    def destroy(self, request, voting_id, *args, **kwargs):
        voters = request.data.get('voters')
        census = Census.objects.filter(voting_id=voting_id, voter_id__in=voters)
        census.delete()
        return Response('Voters deleted from census', status=ST_204)

    def retrieve(self, request, voting_id, *args, **kwargs):
        voter = request.GET.get('voter_id')
        try:
            Census.objects.get(voting_id=voting_id, voter_id=voter)
        except ObjectDoesNotExist:
            return Response('Invalid voter', status=ST_401)
        return Response('Valid voter')


from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import (
        HTTP_201_CREATED as ST_201,
        HTTP_204_NO_CONTENT as ST_204,
        HTTP_400_BAD_REQUEST as ST_400,
        HTTP_401_UNAUTHORIZED as ST_401,
        HTTP_409_CONFLICT as ST_409
)

from rest_framework.permissions import AllowAny
# from base.perms import UserIsStaff
from .models import Census
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from voting.models import Voting

        
class CensusCreate(TemplateView):
    
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        voting_id = request.data.get('voting_id')
        voters = request.data.get('voters')
        try:
            for voter in voters:
                census = Census(voting_id=voting_id, voter_id=voter)
                census.save()
        except IntegrityError:
            return Response('Error try to create census', status=ST_409)
        return Response('Census created', status=ST_201)

    # def list(self, request, *args, **kwargs):
    def list(request, *args, **kwargs):
        template_name = "census/censusList.html"
        voting_id = request.GET.get('voting_id')
        # voters = Census.objects.filter(voting_id=voting_id).values_list('voter_id', flat=True)
        voters = Census.objects.all()
        users = User.objects.all()                
        return render(request, "census/censusList.html", {'users': users, 'voting':voting_id, 'voters':voters})
        # return Response({'voters':voters})                       


class CensusDetail(generics.RetrieveDestroyAPIView):

    def destroy(self, request, voting_id, *args, **kwargs):
        voters = request.data.get('voters')
        census = Census.objects.filter(voting_id=voting_id, voter_id__in=voters)
        census.delete()
        return Response('Voters deleted from census', status=ST_204)

    def retrieve(self, request, voting_id, *args, **kwargs):
        voter = request.GET.get('voter_id')
        try:
            Census.objects.get(voting_id=voting_id, voter_id=voter)
        except ObjectDoesNotExist:
            return Response('Invalid voter', status=ST_401)
        return Response('Valid voter')


class CensusFilter(TemplateView):
    
    def listUsers(request):
        users = User.objects.all()
        return render (request, 'censusFilter.html', {'users':users})
    
    def listNombre(request):
        users = User.objects.filter()
        return render (request, 'censusFilter2.html', {'users':users})
    
    def listActivos(request):
        users = User.objects.filter(is_active=True)
        noUsers = User.objects.filter(is_active=False)
        return render (request, 'censusFilter3.html', {'users': users, 'noUsers':noUsers})
    
    def listStaff(request):
        users = User.objects.filter(is_staff=True)
        noUsers = User.objects.filter(is_staff=False)
        return render (request, 'censusFilter4.html', {'users': users, 'noUsers':noUsers}) 

    def listSuperuser(request):
        users = User.objects.filter(is_superuser=True)
        noUsers = User.objects.filter(is_superuser=False)
        return render (request, 'censusFilter5.html', {'users': users, 'noUsers':noUsers})