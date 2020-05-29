from django.db import models

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=300)

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class Choice(models.Model):
    choice = models.CharField(max_length=900)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class SurveyAnswer(models.Model):
    orig_survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class QuestionAnswer(models.Model):
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    survey_answer = models.ForeignKey(SurveyAnswer, on_delete=models.CASCADE)