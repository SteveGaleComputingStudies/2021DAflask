# Using variables eg an ID for a database query
# exercise 3
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex3/21
# change the Id value in the browser Url and refresh
# ref - https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules


from flask import Flask	
app = Flask(__name__) # Flask constructor


# route - bind function to app path with variable passed as function argument
@app.route('/ex3/<id>')	
def ex3(id):                                    # note variable can be an int, float , default is string
	return 'Exercise 3 id is {}'.format(id)

# run the app
if __name__=='__main__':
    app.run()
