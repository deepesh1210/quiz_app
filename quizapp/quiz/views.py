from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question, Choice, QuizMap


# Create your views here.
class QuestionCreate(APIView):
    """
    Create questions and answers
    """
    @transaction.commit_manually
    def post(self, request, format='json'):
        """
        {
        'question': '',
        'choices': ['c1', 'c2', 'c3']
        'answer': 'c1'
        }
        """
        data = request.data
        question = data.get('question')
        choices = data.get('choices')
        answer = data.get('answer')
        if not question:
            return Response({'error':'Invalid question'}, status=status.HTTP_400_BAD_REQUEST)

        if not choices:
            return Response({'error': 'Invalid question'}, status=status.HTTP_400_BAD_REQUEST)

        if not answer:
            return Response({'error': 'Invalid question'}, status=status.HTTP_400_BAD_REQUEST)

        question_object = Question.objects.create(question=question)
        for choice in choices:
            question=question_object
            ch = Choice(choice=choice)
            ch.save()
        transaction.commit()

        answer_object = QuizMap(question=question_object, answer=answer)

        return Response({'success':"data saved succesfully"}, status=status.HTTP_200_OK)


