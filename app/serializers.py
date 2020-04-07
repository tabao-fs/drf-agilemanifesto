from rest_framework import serializers

from app.models import Messages, TextType


class MessagesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=256)
    text_type = serializers.ChoiceField(choices=TextType.choices)
    message = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Messages.objects.create(**validated_data)


class AgileManifestoSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    message = serializers.CharField(style={'base_template': 'textarea.html'})
