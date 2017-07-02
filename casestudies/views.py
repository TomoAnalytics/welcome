from django.shortcuts import render

def CasestudiesView(request):
	form_lables=request.session["authorized_form_lables"]
	return render(request,"casestudies/casestudies.html",{"authorized_form_lables":form_lables})				