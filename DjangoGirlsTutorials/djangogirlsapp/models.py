from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# This line declares a Python class named Post that inherits from models.Model, which is part of Django's Object-Relational Mapping (ORM) system. This class represents a data model for a blog post.
class Post(models.Model):
    # These lines define the fields of the Post model. Each field represents a different attribute of a blog post, such as the author, title, text content, creation date, and published date. For example, author is a foreign key field linking to the user model (settings.AUTH_USER_MODEL), title is a character field for the title of the post, and so on.
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True, null=True)

# Methods:

# def publish(self): is a method defined within the class. It sets the published_date of the instance to the current time and then saves the instance.

# self.published_date = timezone.now() sets the published_date field to the current date and time.
# self.save() saves the changes made to the instance in the database.
# def __str__(self): is a special method that returns a string representation of the object. In this case, it returns the title of the post.

# Explanation of __str__ method:

# This method is used to display a human-readable representation of the object when it is printed or displayed in the Django admin interface.
# In this case, return self.title means that when you print or refer to a Post object, it will display the title of the post.

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
