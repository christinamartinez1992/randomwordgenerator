from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	response = {
		"string": get_random_string(length=14)
} 
# Create your views here.
# Get this number to increment 
# Make a condition if an incremnt exists 

	if 'coins' not in request.session:
		request.session ["coins"] = 0

	else: 
		request.session ['coins'] = request.session ['coins'] + 1


	return render(request,'random_word/page.html', response)



