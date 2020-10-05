from rest_framework import serializers

from .models import local

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = local
        fields = ('user_id','lat','long','device_token','title','body')