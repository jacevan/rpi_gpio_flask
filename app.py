from flask import Flask, jsonify, request
import gpio

app = Flask(__name__)
app.debug = True

@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/gpio', methods = ['GET', 'POST'])
def led():
  if request.method == "GET":
    return jsonify(gpio.get_output())
  
  if request.method == "POST":
    # Get JSON data from p5.js
    client_data = request.json
    # Update the input file
    gpio.set_input(client_data)
    # Get updated output data
    pin_data = gpio.get_output()

    return jsonify(pin_data)
    

