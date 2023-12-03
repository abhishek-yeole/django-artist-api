from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user_data = response.data
            user = User.objects.get(username=user_data['username'])
            
            if not Artist.objects.filter(user=user).exists():
                Artist.objects.create(user=user, name=user.username)

        return response

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = []

    def get_queryset(self):
        work_type = self.request.query_params.get('work_type', '')
        artist_name = self.request.query_params.get('artist', '')
        
        if artist_name:
            return Work.objects.filter(artist_name=artist_name)
    
        if work_type:
            return Work.objects.filter(work_type=work_type)
        
        return Work.objects.all()

    def perform_create(self, serializer):
        serializer.save()