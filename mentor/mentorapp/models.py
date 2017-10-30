from django.db import models

# Create your models here.


class TestModel(models.Model) :
    name = models.CharField(max_length=128)
    rank = models.IntegerField(default=0)

    def __str__(self) :
        return self.name


class Student(models.Model) :
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    confirmPassword = models.CharField(max_length=128)
    isAStudent = models.BooleanField()



    aboutYourself = models.TextField(max_length=500)
    #github = models.URLField()
    #website = models.URLField()
    #usersince = models.DateTimeField()



    def __str__(self) :
        return self.firstname



class Mentor(models.Model) :
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    confirmPassword = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    aboutYourself = models.TextField(max_length=500)
    github = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    #usersince = models.DateTimeField()

    def __str__(self) :
        return self.firstname
