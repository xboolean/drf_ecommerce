from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListCreateAPIView

class UUIDModelViewSet(ModelViewSet):
    lookup_field = 'uu_id'

class UUIDListCreateAPIView(ListCreateAPIView):
    lookup_field = 'uu_id'

class UUIDGenericViewSet(GenericViewSet):
    lookup_field = 'uu_id'