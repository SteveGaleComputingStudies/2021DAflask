# Json api request and response
# exercise 9
# run the python file (VScode - Run Python File in Terminal) amd run ex9test.py in idle to POST json Data
# change the Id value in the browser Url and refresh
# ref - https://flask.palletsprojects.com/en/2.0.x/quickstart/#apis-with-json


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/addSensorData/<uuid>', methods=['GET', 'POST'])
def addSensorData(uuid):
    content = request.json
    # check uuid - if uuid in ....
    #contentStr='{ "IOTSensorLocation" : "13111111", "Measurement" : "Temperature", "Value": "21.6" }'
    print("{0} {1} {2} {3}".format(content['IOTSensorLocation'],content['Measurement'],content['Value'],uuid))
    #json_data_response['code'],json_data_response['message'],json_data_response['Measurement'],json_data_response['Setpoint'],json_data_response['Deadband']
    responseData = {'code':'200', 'message' :'OK', 'Measurement': 'Temperature', 'Setpoint' : 22 , 'Deadband' : 1.5}
    return jsonify(responseData)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
