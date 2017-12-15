from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
	print request.method
	return render(request, 'surveys/index.html')

def process(request):

	if request.method == 'POST':
		request.session['name']=request.POST['name']
		request.session['location']=request.POST['location']
		request.session['language']=request.POST['language']
		request.session['comment']=request.POST['comment']

	return redirect('/results')

		
# after click, redirect to og page
	
def results(request):
	return render(request, 'surveys/results.html')

def home(request):
	return redirect('/')
