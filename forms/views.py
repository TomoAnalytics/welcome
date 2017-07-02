import mongoengine
import json
from datetime import datetime
from forms.models import FormData
from forms.models import MetaViews
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def forms(request):
    metaviews_forms = MetaViews.forms
    current_user = request.user
    for obj in MetaViews.objects:
     print(obj.forms)
     formObj=obj["forms"]
     formlable=request.GET.get('formlable', '')
     print("formlable="+formlable+" formObj[\"formlable\"] ="+formObj["formlable"])
     #print(has_group(current_user,"peacegeek"))
     formField=""
     if formObj["formlable"]==formlable and formObj["active"]== "true":
       formField=formObj["fields"]
       break
    print("formField::"+json.dumps(formField))
    form_lables=request.session["authorized_form_lables"]
    return render(request,'forms/Form.html',{"authorized_form_lables":form_lables,"formFields":formField,"formHeader_h2":formObj["header_h2_description"],"formHeader_h4":formObj["header_h4_description"],"formDescription":formObj["description"]})

@login_required
def SaveForm(request):
	saved = False
	formdata = {}
	if request.method == "POST":
	#Get the posted form
		for obj in MetaViews.objects:
			print(obj.forms)
			formObj=obj["forms"]
			formData = FormData()		
			formData.formname=formObj["formname"]
			formData.formname=formObj["formtype"]
			for formField in formObj["fields"]:
				formdata[formField["name"]]=request.POST.get(formField["name"])
				print(formField["name"])
				print(request.POST.get(formField["name"]))
				#print(json.dumps(formField))
			formData.fdata=formdata
			formData.save()
			saved = True
			form_lables=request.session["authorized_form_lables"]
	return render(request, 'forms/saved.html', {"authorized_form_lables":form_lables,"saved":saved})	

def has_group(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False	
