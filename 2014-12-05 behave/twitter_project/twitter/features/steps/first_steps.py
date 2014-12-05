from behave import given, then, when

from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

@given(u'an anonimous user')
def impl(context):
    pass

@then(u'he has access to {page}')
def impl(context,page):
    response = context.client.get(page)
    assert response.status_code == 200	

@when(u'he is logged in')
def impl(context):
    status = context.client.login(username='user',
    							  password='user')
    assert status

@given(u'a new user')
def impl(context):
    u = User.objects.create_user(
    		username='user',
    		password='user',
    	)



