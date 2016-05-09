from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import ListView,DetailView
from books.models import *
from books.forms import ContactForm

# Create your views here.
# 4 viewfuction
def search_form(request):
	return render_to_response('search_form.html')
# 5 viewfuction
def search(request):
	errors = []
	if 'q' in request.GET: #and request.GET['q']
		q = request.GET['q']
		if not q:
			errors.append('Enter a Search Term')
		elif len(q) > 20:
			errors.append('Enter at most 20 characters')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_book_results.html',{'books':books,'query':q})
	return render_to_response('search_form.html',{'errors':errors})	# handle empty timely return
	#message = 'You Search for %r.' % request.GET['q']
	#message = 'Your Submit is Empty!'
	#return HttpResponse(message)
# 6 viewfuction
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','zilanxingshuo@163.com'),
				['zilanxingshuo@163.com'],)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial={'subject':'I need your site.'})
	return render_to_response('contact_form.html',{'form':form})
# 9 viewfunction-class
class PublisherList(ListView):
	model = Publisher
	context_object_name = 'my_favorite_publishers'	#*****#
# 10 viewclass
class PublisherDetail(DetailView):
	def go_context_data(self,**kw):
		# Call the base implementation first to get a context
		context = super(PublisherDetail,self).get_context_data(**kw)
		# Add in a QuerySet of all the books
		context['book_list'] = Book.objects.all()  #*****#
		return context
# 11 viewclass
class BookList(ListView):
	queryset = Book.objects.order_by('-publication_date')
	context_object_name = 'book_list'  #*****#
# 12 viewclas
class AcmeBookList(ListView):
	context_object_name = 'book_list'
	queryset = Book.objects.filter(publisher__name = 'Acme Publishing')
	template_name = 'books/acme_list.html'	 #*****#
# 13 viewclass
class PublisherBookList(ListView):
	template_name = 'books/book_by_publiser.html'
	def get_queryset(self):
		self.publisher = get_object_or_404(Publisher,name = self.args[0])
		return Book.objects.filter(publisher = self.publisher)
	def go_context_data(self,**kw):
		# Call the base implementation first to get a context
		context = super(PublisherBookList,self).get_context_data(**kw)
		# Add in a QuerySet of all the books
		context['Publisher'] = self.publisher
		return context