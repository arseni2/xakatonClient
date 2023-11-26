from rest_framework import serializers
from .models import Document
from .models import AdditionalInfo
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ['id', 'document', 'info_text', 'created_at']