# Sessions
# exercise 10
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/login or http://localhost:5000/logout
from flask import Flask, session, request, redirect , url_for, render_template 
app = Flask(__name__) # Flask constructor

# Set the secret key to some random bytes. Keep this really secret!

app.secret_key = b'_6H39ax12hdv\a\yls]/'
#                  012345678901234567890

@app.route('/')
def index():
    if 'username' in session:                               # checks session for usename key 
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']      # sets up session from form input
        return redirect(url_for('index'))                   # go to index page if logged in
    return render_template("ex10.html")                      # render ex10.html if not yet logged in om templates folder in project
    '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug = True)                       # added debug = True -  can make changes save and app will restart
