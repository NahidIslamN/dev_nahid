from django.shortcuts import render, redirect
from django.views import View
from viewer.models import PublicMessage
from django.contrib import messages

# Create your views here.


class HomePage(View):
    def get(self, request):
        
        return render(request,"public/index.html")


class AboutMe(View):
    def get(self, requset):

        return render(requset,'public/about.html')
    


class MyResume(View):
    def get(self, requset):
        
        return render(requset,'public/resume.html')
    


class MyPortfolio(View):
    def get(self, requset):
        
        return render(requset,'public/portfolio.html')
    



class MyService(View):
    def get(self, requset):
        
        return render(requset,'public/service.html')
    


class MyContact(View):
    def get(self, requset):
        
        return render(requset,'public/contact.html')
    
    def post(self, request):
        data = request.POST
      
        public_message = PublicMessage.objects.create(
            name = data.get('name'),
            email = data.get('email'),
            subject = data.get('subject'),
            message = data.get('message'),
            
        )
        public_message.save()
        messages.info(request,'Successfully sent to Nahid Islam !')
    

       
        return redirect('/viewer/contacts/') 
    
