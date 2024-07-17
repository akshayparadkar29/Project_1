# Http Response() only returns string data
# render() is used to render html files
from django.shortcuts import render, HttpResponse, redirect
# from blogapp -> import models.py -> import Post class
from blogapp.models import Post
# Q class is used to specify multiple conditions for sql statements
from django.db.models import Q
# from blogapp -> import forms.py -> import StudentForm class
from blogapp.forms import StudentForm
# UserCreationForm is in-built class of django 
# AuthenticationForm is in-built class used to perform form authentication
from django.contrib.auth.forms import AuthenticationForm
from blogapp.forms import UserForm
# authenticate() is method used to authenticate details while login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
'''
# Procedural oriented approach -> function based
# These functions takes Http-Request & returns Http-Response
'''

# USER-DASHBOARD
def user_dashboard(request):
    # retrieving logged- user id from session
    # request.user.id will return the id of logged-in user from session
    userId = request.user.id
    # specifying condition based on which post are retrieved
    # q1 -> retrieve post's which are not deleted
    # q2 -> retrieve post's which belongs to the logged-in user
    q1 = Q(is_deleted = 0)
    q2 = Q(uid = userId)
    # retrieving list of records from database which are not deleted
    # rows are objects of model
    records = Post.objects.filter(q1 & q2)
    # print(records)
    # dictionary
    content = {}
    # passing list of records to dictionary 'data' key 
    content['data'] = records
    return render(request,'udashboard.html',content)

# CREATE POST
def create_post(request):
    # retrieving logged- user id from session
    # request.user.id will return the id of logged-in user from session
    userId = request.user.id
    print("Logged-in Use Id -> ",userId)

    if request.method=="POST":
        # POST request section
        # Retriving create_post form input values
        title = request.POST['ptitle']
        sdesc = request.POST['sdesc']
        det   = request.POST['det_desc']
        cat  = request.POST['cat']
        act   = request.POST['pactive']

        '''
        print("Title -> "+title)
        print("Small Desc. -> "+sdesc)
        print("Details -> "+det)
        print("Category -> "+cat)
        print("Is Active -> "+act)
        '''
        
        # objects -> is the object manager OR Object Relational Mapper
        # creating object of Post Model class
        # create() is the method of objects manager OR ORM
        # is_deleted column value will be 1 for new records
        # is_deleted = 0, means False -> record exists in database
        # is_deleted = 1, means True -> record deleted from database 
        # uid -> holds user id to track which post belong to which user
        records = Post.objects.create(title=title, small_description=sdesc, details=det, category=cat, active=act, is_deleted=0,uid=userId)
        # inserting the row in database using save() of objects manager OR ORM
        records.save()
        print(records)
        return redirect("user_dash")
    else:
        # GET request Section
        return render(request,"create_post.html")

# EDIT RECORD
def edit(request,rid):
    if request.method == "POST":
        # POST section
        # retreving edit form values
        utitle = request.POST['ptitle']
        usdesc = request.POST['sdesc']
        udetdesc = request.POST['det_desc']
        ucat = request.POST['cat']
        upactive = request.POST['pactive']

        # getting record based on id value
        records = Post.objects.filter(id=rid)
        # updating values of record
        records.update(title=utitle, small_description=usdesc, details=udetdesc, category=ucat, active=upactive)
        return redirect('user_dash')
    else:
        # GET section
        # getting record based on id value
        # records = Post.objects.get(id=rid)
        records = Post.objects.get(id=rid)
        content = {}
        content['data'] = records
        # edit form
        return render(request,"edit.html",content)

# DELETE RECORD
def delete(request,rid):
    # hard deleting record
    # records = Post.objects.get(id=rid) 
    # records.delete()
    
    # in order to update is_deleted column,
    # you have to use filter() &
    # then use update() to update is_deleted column value
    # soft-deleting record
    records = Post.objects.filter(id=rid)
    records.update(is_deleted=1)
    return redirect("user_dash")

# POST DEACTIVATION
def deactivate(request,rid):
    # getting post data based on post-id
    records = Post.objects.filter(id=rid)
    # updating post record for the above post-id
    records.update(active=0)
    return redirect('user_dash')

# POST ACTIVATION
def activate(request,rid):
    # getting post data based on post-id
    records = Post.objects.filter(id=rid)
    # updating post record for the above post-id
    records.update(active=1)
    return redirect('user_dash')

# FILTER BY CATEGORY
def categoryFilter(request,opt):
    # Q class is used to build complex sql queries 
    # using logical AND, OR, NOT conditions
    # filtering post based on category number
    q1 = Q(category = opt)
    # filtering non-deleted posts
    q2 = Q(is_deleted = 0)
    records = Post.objects.filter(q1 & q2)
    content = {}
    content['data'] = records
    return render(request,'udashboard.html',content)
    

# FILTER BY STATUS
def activeFilter(request,opt):
    # Q class is used to build complex sql queries 
    # using logical AND, OR, NOT conditions
    # filtering posts based on active status
    q1 = Q(active = opt)
    # filtering non-deleted posts
    q2 = Q(is_deleted = 0)
    # filtering posts based on above conditions
    records = Post.objects.filter(q1 & q2)
    content = {}
    content['data'] = records
    return render(request,'udashboard.html',content)

# HOME PAGE
def index(request):
    # retrieving logged- user id from session
    # request.user.id will return the id of logged-in user from session
    userId = request.user.id
    # print("USERID ->",userId)

    if userId is not None:
        # Q class is used to build complex sql queries 
        # using logical AND, OR, NOT conditions
        # filtering active posts
        q1 = Q(active = 1)
        # filtering non-deleted posts
        q2 = Q(is_deleted = 0)
        # filtering records for specific logged-in user
        q3 = Q(uid = userId)
        # filtering posts based on above conditions & in ascending order
        # records = Post.objects.filter(q1 & q2).order_by('date_time')
        # filtering posts based on above conditions & in descending order
        records = Post.objects.filter(q1 & q2 & q3).order_by('-date_time')
        # passing the records to the dictionary
        content = {}
        content['data'] = records
        content['data2'] = request.user
        # passing dictionary to index.html page
        return render(request,'index.html',content)
    else:
        # Q class is used to build complex sql queries 
        # using logical AND, OR, NOT conditions
        # filtering active posts
        q1 = Q(active = 1)
        # filtering non-deleted posts
        q2 = Q(is_deleted = 0)
        # filtering posts based on above conditions & in ascending order
        # records = Post.objects.filter(q1 & q2).order_by('date_time')
        # filtering posts based on above conditions & in descending order
        records = Post.objects.filter(q1 & q2).order_by('-date_time')
        # passing the records to the dictionary
        content = {}
        content['data'] = records
        # passing dictionary to index.html page
        return render(request,'index.html',content)

# USER REGISTER
def user_register(request):
    if request.method == 'POST':
        # when using UserCreationForm class we can pass request.POST in parenthesis
        # to retrieve form input values  
        '''form = UserCreationForm(request.POST)'''
        # UserForm contains extra fields first_name, last_name, email icluding above fields
        form = UserForm(request.POST)
        # print(form)

        # You need to follow the pre-defined validations of UserCreationForm class
        # Username -> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        # Password ->   Your password can’t be too similar to your other personal information.
                    #   Your password must contain at least 8 characters.
                    #   Your password can’t be a commonly used password.
                    #   Your password can’t be entirely numeric.
                    #   should not contain characters same as present in Username & Email
        # Conf.Password -> Enter the same password as before, for verification.

        # is_valid() makes sure above validations are full-filled by the user
        if form.is_valid():
            # since above form object have all the input fields we can directly save the object
            # inserting username & password in auth_user table
            form.save()
            return redirect('/login')
        else:
            return HttpResponse("Failed to Create User !")
    else:
        # UserCreationForm class provides 3 fields below:
        # Username, Password, Confirm Password, labels, fields, help text, errors
        # Label in the form is handled by label_tag
        # help-text in the form is handled by help_text
        # errors in the form is handled by errors
        # UserCreation form contains 3 rows -> Username, Password, Conf.password
        '''form = UserCreationForm()'''
        # UserForm contains extra fields first_name, last_name, email including above fields
        form = UserForm()
        content = {}
        # assigning above form to dictionary 
        content['data'] = form
        # passing above dictionary to djangoform.html file
        # using 'data' key we can access above form
        return render(request,'register.html',content)

# USER LOGIN
def user_login(request):
    if request.method == "POST":
        # AuthenticationForm takes two parameters request & form input data in form of key=value pair
        # AuthenticationForm will then check if given user cridentials exist in auth_user table or not
        form = AuthenticationForm(request=request, data=request.POST)
        # checking if form constraints are maintained
        if form.is_valid():
            # retreving form input values
            # cleaned_data['key_name] is used to retrieve form input values while using AuthenticationForm() 
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            
            # authenticate() takes two parameters username & password
            # username & password are the column names of auth_user table
            # authenticate() checks in auth_user table for the given username & password
            # if given username & password is found in auth_user table then authenticate() return the username
            u = authenticate(username=uname,password=upass)
            # print("USER -> ",u)

            # # if user exist in auth_user table 
            if u:
                # login() function starts session
                # login() function saves user_id in session
                login(request,u)
                return redirect('user_dash')
        # if form not valid
        else:
            # AuthenticationForm() returns two fields -> Username & Password
            form = AuthenticationForm()
            content = {}
            content['data'] = form
            # show error message if form is not valid
            content['errmsg'] = "Invalid Username OR Password!!"
            return render(request,'login.html',content)
    else:
        # AuthenticationForm() returns two fields -> Username & Password
        form = AuthenticationForm()
        content = {}
        # assigning above form to dictionary 
        content['data'] = form
        # passing above dictionary to djangoform.html file
        # using 'data' key we can access above form
        return render(request,'login.html',content)

# USER LOGOUT
def user_logout(request):
    # logout() function is used to destroy the session
    logout(request)
    return redirect('index_page')

# SET COOKIE (UNSECURE -> saved on browser)
def setcookies(request):
    # storing reponse object
    response = render(request,'setcookie.html')
    # Cookies are piece of information stored on users browser
    # Cookies are used for login systems
    # Cookies are set when server send back the response
    # Cookies are not secure as anyone can access cookies information from browser
    # Cookies are dictionary with 'key' = 'value' pair
    # setting cookies below 
    response.set_cookie('name','ITVEDANT')
    response.set_cookie('percentage',98.99)
    return response

# GET COOKIE
def getcookies(request):
    content = {}
    # request.COOKIES['name'] gets the value the key 'name' which is -> 'ITVEDANT'
    # request.COOKIES['percentage'] gets the value the key 'percentage' which is -> 98.99
    # cookies are reffered when user visits the website second time
    # along with the request cookies are sent to the server
    content['n'] = request.COOKIES['name']
    content['p'] = request.COOKIES['percentage']
    return render(request,'getcookie.html',content)

# SET SESSION (SECURE -> saved on server)
def setsession(request):
    # session are piece of information stored on server
    # session can be used to store sensitive information like passwords
    # since session are stored on server sensitive information remains safe
    # session is dictionary with ['key'] = 'value' pair 
    # 'request' object is used to set the session
    request.session['username'] = "ITVEDANT"
    request.session['password'] = "redhat123@"
    return render(request,'setsession.html')

# GET SESSION
def getsession(request):
    data = {}
    # retrieving sessions using request.session['session_key_name']
    # and passing session data to 'uname' & 'upass' key of dictionary names 'data'
    data['uname'] = request.session['username']
    data['upass'] = request.session['password']
    return render(request,'getsession.html',data)

# DEMO FORM
def djangoform(request):
    # form object below contains 3 input fields declared in StudentForm class in forms.py
    form = StudentForm()
    content = {}
    # assigning above form to dictionary 
    content['data'] = form
    # passing above dictionary to djangoform.html file
    # using 'data' key we can access above form
    return render(request,'djangoform.html',content)

# def contact(request): 
#     return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

# def post(request):
#     return render(request,'post.html')



    