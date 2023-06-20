#A model in Django is like any normal Python class. The ORM layer maps this model to a database table in the Django project. 

# Each attribute of a model class represents a field in the table. 

#The Django ORM enables storing and retrieving data in tables, not by executing raw SQL queries, but by invoking the model methods. 

#A model class subclasses the django.models.Model class. A typical definition of a model class is done inside the app's models.py file.

from django.db import models
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
#When you migrate this model (you need to include your app in the INSTALLED_APPS setting), the myapp_person table will be created as would be done by the CREATE TABLE query:

CREATE TABLE Person (
    id  INTEGER  PRIMARY KEY,
    first_name VARCHAR (20),
    last_name VARCHAR (20)
)

#Note that the first_name and last_name are the class attributes corresponding to the fields in the table.

#Django automatically names the table as appname_modelname, which you can override by assigning the desired name to db_table parameter of the Meta class, to be declared inside the model class

class Student(CommonInfo):
    #...
    class Meta(CommonInfo.Meta): #inherit the Student class with Meta, and then assign a variable called db_table + name of the app, to add a custom name to the app
        db_table = 'student_info'
        
# Field Properties
#primary_key - a parameter, false by default. can be set to true if you want the mapped field to be used as the primary key
#integerfield - without a primary key, django created an  integer field to hold a unique auto-incrementing number
#default - you can specify any default in the form of a value or a function that will be called whena new object is created

class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, default='Mumbabi')
    
#unique - if set to true, each object has a unique value

tax_code = models.CharField(
                    max_lenth = 20
                    unique = True
                    )

#choice - if you want the user to have a drop-down menu, set this parameter to a list of two-item tuples

SEMSETER_CHOICES = (
    ("", "Civil"),
    ("2", "Electrical")
    ("3", "Mechanical")
    ("4", "CompSci")
)

#declaring a Student Model

class Student(models.Model):
    semester = models.CharField(
        max_length = 20,
        choices = SEMESTER_CHOICES,
        deafult = '1'
    )
    