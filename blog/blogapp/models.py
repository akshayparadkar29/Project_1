# django.db is module & models is also module
from django.db import models
from datetime import datetime

# `Model` is a class
# Post class is inheriting Model class
# Post class will become a table in database
class Post(models.Model):
    # below variables will become columns of Post table in database
    # CharField() & IntegerField() -> datatype 
    title = models.CharField(max_length=50)
    small_description = models.CharField(max_length=50)
    details = models.CharField(max_length=300)
    category = models.IntegerField()
    active = models.IntegerField(default=1)
    # we are adding these columns after creating the table
    # when we have existing rows & data in tables,
    # then we will have to provide a default value to both columns 
    is_deleted = models.IntegerField(default=0)
    # providing default value to below field
    date_time = models.DateTimeField(default=datetime.now)
    # this column will hold user id from auth_user table when a particular user creats a post
    uid = models.IntegerField(default=0)

    # this method is used to show one column in admin interface
    def __str__(self):
        return self.title

'''
Create database migration, will create a file inside migration folder included details to create above Post table
-> py manage.py makemigrations

Note :- if you are getting 'No Changes Detected error then follow below steps:
    1. check if you app is registered in INSTALLED_APPS[] or not in settings.py
    2. check in models.py file inside Class parenthesis its models.Model
    3. check if the migration file is already exist in blogapp/migration folder

Execute migration file
-> py manage.py migrate

Above command will create table in database 
'''    

'''
When you try to add new column to existing database table then you will have to provide a default value to the column
You will get below message & options :

It is impossible to add a non-nullable field 'is_deleted' to post without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py

 Select 1 & you will be asked to provide a default value, then provide the default value & press enter
 '''

'''
in admin panel when you add your models, its row names are in 
Model object (count of rows)
for example, in this case -> Post object (number of rows)

so if we want to delete/edit table rows from table we will have to open each row to decide which row to delete
its very time consuming process. We want the names to be displayed for each row
So in this case we will be displaying 'title' row's value as the name of the row in admin panel
for this we have to use __str__(self) in model.py file

__str__(self):
    return self.title

`self` paramerter points to the current instance of the Post class
'''