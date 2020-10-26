from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
# from twilio.rest.exceptions import TwilioRestException
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .sms import send_sms , get_otp
from .forms import CreateUserForm


random_otp = get_otp()
msg_body = f"""
welcome here 
submit your otp here : urvicode
YOUR OTP IS :{random_otp}
"""
account_sid = 'ACf87e9e6434e3a29b23a7e84f3312d5af'
auth_token = '2bdd02338e554863c6c02b9fd885e7a4'


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				u_phn = form.cleaned_data.get('phone')
				# user.set_password(user.password)

                # user.set_password(user.password)
				emailhere = form.cleaned_data.get('email')
				email = EmailMessage('login email ', 'hey there welcome ', to=[emailhere])
				email.send()
				send_sms(account_sid,auth_token,msg_body,'+12679154178','+918306308768')
				# if send_sms == True:
				#     return redirect('otp')
				
                
				# send_sms(account_sid,auth_token,msg_body,'+12679154178','+918306308768')
                
                
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')

	if request.method == 'POST':
		all_user = User.objects.all()
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if len(all_user) != 0:

			for user in all_user:
				if user.username == username:
					if user.password == password :
						data = {'username' : username,'password':password}
						return render(request,'dashboard.html',data)
			else:
				messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def otp(request):
    return render(request,'otp.html')


def home(request):
	return render(request, 'dashboard.html')
