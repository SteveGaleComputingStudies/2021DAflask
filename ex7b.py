# Jinja templates b
# exercise 7b
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex7b/Bill

from flask import Flask	, render_template       # added import
app = Flask(__name__) # Flask constructor


# route - bind function to app path
@app.route('/ex7b/<name>')	
def ex7b(name):
    templateData = {
        'title' : 'Execise 7 b',
        'user' : name
        }

    return render_template('ex7b.html' , **templateData)          # from templates folder in project, pass user variable to template

# run the app
if __name__=='__main__':
    app.run(debug = True)                       # added debug = True -  can make changes save and app will restart
