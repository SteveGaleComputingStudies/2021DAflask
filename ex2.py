# Flask routing
# exercise 2
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex2 OR http://localhost:5000/
# ref - https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing


from flask import Flask	
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/ex2')	
def ex2():
	return 'Exercise 2'

@app.route('/')	
def ex2root():
	return 'Exercise 2 / Route'

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0')
