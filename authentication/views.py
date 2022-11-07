from email import message
from django.shortcuts import render
from django.db import connection






# Create your views here.
from email.message import EmailMessage
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from gfg import  settings
from django.contrib.auth import get_user_model
from .models import history
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View,TemplateView, CreateView

from django.template import loader
#from .forms import TransactionForm

User = get_user_model()
from django.db import connections






from django.core.mail import send_mail,EmailMessage






# Create your views here.
def home(request):
    return render(request,"authentication/index.html")
def signup(request):
    
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        type = request.POST['type']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            return redirect('home')

        if User.objects.filter(email=email):

            messages.error(request,"email already exist")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")
        if pass1 != pass2:
            messages.error('Password did not match')
        if not username.isalnum():
            messages.error('username must be alpha-numric!')
            return redirect('home')
        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name =fname
        myuser.lastname =lname
        myuser.is_seller=True
        
    

        
    

        myuser.save()
        


        messages.success(request,"Your account is created" )
        
       
       
       
        return redirect("signin")


    
    
    
    return render(request,"authentication/signup.html")
def signin(request):
    


    if request.method =="POST":

        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username= username, password= pass1)
        if user is not None and user.is_seller:



            login(request,user)
            fname = user.first_name
            return redirect('seller')
        elif user is not None and user.is_customer:



            login(request,user)
            fname = user.first_name
            return redirect('customer')



        else:

            messages.error(request,"Bad credentials")
            return redirect('home')
   
   
   
   
   
    return render(request,"authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"logged out succesfullly")
    return redirect('home')

def profile(request):
    
    contex={
        'user':request.user

    }
    return render(request,"authentication/profile.html")
def signupc(request):
    
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        country=request.POST['country']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            return redirect('home')

        if User.objects.filter(email=email):

            messages.error(request,"email already exist")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")
        if pass1 != pass2:
            messages.error('Password did not match')
        if not username.isalnum():
            messages.error('username must be alpha-numric!')
            return redirect('home')
        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name =fname
        myuser.lastname =lname
        myuser.is_customer=True
    

        
    

        myuser.save()
        


        messages.success(request,"Your account is created" )
        
       
       
       
        return redirect("signin")


    
    
    
    return render(request,"authentication/signupc.html")
def seller(request):
    global amount1
    if request.method =="POST":
        amount = amount1.POST['amount2']

    
     
    
    return render(request,"authentication/seller.html")
def customer(request):
    return render(request,"authentication/customer.html")
def payment(request):
    

    

    val=1
    

    messages.success(request,'Transaction successfull')
               
    
    

     
    
   
     
    
    
    
    return render(request,"authentication/payment.html",{'val':val})
#def history1(request):
    
    history.objects.raw("INSERT VALUES(transaction_id1,transaction_status,transaction_update_time)" )

    History=history()
    History.transaction_id=transaction.id1
    History.status=transaction_status
    history.save(transaction_id,status,update_time)
    a=history.objects.all()
    
#class thistory(CreateView):
    template_name = "history.html"
    form_class = TransactionForm 
    success_url = reverse_lazy("authentication:history")

  #  def form_valid(self, form):
       # transaction_id = form.cleaned_data.get("transaction_id1")
       # status = form.cleaned_data.get("transaction_status")
       # update_time = form.cleaned_data.get("transaction_update_time")
       # history.objects.create(transaction_id=transaction_id,status=status,update_time=update_time)
        


       # user = User.objects.create_user(qid,status,update_time)
    
      #  history.save()
       # form.instance. = user
        
       # return super().form_valid(form)


def history(request):
    #if request.method =="POST":
     #   transaction_id = request.POST['transaction_id1']
      #  status = request.POST['transaction_status']
       # update_time = request.POST['transaction_update_time']
    #with connection.cursor() as cursor:


       
        
        
    # a=history.objects.raw("INSERT VALUES(transaction_id1,transaction_status,transaction_update_time)" )
   # with connections.cursor() as cursor:
    # cursor.execute("INSERT INTO history VALUES(transaction_id1,transaction_status,transaction_update_time)" )\
    History=history()
    if request.method=="POST":
        transaction_id=History.request.GET('details.id')
        transaction_status=History.request.GET('details.status')
        update_time=History.request.GET('details.update_time')





        
    

    History.save()
        


       
       
       
       
    return redirect("history")


    
    
    
      







 