# step 6: Creating the models

from django.db import models

# Here, each model is represented by a class that subclasses django.db.models.Model. 
# In the case of the Question Model : django.db.models.Model.Question

# Each model has a number of class variables, each of which represents a database field in the model.
# Thus, the class variables of the Question class (or Model), 'question_text' and 'pub_date', represent database fields
# So each class variable is a field that is a represented by an instance of a Field class – e.g., CharField for character fields 


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    #the __str__ method adds convenience when dealing with the interactive prompt by giving an helpful description/representation of objects
    def __str__(self):
        return self.question_text


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # notice, the ForeignKey property indicates that each Choice is related to a single Question.
    # that foreignkey indicates that the Choice and Question classes have a relationship !
    # that relationship will allow the creation of a "choice_set" object in the Question class, so for every entry in Questions, there might be some Choice instances (rows of data in the Choice table). The general rule is a lowercase version of the model name, followed by "_set"
    # Our model is called Choice, so the set will be called "choice_set".

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


#The above code, although small, gives Django a lot of information. With it, Django is able to:
# 1. Create a database schema (CREATE TABLE statements) for this app.
# 2. Create a Python database-access API for accessing Question and Choice objects.
# 3. But first we need to tell our django project that the polls app is installed. We'll activate the models. That's going to be done in the "INSTALLED-APPS section of myFirstDjangoApp/settings.py (step 7)

# 💡 The Philosophy behind this :

# Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.