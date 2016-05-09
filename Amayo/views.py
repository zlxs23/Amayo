from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template import loader,RequestContext
import  MySQLdb
'''
from django.template import Context
from django.template.loader import get_template
'''
import datetime

# a view TO a PYfunction
# 1 viewfunction
def hello(request):	# view function
	return HttpResponse("Hello World!")

# 2 viewfunction
def CurrentTime(request):
	now = datetime.datetime.now()
	return render_to_response('current_time.html',{'current_time':now})	# {'current_time':now}->loacls() <built in python>
	'''
	t = get_template('current_time.html')
	html = t.render(Context({'current_time':now}))
	return HttpResponse(html)
	'''
# 3 viewfunction
def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	return render_to_response('next_time.html',{'next_time':dt,'hour_offset':offset})
# 3 viewfuction
def display_meta(request):
	values = request.META.items()
	values.sort()
	return render_to_response('display_meta.html',{'values':values})
# 4 viewfuction
# 5 viewfuction
# 7 viewfuction
def custom_proc(request):
	# A context Processor that provides 'app','user','ipadress'
	return {'app':'Amayo',
					'user':'Amayou',
					'ipaddress':request.META['REMOTE_ADD']}
# 8.1 viewfuction
def view_test_custom_1(request):
	return render_to_response('template1.html',{'message':'I am First.'},context_instance=RequestContext(request,processors=[custom_proc]))
# 8.2 viewfuctio
def view_test_custom_2(request):
	return render_to_response('template2.html',{'message':'You are Second.'},context_instance=RequestContext(request,processors=[custom_proc]))
