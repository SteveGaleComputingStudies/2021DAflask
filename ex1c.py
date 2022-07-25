# Getting Started With Flask
# exercise 1c
# ex1c - server running on port 80, accessible remotely - host='0.0.0.0', port=80, debug=True  
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/

from flask import Flask	
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/')	
def ex1():
	return 'Exercise 1c completed - Hello All from port 80'

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
