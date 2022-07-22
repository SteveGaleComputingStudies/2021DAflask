# Flask routing api calls
# exercise 2b
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex2 OR http://localhost:5000/
# ref - https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing


from flask import Flask	
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/api/v1/hello')	
def helloV1():
	return 'hello from V1'

@app.route('/api/v1/bye')	
def byeV1():
	return 'Bye from V1'

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0')
