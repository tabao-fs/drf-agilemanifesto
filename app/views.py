from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import Messages, TextType
from app.serializers import MessagesSerializer


class AgileManifestoValues(APIView):
    def get(self, request):
        messages = Messages.objects.filter(text_type=TextType.VALUES)
        serializer = MessagesSerializer(messages, many=True)
        return Response(serializer.data)


    def post(self, request):
        request.data['text_type'] = TextType.VALUES
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgileManifestoPrinciples(APIView):
    def get(self, request):
        messages = Messages.objects.filter(text_type=TextType.PRINCIPLES)
        serializer = MessagesSerializer(messages, many=True)
        return Response(serializer.data)


    def post(self, request):
        request.data['text_type'] = TextType.PRINCIPLES
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
