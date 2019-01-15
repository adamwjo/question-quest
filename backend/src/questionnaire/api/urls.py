from django.urls import path

from .views import QuestionDetailView, QuestionListView, AnswerDetailView, AnswerListView

urlpatterns = [
    path('', QuestionListView.as_view()),
    path('', AnswerListView.as_view()),
    path('<pk>', QuestionDetailView.as_view()),
    path('<pk>', AnswerDetailView.as_view())
]


