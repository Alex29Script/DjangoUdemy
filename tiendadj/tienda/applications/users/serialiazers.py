from rest_framework import serializers

class LoginGoogleSerializers(serializers.Serializer):
    token_id=serializers.CharField(required=True)