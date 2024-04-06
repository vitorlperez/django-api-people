# api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from uuid import UUID
from .service import PersonService
import logging

logger = logging.getLogger(__name__)


class PersonViewSet(viewsets.ViewSet):

    def create(self, request):
        try:
            person = PersonService.add_person(person_dto=request.data)
            if person:
                return Response(person.model_to_dict(), status=201)
            return Response(person.errors, status=400)
        except Exception as e:
            logger.error(e)
            raise 

    def get_list(self, request):
        try:
            persons = PersonService.get_list(username=request.GET.get('username'))
            return Response({'total': len(persons), 'data': [person.model_to_dict() for person in persons]}, status=200)
        except Exception as e:
            logger.error(e)
            raise
    
    def update(self, request, person_id: UUID):
        try:
            person = PersonService.update(person_id=person_id, person_dto=request.data)
            if person:
                return Response(person.model_to_dict(), status=200)
            return Response({'message': 'person id not found'}, status=204)
        except Exception as e:
            logger.error(e)
            raise
    
    def delete(self, request, person_id: UUID):
        try:
            person = PersonService.delete(person_id=person_id)
            if person:
                return Response(status=200)
            return Response({'message': 'person id not found'}, status=200)
        except Exception as e:
            logger.error(e)
            raise
