from Quiz.models import Quiz
from rest_framework import serializers


class QuizzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('category', 'user', 'description', 'title', 'photo',
                  'status')
