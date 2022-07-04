from django.contrib.auth.models import User
from django.views.generic import TemplateView

from HR_App.models import add_trainee, add_mentor, time_table


class IndexView(TemplateView):
    template_name = 'mentor/mentor_index.html'

class View_Trainee(TemplateView):
    template_name = 'mentor/view_trainee.html'
    def get_context_data(self, **kwargs):
        context = super(View_Trainee,self).get_context_data(**kwargs)
        id = self.request.user.id
        men=add_mentor.objects.get(user_id=id)
        id1=men.id
        print(id1,'eeeeeeeeeeee')
        print(id,'wwwwwwwwww')
        trainee = add_trainee.objects.filter(user__last_name='1',mentorid_id=id1)
        context['trainee']=trainee
        return context

class View_Time_Table(TemplateView):
    template_name = 'mentor/view_time_table.html'
    def get_context_data(self, **kwargs):
        context = super(View_Time_Table,self).get_context_data(**kwargs)
        id = self.request.user.id
        men=add_mentor.objects.get(user_id=id)
        id1=men.id
        print(id1,'eeeeeeeeeeee')
        print(id,'wwwwwwwwww')
        view_time_table = time_table.objects.filter(mentorid_id=id1)
        context['view_time_table']=view_time_table
        return context
