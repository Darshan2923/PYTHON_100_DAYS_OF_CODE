from django.db import models

# Create your models here.


class CreateBook(models.Model):
    bookname=models.CharField(max_length=200)
    bookprice=models.TextField()
    bookauthor=models.CharField(max_length=200)

    def __str__(self):
        return self.name
