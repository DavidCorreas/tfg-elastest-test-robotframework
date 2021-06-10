import os

from flask import Flask
import robot.libdoc as ld
import json

app = Flask(__name__)

@app.route('/library_info/<library>')
def hello_world(library):
    ld.libdoc(f"{os.getcwd()}\\robotframework\\po\\{library}.py", "prueba.json", format="JSON", docformat="REST")
    with open('prueba.json') as json_file:
        return json.load(json_file)

@app.route('/get_libraries')
def get_libraries():
    libraries = [f.replace(".py", "") for f in os.listdir(".\\robotframework\\po") if os.path.isfile(os.path.join(f"{os.getcwd()}\\robotframework\\po", f))]
    return json.dumps(libraries)


app.run("0.0.0.0", "8181")



