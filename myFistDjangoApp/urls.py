"""
URL configuration for myFistDjangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#this file is the root URLconf(ig) file

#step 4: we import the include and path functions from django.urls and insert an include() in the urlpatterns variable (a list type).

from django.contrib import admin
from django.urls import include, path

#the urlpatters list links polls/ URL path to the polls.urls module that contains the index view function that sends the "Hello World" string http response ...

# and the admin/ URL path to the admin.site.urls module


urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

# The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

# We have now wired the index view into the root URLconf. To Verify it’s working type the following command ...\> py manage.py runserver

#Notice, the admin moduel import. It provides an automatically generated admin site that is accessible at localhost:8000/admin


#The next step (step 5) is to setup the database. We'll do so in myFistDjangoApp/settings.py that is a normal Python module with module-level variables representing Django settings.