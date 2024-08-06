from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Note
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

# Create your views here.
class Notes(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']
