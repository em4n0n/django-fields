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
    
#Field Types

#CharField: 
#This is the most used field type. It can hold string data of length specified by max_lenth parameter. For a longer string, use TextField.

#IntegerField - The field can store an integer between -2147483648 to 2147483647. 
# There are BigIntegerField, SmallIntegerField and AutoFieldtypes as well to store integers of varying lengths.

#FloatField: can store floating-point number. Variant DecimalField stores a number iwth fixed digits in the fractional part
class Student(Model):
    grade = models.DecimanField(
                        max_digits = 5,
                        decimal_places = 2)
    
#DateTimeField

#Stores the date and time as an object of Python's datetime.datetime class. The DateField stores datetime.date value.

#EmailField

#It’s actually a CharField with an in-built EmailValidator

#FileField

#This field is used to save the file uploaded by the user to a designated path specified by the upload_to parameter.

#ImageField 

#This is a variant of FileField, having the ability to validate if the uploaded file is an image.

#URLField

#A CharField having in-built validation for URL.

#ForeignKey 

#It is used to establisha one-to-many relationship between two models. 
# It requires two positional arguments - the model with which it is related, and the on_delete option to define the behavior of the delete operation.
#Suppose you have a Customer and Vehicle model with a one-to-many relationship. A customer can have more than one vehicle.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )
    
#The on_delete option specifies the behavior in case the associated object in the primary model is deleted. The values are:

#CASCADE: deletes the object containing the ForeignKey

#PROTECT: Prevent deletion of the referenced object

#RESTRICT: Prevent deletion of the referenced object by raising RestrictedError

class Artist(model.Models):
    name = models.CharField(max_length=10)
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCASE)
    
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
    
#Next, you can create a few instances of these models:

>>> artist1 = Artist.objects.create(name='Danny') 
>>> artist2 = Artist.objects.create(name='John') 
>>> album1 = Album.objects.create(artist=artist1) 
>>> album2 = Album.objects.create(artist=artist2) 
>>> song1 = Song.objects.create(artist=artist1, album=album1) 
>>> song_two = Song.objects.create(artist=artis1, album=album2)

#You can safely delete the artist1 instance. If you try to delete artist2, the RestrictedError is raised.

#OneToOneField: 
#This field in one of the models establishes a one-to-one relationship between the two models. 

#Although a ForeignKey field with unique=True setting, behaves similarly, the reverse side of the relationship will always return a single object.

#The following model definition demonstrates a one-to-one relationship between the college model and a principal model. 

#A college can have only one principal and one person can be a principal of only one college.

class college(Model):
    CollegeID = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website=models.URLField()
    
class Principal(models.Model):
    CollegeID = models.OneToOneField(
                College,
                on_delete=models.CASCADE
                )
    Qualifications = models.Charfield(max_length=50)
    email = models.EmailField(max_length=50)
    
    
    
#ManyToManyField: 

#This field helps in setting a many-to-many relationship between two models. 

#Here, multiple objects of one model can be associated with multiple objects of another model. 

#For example, in the case of Subject and Teacher models, a subject is taught by more than one teacher. 

#Similarly, a teacher can teach more than one subject. This is represented in the following model definitions:

class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    Qualification = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    
class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key = True)
    name = models.Charfield(max_length=30)
    credits = model.IntegerField()
    teacher = model.ManyToManyField(Teacher)