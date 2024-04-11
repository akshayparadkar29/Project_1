# this is a user defined file

# Middleware is used to prevent attacks from hacker
# All request has to go through Middleware
# When form is initialized with GET request
# csrf token is saved on server in session
# then Middleware compares the csrf token which came along with form
# with the csrf token stored on server in session
# if both csrf token matches then user is allowed to submit the form

'''
        Request              Request
Client ---------> Middleware ----------> Views.py
       <---------           <---------- 
        Response             Response         
'''

# blog_middleware() is user-defined function
# register blog_middleware() in settings.py
# blog_middleware() is executed when you run the server
# get_Response() is pre-defined function which catch the response
def Blog_middleware(get_response):
    # blog_function() is user-defined function
    # blog_function(request) will be called for each request
    def blog_function(request):
        # Code to be executed before view is called
        response = get_response(request)
        # Code to be executed after view is called
        return response
    return blog_function