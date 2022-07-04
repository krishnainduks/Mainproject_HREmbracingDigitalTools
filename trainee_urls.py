from django.urls import path

from HR_App.trainee_views import IndexView, View_Time_Table, View_Vacancy, Apply, View_Certificate, Weekend_Review, \
    Send_Message, View_Reply

urlpatterns =[
    path('',IndexView.as_view()),
    path('view_time_table',View_Time_Table.as_view()),
    path('view_vacancy',View_Vacancy.as_view()),
    path('apply',Apply.as_view()),
    path('view_certificate',View_Certificate.as_view()),
    path('view_review',Weekend_Review.as_view()),
    path('send_msg',Send_Message.as_view()),
    path('view_reply',View_Reply.as_view())

]
def urls():
      return urlpatterns,'trainee', 'trainee'