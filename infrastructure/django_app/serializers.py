from rest_framework import serializers


class TaskSerializerDRF(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    completed = serializers.BooleanField(
        required=False, default=False
    )  # Hacer opcional
    created_at = serializers.DateTimeField(read_only=True)
