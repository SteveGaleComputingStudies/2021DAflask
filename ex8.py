# Json api response
# exercise 8
# run the python file (VScode - Run Python File in Terminal) amd open browser to http://localhost:5000/ex8/13112111
# change the Id value in the browser Url and refresh
# ref - https://flask.palletsprojects.com/en/2.0.x/quickstart/#apis-with-json


from flask import Flask	
app = Flask(__name__) # Flask constructor


# route - bind function to app path with variable passed as function argument
@app.route('/ex8/<location>')	
def ex8(location):                                    # note variable can be an int, float , default is string
    return {
        'IOTsensorlocation' : location,
        'Measurement' : 'Temperature',
        'Setpoint' : 23.4,
        'Deadband' : 1.2
    }


# run the app
if __name__=='__main__':
    app.run()
