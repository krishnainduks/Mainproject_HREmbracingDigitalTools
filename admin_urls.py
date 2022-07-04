
from django.urls import path

from HR_App import admin_views
from HR_App.admin_views import IndexView, Add_Trainee, Add_Mentor, View_Trainee, Remove_Trainee, View_Mentor, \
    Remove_Mentor, Time_Table, Add_Notification, Certificate, Genarate_Certificate, certificate_report, \
    Trainee_Certificate, Upload_Certificate, View_Certificate, Add_Weekend_Review, Chat

urlpatterns =[
    path('',IndexView.as_view()),
    path('add_trainee',Add_Trainee.as_view()),
    path('add_mentor',Add_Mentor.as_view()),
    path('view_trainee',View_Trainee.as_view()),
    path('remove_trainee',Remove_Trainee.as_view()),
    path('view_mentor',View_Mentor.as_view()),
    path('remove_mentor',Remove_Mentor.as_view()),
    path('time_table',Time_Table.as_view()),
    path('notification',Add_Notification.as_view()),
    path('certificate',Certificate.as_view()),
    path('generate_certificate',Genarate_Certificate.as_view()),
    path('certificate_report', certificate_report.as_view()),
    path('trainee_certificate',Trainee_Certificate.as_view()),
    path('upload_certificate',Upload_Certificate.as_view()),
    path('view_certificate',View_Certificate.as_view()),
    path('add_reviews',Add_Weekend_Review.as_view()),
    path('chat',Chat.as_view())




]
def urls():
      return urlpatterns,'admin', 'admin'