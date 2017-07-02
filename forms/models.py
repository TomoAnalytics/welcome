from django.db import models
from datetime import datetime
from mongoengine import *


class MetaViews(Document):
	forms = StringField(max_length=50000)
	datagrid = StringField(max_length=90000)
	changeIs = StringField(max_length=5000)
	viewcreated = DateTimeField(default=datetime.now)

class FormData(Document):
	formname = 	StringField(max_length=500)
	formtype = 	StringField(max_length=500)
	fdata  = DictField(max_length=25000)
	datacreated = DateTimeField(default=datetime.now)
	usercreated = StringField(max_length=50)

