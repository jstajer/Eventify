from django.shortcuts import render
from rest_framework import mixins, generics

import eventify
from api.serializers import EventSerializer, EventdetailSerializer
from viewer.models import Event


class Events(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Eventdetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventdetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)