from django.contrib import admin
# import your model first
from blogapp.models import Post

# Register your models here.

# registering Post model in admin panel
# this method is used to only display one column in admin interface
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','small_description','details','category','active','is_deleted']
    list_filter = ['category','active','is_deleted']

admin.site.register(Post,PostAdmin)

'''
admin will have full acces to all the rows from `Post` table
admin will be able to see all rows of `Post` table in admin interface
'''

'''
PostAdmin() is user-defined class
admin -> is a module
ModelAdmin -> is a Class
ModelAdmin class is used to do modifications in admin interface
list_display = [] -> is attribute of ModelAdmin class -> used to show table columns & data on admin interface
list_filter = [] -> is attribute of ModelAdmin class -> used to show filter options on admin interface
'''

'''
create super user -> py manage.py create superuser
super user will have access to all model data created by all users
'''

'''
auth_permission table contains all the permissions 
auth_user contains all the users (super-user / normal-user)
'''

'''
below are id's for specific permissions in auth_permission table

id = 25 -> Add Post
id = 26 -> Change Post
id = 27 -> Delete Post
id = 28 -> View Post
'''

'''
auth_user_user_permission table keeps track of which permission
is given to which user 
This table uses the id's of users & permission to track

for example: User with id = 1 is assigned permission to view post
then in this table it will add user_id -> 1 & permission_is -> 28 (View Post)
'''