from django.test.client import Client

def before_all(context):
	context.client = Client()
