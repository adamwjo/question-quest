from django.urls import path

from .views import QuestionDetailView, QuestionListView, AnswerDetailView, AnswerListView

urlpatterns = [
    path('questions', QuestionListView.as_view()),
    path('answers', AnswerListView.as_view()),
    path('questions/<pk>', QuestionDetailView.as_view()),
    path('answers/<pk>', AnswerDetailView.as_view())
]


