# Using URLs in Flask with redirection
# exercise 4
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex4/Temperature Or http://localhost:5000/ex4/Light
# change the parameter value in the browser Url and refresh , NOte the URL redirection 
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#unique-urls-redirection-behavior


from flask import Flask, redirect, url_for      # extra imports
app = Flask(__name__) # Flask constructor

@app.route('/temperature/<value>')
def displayTemperature(value):
    return(' Temperature is {} deg C'.format(value))

@app.route('/lightlevel/<value>')
def displayLightLevel(value):
    return(' Light Level is {} lux'.format(value))


# route - bind function to app path with variable passed as function argument
@app.route('/ex4/<measurement>')	
def ex4(measurement): 
    if measurement == 'Temperature':                              
        return redirect(url_for('displayTemperature', value = 24))      # URL redirection (to function) with parameter value
    else:
        return redirect(url_for('displayLightLevel', value = 200))      # URL redirection (to function) with parameter value 

# run the app
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
