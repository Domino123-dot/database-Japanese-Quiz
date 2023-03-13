from rest_framework import serializers
from .models import questions

class questionsSerializer(serializers.ModelSerializer):

    class Meta:

        model = questions
        fields = ('pk' , 'category' , 'question' ,'is_active','good_answer')