from django.db import models
from django.utils.timezone import datetime


class Question(models.Model):
    question_text = models.CharField(null=True, blank=True, max_length=200)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    deadline_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question_text

    def deadline_greater_or_eaqual_to_creation_date(self):
        """
        Returns True if deadline date >= creation date else False
        """
        if self.deadline_date >= self.creation_date:
            return True
        else:
            return False


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sign = models.BooleanField(default=None)
    weight = models.PositiveIntegerField(default=0)
    grade = models.PositiveIntegerField(default=0)
    answer_text = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.answer_text
