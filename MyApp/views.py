from django.shortcuts import render, redirect
from .models import MySkill,Service,Portfolio
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    skills = MySkill.objects.all()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    data = {
        'skills':skills,
        'services':services,
        'portfolios':portfolios,
        }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "Message from myPortfolio website"
        message_body = "Name: "+name+"\nEmail: "+email+"\nContact: "+phone+"\nMessage: "+message
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'sahudil418@gmail.com',
                [admin_email],
                fail_silently=False,
                )
        messages.success(request,'Thankyou...! your message sent succssfully')
        return redirect('/')
            
    return render(request,'base.html',data)


   

    
   