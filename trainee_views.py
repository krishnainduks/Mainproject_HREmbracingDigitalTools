from django.shortcuts import render
from django.views.generic import TemplateView, View

from HR_App.models import add_trainee, time_table, Notification, Certificate_Upload, Reviews, chat


class IndexView(TemplateView):
    template_name = 'trainee/trainee_index.html'

class View_Time_Table(TemplateView):
    template_name = 'trainee/view_time_table.html'
    def get_context_data(self, **kwargs):
        context = super(View_Time_Table,self).get_context_data(**kwargs)
        id = self.request.user.id
        print(id,'qqqqqqqqqqqq')
        men=add_trainee.objects.get(user_id=id)
        id1=men.mentorid_id
        print(id1,'eeeeeeeeeeee')
        print(id,'wwwwwwwwww')
        view_time_table = time_table.objects.filter(mentorid_id=id1)
        context['view_time_table']=view_time_table
        return context

class View_Vacancy(TemplateView):
    template_name = 'trainee/view_vacancy.html'
    def get_context_data(self, **kwargs):
        context = super(View_Vacancy,self).get_context_data(**kwargs)
        technology = Notification.objects.filter(status='addedd')
        context['technology']=technology
        return context

class Apply(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        noti = Notification.objects.get(pk=id)
        coun=noti.count
        s=int(coun)
        print(coun,'qqqqqqqqqqq')
        if s == 0:
            print('wwwwwwwww')
            return render(request,'trainee/trainee_index.html',{'messages':" vacancy filled"})
        else:
            print('xxxxxxxxx')
            noti = Notification.objects.get(pk=id)
            a=noti.number
            b=int(a)
            c=b-1
            noti.status='applyed'
            noti.count=c
            noti.save()

            return render(request,'trainee/trainee_index.html',{'messages':" Apply successfully"})

class View_Certificate(TemplateView):
    template_name = 'trainee/view_certificate.html'
    def get_context_data(self, **kwargs):
        id = self.request.user.id
        trai=add_trainee.objects.get(user_id=id)
        id1=trai.id
        context = super(View_Certificate,self).get_context_data(**kwargs)
        certificate = Certificate_Upload.objects.filter(trainer_id=id1)
        context['certificate']=certificate
        return context

class Weekend_Review(TemplateView):
    template_name = 'trainee/weekend_review.html'
    def get_context_data(self, **kwargs):
        context = super(Weekend_Review,self).get_context_data(**kwargs)
        id = self.request.user.id
        print(id,'qqqqqqqqqqqq')
        men=add_trainee.objects.get(user_id=id)
        id1=men.mentorid_id
        print(id1,'eeeeeeeeeeee')
        print(id,'wwwwwwwwww')
        view_reviews = Reviews.objects.filter(mentorid_id=id1)
        context['view_reviews']=view_reviews
        return context

class Send_Message(TemplateView):
    template_name = 'trainee/chat.html'
    def post(self , request,*args,**kwargs):
        message=request.POST['message']
        date=request.POST['date']
        id=self.request.user.id
        employee=add_trainee.objects.get(user_id=id)
        id2=employee.id
        chat_mess=chat()
        chat_mess.trainee_id=id2
        chat_mess.message=message
        chat_mess.date=date
        chat_mess.status='addedd'
        chat_mess.save()
        return render(request,'trainee/trainee_index.html',{'messages':"message send"})

class View_Reply(TemplateView):
    template_name = 'trainee/view_message.html'
    def get_context_data(self, **kwargs):
        id=self.request.user.id
        trainee=add_trainee.objects.get(user_id=id)
        id2=trainee.id
        context = super(View_Reply,self).get_context_data(**kwargs)
        view_message = chat.objects.filter(trainee_id=id2)
        context['view_message']=view_message
        return context


