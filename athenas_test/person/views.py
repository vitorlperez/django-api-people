# api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import PersonSerializer

class PersonViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Person added successfully"}, status=201)
        return Response(serializer.errors, status=400)
