# Getting Started With Flask
# exercise 1
#ex1b - safe removal of control characters eg cross site scripting  
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/
# https://tedboy.github.io/flask/generated/flask.escape.html

from flask import Flask	, escape
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/')	
def ex1b():
	return escape('<html><script type = "text/javascript">alert("hacked")></script><body><H1>Ex 1A</H1></body></html>')           # safe removal of control characters eg cross site scripting

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0')
