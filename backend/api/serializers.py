from rest_framework import serializers
from backend.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"