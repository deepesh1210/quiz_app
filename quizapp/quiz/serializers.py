from django.contrib.auth.models import User
from rest_framework import serializers

from quiz.models import Question, Choice, QuizMap

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice')