# Rendering HTML from a template
# exercise 5
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#http-methods
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#the-request-object
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/login 
from flask import Flask, request, redirect , url_for, render_template 
app = Flask(__name__) # Flask constructor

@app.route('/login', methods=['GET', 'POST'])
def login():
           # 
    return render_template("ex5.html")                                      # procees HTTP GET - render ex5.html if not yet logged in om templates folder in project
    '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)                       # added debug = True -  can make changes save and app will restart
