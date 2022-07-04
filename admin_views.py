
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import TemplateView, View
from django.core.mail import EmailMessage
from django.conf import settings


from HR_App.models import add_trainee, UserType, add_mentor, time_table, Notification, Certificate_Upload, Reviews
from xhtml2pdf import pisa
from django.template.loader import get_template

from django.http import HttpResponse
from io import StringIO



class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Add_Trainee(TemplateView):
    template_name = 'admin/add_trainee.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Trainee,self).get_context_data(**kwargs)
        mentor=add_mentor.objects.all()
        context['mentor'] =mentor
        return context
    def post(self, request,*args,**kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        mentor= request.POST['mentor']
        print(mentor,'wwwwwwwwwwwwwwwwwwwww')
        college=request.POST['college']
        designation = request.POST['designation']
        join_date = request.POST['join_date']
        image= request.FILES['image']
        F = FileSystemStorage()
        files = F.save(image.name, image)
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password,first_name=name,email=email,last_name=1)
        user.save()
        ment=add_mentor.objects.get(user_id=mentor)
        print(ment,'qqqqqqqqqqqqqqqqqqqqqqqq')
        trainee= add_trainee()
        trainee.user=user
        trainee.phone=phone
        trainee.mentorid_id=ment.id
        trainee.address=address
        trainee.college=college
        trainee.designation=designation
        trainee.join_date=join_date
        trainee.image=files
        trainee.status='addedd'
        trainee.status1='addedd'
        trainee.save()
        usertype = UserType()
        usertype.user = user
        usertype.type = "trainee"
        usertype.save()
        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})

class Add_Mentor(TemplateView):
    template_name = 'admin/add_mentor.html'
    def post(self, request,*args,**kwargs):
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        department = request.POST['department']
        image= request.FILES['image']
        F = FileSystemStorage()
        files = F.save(image.name, image)
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password,first_name=name,email=email,last_name=1)
        user.save()
        mentor= add_mentor()
        mentor.user=user
        mentor.phone=phone
        mentor.address=address
        mentor.department=department
        mentor.image=files
        mentor.status='addedd'
        mentor.save()
        usertype = UserType()
        usertype.user = user
        usertype.type = "mentor"
        usertype.save()
        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})

class View_Trainee(TemplateView):
    template_name = 'admin/view_trainee.html'
    def get_context_data(self, **kwargs):
        context = super(View_Trainee,self).get_context_data(**kwargs)
        trainee = add_trainee.objects.filter(user__last_name='1')
        context['trainee']=trainee
        return context

class Remove_Trainee(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class View_Mentor(TemplateView):
    template_name = 'admin/view_mentor.html'
    def get_context_data(self, **kwargs):
        context = super(View_Mentor,self).get_context_data(**kwargs)
        mentor = add_mentor.objects.filter(user__last_name='1')
        context['mentor']=mentor
        return context
class Remove_Mentor(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Time_Table(TemplateView):
    template_name = 'admin/time_table.html'
    def get_context_data(self, **kwargs):
        context = super(Time_Table,self).get_context_data(**kwargs)
        mentor=add_mentor.objects.all()
        context['mentor'] =mentor
        return context
    def post(self, request,*args,**kwargs):
        meeting_link = request.POST['meeting_link']
        date=request.POST['date']
        start_time=request.POST['start_time']
        end_time= request.POST['end_time']
        mentor=request.POST['mentor']
        ment=add_mentor.objects.get(id=mentor)
        time=time_table()
        time.meeting_link=meeting_link
        time.date=date
        time.start_time=start_time
        time.end_time=end_time
        time.mentorid_id=ment.id
        time.save()
        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})

class Add_Notification(TemplateView):
    template_name = 'admin/notification.html'
    def post(self, request,*args,**kwargs):
        technology=request.POST['technology']
        number=request.POST['number']
        description=request.POST['description']
        tech=Notification()
        tech.technology=technology
        tech.number=number
        tech.description=description
        tech.status='addedd'
        tech.count=number
        tech.save()
        noti = add_trainee.objects.all()
        for i in noti:
            email = EmailMessage(
            i.user.first_name,
            'Customer selected you to redesign their work.',
            settings.EMAIL_HOST_USER,
            [i.user.email],
            )
            email.fail_silently = False
            email.send()

        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})

class Genarate_Certificate(TemplateView):
    template_name = 'admin/generate_certificate.html'
    def get_context_data(self, **kwargs):
        context = super(Genarate_Certificate,self).get_context_data(**kwargs)
        certificate=add_trainee.objects.filter(status1='addedd')
        context['certificate'] =certificate
        return context


class Certificate(TemplateView):
    template_name = 'admin/certificate.html'
    def get_context_data(self, **kwargs):
        id1 = self.request.GET['id']
        print(id1)


        context = super(Certificate,self).get_context_data(**kwargs)

        gene = add_trainee.objects.get(id=id1)
        context['gene'] = gene
        return context

class certificate_report(View):
    def dispatch(self, request, *args, **kwargs):
        id1 = self.request.GET['id']
        gene = add_trainee.objects.get(id=id1)
        gene.status1='created'
        gene.save()
        template_path='admin/certificate_report.html'
        context={'gene':gene}
        response=HttpResponse(content_type='application/pdf')
        response['Content-Disposition']= 'filename="certificate_report.pdf"'
        template= get_template(template_path)
        html=template.render(context)
        pisa_status=  pisa.CreatePDF(
            html, dest=response
        )
        if pisa_status.err:
            return HttpResponse('we had some error <pre>' + html + '</pre>' )
        return response

class Trainee_Certificate(TemplateView):
    template_name = 'admin/trainee_certificate.html'
    def get_context_data(self, **kwargs):
        context = super(Trainee_Certificate,self).get_context_data(**kwargs)
        certificate=add_trainee.objects.filter(status1='created')
        context['certificate'] =certificate
        return context

class Upload_Certificate(TemplateView):
    template_name = 'admin/upload_certificate.html'
    def post(self, request,*args,**kwargs):
        id=self.request.GET['id']
        gene = add_trainee.objects.get(id=id)
        gene.status1='uploaded'
        gene.save()
        certificate= request.FILES['certificate']
        Fi = FileSystemStorage()
        filess = Fi.save(certificate.name, certificate)
        date=request.POST['date']
        uplo=Certificate_Upload()
        uplo.trainer_id=id
        uplo.certificate=filess
        uplo.date=date
        uplo.status='uploaded'
        uplo.save()
        messages = "Successfully Uploaded"
        return render(request,'admin/admin_index.html',{'messages':messages})

class View_Certificate(TemplateView):
    template_name = 'admin/view_certificate.html'


class Add_Weekend_Review(TemplateView):
    template_name ='admin/add_reviews.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Weekend_Review,self).get_context_data(**kwargs)
        mentor=add_mentor.objects.all()
        context['mentor'] =mentor
        return context
    def post(self, request,*args,**kwargs):
        meeting_link = request.POST['meeting_link']
        date=request.POST['date']
        start_time=request.POST['start_time']
        end_time= request.POST['end_time']
        mentor=request.POST['mentor']
        ment=add_mentor.objects.get(id=mentor)
        time=Reviews()
        time.meeting_link=meeting_link
        time.date=date
        time.start_time=start_time
        time.end_time=end_time
        time.mentorid_id=ment.id
        time.save()
        messages = "Successfully Added"
        return render(request,'admin/admin_index.html',{'messages':messages})

class Chat(TemplateView):
    template_name = 'admin/chat.html'



























