from rest_framework.generics import ListAPIView, RetrieveAPIView
from questionnaire.models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionDetailView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerDetailView(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
