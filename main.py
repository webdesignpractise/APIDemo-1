### import the packages
from flask import Flask, jsonify, request
# import requests, json
# instantiate the class
app = Flask(__name__)
# setting up routes for methods to be accessed via call requests
@app.route('/cal', methods=['POST'])
def gather():
    data = request.get_json() # fetch the payload and 
    output = None
    height = data['height']         # desearlize it and capture the data into identifiers
    #print(name)
    weight = data['weight']
    #print(age)
    #ra_no = data['random_number']
    #print(ra_no)
    output =weight/pow(height,2)
    #print(output)
    return(jsonify({"BMI": output}))

# @app.route('/details', methods=['GET'])
# def fetch():

#     details = [1,2,43]
#     return(jsonify({"output":details}))

if __name__ == '__main__':
    app.run(port=5000,debug=True)
