# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_remove_question(self):
        """
        If a question is removed, its choices ae removed too.

        """
        q = Question.objects.create(question_text="example question", pub_date=timezone.now())
        c = Choice.objects.create(choice_text="option1", question=q)
        c2 = Choice.objects.create(choice_text="option2", question=q)
        c3 = Choice.objects.create(choice_text="option3", question=q)

        Question.objects.filter(question_text__contains="question").delete()
        Choice.objects.filter().exists()

        assert not Choice.objects.filter().exists()
