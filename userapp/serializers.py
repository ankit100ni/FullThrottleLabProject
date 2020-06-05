from rest_framework import serializers
from . models import ActivityPeriod, UserDF


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDF
        fields = ['id', 'activity_period', 'real_name', 'tz']
        depth=1


    def create(self, validated_data):
        validated_data['activity_period'] = ActivityPeriod.objects.create(**validated_data.get('activity_period', {}))
        player = UserDF.objects.create(**validated_data)
        return player