from django.contrib import admin

# Register your models here.

from .models import Survey,SurveyAnswer,Choice,Question,QuestionAnswer


admin.site.register(Survey)
admin.site.register(SurveyAnswer)
admin.site.register(Choice)
admin.site.register(QuestionAnswer)
admin.site.register(Question)