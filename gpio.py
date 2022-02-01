import json

def get_output():
  with open("output", "r") as pin_file:
    return json.load(pin_file)

def set_input(input_data):
  with open("input", "w") as in_file:
      json.dump(input_data, in_file)