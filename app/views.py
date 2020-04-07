from rest_framework.views import APIView
from rest_framework.response import Response


class AgileManifestoValues(APIView):
    def get(self, request):
        return Response({'status': 'Ok'})


class AgileManifestoPrinciples(APIView):
    def get(self, request):
        return Response({'status': 'Ok'})
