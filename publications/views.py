from django.shortcuts import render

def PublicationView(request):
	form_lables=request.session["authorized_form_lables"]
	return render(request,"publication/publication.html",{"authorized_form_lables":form_lables})				