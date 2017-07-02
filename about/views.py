from django.shortcuts import render

def AboutView(request):
	form_lables=request.session["authorized_form_lables"]
	return render(request,"about/about.html",{"authorized_form_lables":form_lables})					
