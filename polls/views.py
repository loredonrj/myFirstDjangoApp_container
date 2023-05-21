#step 1
# We create an index function (a view) that will return  an http response after receiving an http request
# To call this index view function, we need to map it to a URL - and for this we need a URLconf(iguration). 
# To create a URLconf we must create a file called urls.py in the the current polls directory (see step 2 in poll/urls.py).


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
