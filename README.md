# 2021DAflask
Flask introductory exercises

c:\Python37> python -m pip install flask  

# ex1 - First Flask app

# ex2 - Routing

# ex3 - Using variables eg an ID for a database query

## accepted variable types
string - (default) text (without a slash)

int -  positive integers

float - positive floating point values

path - similar to string , allows slashes

uuid  - UUID strings

# ex4 - Using URLs with redirection

# ex5 - HTTP methods and request object

## http methods supported
GET	    This is used to send the data in an without encryption of the form to the server.  
HEAD	provides response body to the form  
POST	Sends the form data to server. Data received by POST method is not cached by server.  
PUT	    Replaces current representation of target resource with URL.  
DELETE	Deletes the target resource of a given URL  

# ex6 - Static files and templates

# ex7 - Jinja2 templating

# ex8 - Json api response

# ex9 - Json api request and response

# ex10  - sessions



# References

## http methods
GET	    This is used to send the data in an without encryption of the form to the server.  
HEAD	provides response body to the form  
POST	Sends the form data to server. Data received by POST method is not cached by server.  
PUT	    Replaces current representation of target resource with URL.  
DELETE	Deletes the target resource of a given URL  

## error codes
400 – For Bad Request  
401 – For Unauthenticated  
403 – For Forbidden request  
404 – For Not Found  
406 – For Not acceptable  
425 – For Unsupported Media  
429 – Too many Requests  
