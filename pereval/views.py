from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PassUserViewset(viewsets.ModelViewSet):
    queryset = PassUser.objects.all()
    serializer_class = PassUserSerializer


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ('user__email',)


    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == "new":
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1, "message": "Перевал успешно изменен"})
            else:
                return Response({"state": 0, "message": serializer.errors})
        else:
            return Response({"state": 0, "message": f"Причина: {pereval.get_status_display()}"})