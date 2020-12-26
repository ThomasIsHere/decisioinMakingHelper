import datetime
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase):

    def test_case_true_deadline_greater_or_eaqual_to_creation_date(self):
        """
        deadline date >= creation date should retrun True
        """
        question_to_test = Question(
            question_text = 'Question to test',
            creation_date = datetime.datetime(2020,11,10,11,30,5),
            deadline_date = datetime.datetime(2020,12,10,11,30,5)
            )
        self.assertIs(question_to_test.deadline_greater_or_eaqual_to_creation_date(), True)

    def test_case_false_deadline_greater_or_eaqual_to_creation_date(self):
        """
        deadline date >= creation date should retrun True
        """
        question_to_test =Question(
            question_text = 'Question to test',
            creation_date = datetime.datetime(2020,11,10,11,30,5),
            deadline_date = datetime.datetime(2020,10,10,11,30,5)
            )
        self.assertIs(question_to_test.deadline_greater_or_eaqual_to_creation_date(), False)
