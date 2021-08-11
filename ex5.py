# HTTP Methods and request object
# exercise 5
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#http-methods
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#the-request-object
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/login 
from flask import Flask, session, request, redirect , url_for, render_template 
app = Flask(__name__) # Flask constructor

@app.route('/loggedin/<name>')
def loggedin(name):
    return 'You are logged in as {}'.format(name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName =  request.form['username']                                # gets the form key / value pair - gets the value for 'username'
        return redirect(url_for('loggedin', name = userName))               # loggedin page as name variable value  = username
    return render_template("ex5.html")                                      # render ex5.html if not yet logged in om templates folder in project
    '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


if __name__=='__main__':
    app.run(debug = True)                       # added debug = True -  can make changes save and app will restart
