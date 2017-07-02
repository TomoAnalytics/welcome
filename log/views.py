#!python
#log/views.py
import mongoengine
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from forms.models import FormData
from forms.models import MetaViews
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

#@login_required(login_url="login/")
def home(request):
	current_user = request.user
	form_lables=[]
	form_names=[]
	if current_user.is_authenticated():
			metaviews_forms = MetaViews.forms
			for obj in MetaViews.objects:
				print(obj.forms)
				formObj=obj["forms"]
				if formObj["active"]== "true":
					frmObj=has_group(current_user,formObj)
					print(frmObj["formlable"])
					form_lables.append(frmObj["formlable"])
					form_names.append(frmObj["formname"])
	request.session["authorized_form_lables"]=form_lables				
	return render(request,"home.html",{"authorized_form_lables":form_lables,"authorized_form_names":form_names})					

def has_group(user, formObj ):
	form_groups_str=formObj["user_groups"]
	user_groups = user.groups.all().values_list('name', flat=True)
	#shared_items = set(groups.items()) & set(user_groups.items())
	form_groups=form_groups_str.split(",")
	user_forms=[]
	for form_group in form_groups:
		print(form_group)
		if user in User.objects.filter(groups__name=form_group):
			return formObj
def profile_view(request, id):
    u = UserProfile.objects.get(pk=id) 		