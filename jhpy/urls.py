from django.urls import path
from .views import base_views, question_views, answer_views, filedown_views, main_views, notice_views

app_name='jhpy'

urlpatterns = [
    # main_views.py
    path('',main_views.notice, name='index'),
    
    # base_views.py
    path('qna/',
         base_views.qna, name='qna'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),
    
    # notice_views.py
    path('notice/',
         notice_views.notice, name='notice'),
    path('notice/<int:notice_id>/',
         notice_views.notice_detail, name='notice_detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    
    # filedownload
    path('fdownload/',
         filedown_views.download, name='fdownload'),
]