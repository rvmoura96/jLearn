from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'quiz', views.QuizViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # path("quiz/<ID>", views.showQuiz, name="showQuiz"),
    # path("quiz/<ID>/submit", views.submitQuiz, name="submitQuiz"),
]
