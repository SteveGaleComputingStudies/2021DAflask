# Static Files and templates
# exercise 6
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex6

from flask import Flask	, render_template       # added import
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/ex6')	
def ex6():
	return render_template("ex6.html")          # from templates folder in project

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)                       # added debug = True -  can make changes save and app will restart
