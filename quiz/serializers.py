from rest_framework import serializers
from .models import questions
from .models import changelog


class questionsSerializer(serializers.ModelSerializer):

    class Meta:

        model = questions
        fields = ('pk', 'category', 'question', 'is_active',
                  'good_answer', "max_points_to_get")


class changelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = changelog
        fields = ('ID','title', 'info','timestamp' , 'isNew')

