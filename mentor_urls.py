from django.urls import path

from HR_App.mentor_views import IndexView, View_Trainee, View_Time_Table

urlpatterns =[
    path('',IndexView.as_view()),
    path('view_trainee',View_Trainee.as_view()),
    path('view_time_table',View_Time_Table.as_view())

]
def urls():
      return urlpatterns,'mentor', 'mentor'