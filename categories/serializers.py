from rest_framework import serializers


class CategorySerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {
            "uuid": instance.uuid,
            "name": instance.name
        }
