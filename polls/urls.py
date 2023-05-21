#step 2 : We created this file (ie the polls.urls module) to serve as a URLconf(iguration) specific to the polls module that will call the index function and map it to a URL. this index view sends the "Hello World" string http response.

from django.urls import path

from . import views

#we define a url pattern for the index view function

urlpatterns = [
    path("", views.index, name="index"),
]

#step 3: The next step is to make the root URLconf(ig) file (myFirstDjangoApp/urls.py) point at the polls.urls module (polls/urls.py). To do so, in myFirstDjangoApp/urls.py, we'll import the include and path functions from django.urls and insert an include() in the urlpatterns list.

# The include() function allows referencing other URLconfs.