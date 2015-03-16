from django.http import HttpResponse, Http404
from django.shortcuts import render
from books.models import Book
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView

# Create your views here.
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append("Enter a search term.")
		elif len(q) > 20:
			errors.append("Please enter at most 20 characters.")
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html', { 'books': books, 'query': q })
	return render(request, 'search_form.html', {'error': errors})

# generic views with TemplateView
def about_pages(request, page):
	try:
		return TemplateView(request, template="about/%s.html" %page)
	except TemplateDoesNotExist:
		raise Http404()
