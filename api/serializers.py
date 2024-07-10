from rest_framework import serializers

from viewer.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        #fields = ['start_date', 'end_date', 'type', 'location', 'region',]
        fields = '__all__'


class EventdetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
