# Getting Started With Flask
# exercise 1
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/

from flask import Flask	
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/')	
def ex1():
	return 'Exercise 1 completed - Hello All'

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0')
