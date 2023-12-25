from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date.A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
# It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.



# Note:
# Wait a minute. <Question: Question object (1)> isn’t a helpful representation of this object.
#  Let’s fix that by editing the Question model (in the polls/models.py file) 
# and adding a __str__() method to both Question and Choice:
# That's why we're adding the shit of __str__ method for our model