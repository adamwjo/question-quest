from rest_framework import serializers

from questionnaire.models import Question
from questionnaire.models import Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'content')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('name', 'content', 'question')