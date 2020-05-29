
from django.urls import path, include, re_path
from . import views

urlpatterns = [

    path(r'index/', views.index, name="root"),
    path(r'survey_load/', views.load_survey, name="load-survey"),
    re_path(r'survey_load/(?P<survey_id>\d+)/', views.survey_view, name="survey-detail"),
    path(r'admin_login/', views.admin_login, name="admin-login"),
    path(r'admin_panel/', views.admin_panel, name="admin-panel"),
    path(r'admin_panel/survey_delete/', views.survey_delete, name="admin-survey-delete"),
    path(r'admin_panel/survey/(?P(survey_id)\d+)/', views.admin_answers, name="answer-detail"),
    path(r'survey_fill/', views.survey_fill, name="fill-survey"),

    # path(r'^admin_panel/survey/(?P<survey_id>\d+)/$', views.admin_answers, name="answer-detail"),
    path(r'admin_panel/survey_create_view/', views.survey_create_view, name="admin-survey-create-view"),
    path(r'admin_panel/survey_create/', views.survey_create, name="admin-survey-create"),
    path(r'admin_panel/question_add_view/', views.question_add_view, name="admin-question-add-view"),
    path(r'admin_panel/question_add/', views.question_add, name="admin-question-add"),
    path(r'admin_panel/choice_add_view/', views.choice_add_view, name="admin-choice-add-view"),
    path(r'admin_panel/choice_add/', views.choice_add, name="admin-choice-add"),
    # path(r'^admin_panel/survey_delete/$', views.survey_delete, name="admin-survey-delete"),

]