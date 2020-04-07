from rest_framework import serializers
from snippets.models import Messages


class MessagesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    messages = serializers.TextField()
