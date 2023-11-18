import re
from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    color = serializers.CharField()

    def to_representation(self, instance):
        return {
            "uuid": instance.uuid,
            "name": instance.name,
            "color": instance.color
        }

    def validate_name(self, data):
        if Category.objects.filter(name=data).exists():
            raise serializers.ValidationError({
                "error": "There is already a category with this name."
            })
        return data

    def validate_color(self, data):
        pattern = re.compile(r'^#[0-9a-fA-F]{6}$')
        match = re.match(pattern, data)

        if bool(match) is False:
            raise serializers.ValidationError({
                "error": "The color is invalid."
            })
        return data

    def create(self, validated_data):
        return Category.objects.create(
            name=validated_data['name'],
            color=validated_data['color']
        )
