from urllib.parse import unquote

from flask import Flask, request, make_response, jsonify

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

INFO = {
    "languages": ["Python", "Java", "ruby"],
    "Tools": ["Pycharm", "Docker", "K8s"],
    "DB": ["MongoDb", "PostgreSql", "SQL"]
}


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route("/data/<connector>/<member>/")
def get_data(connector, member):
    if connector and connector in INFO:
        if member and member in INFO[connector]:
            print("Memeber  : ", INFO[connector])
            return make_response(jsonify({"res": INFO[connector]}), 200)

        return make_response(jsonify({"res": "Member not found"}), 400)

    return make_response(jsonify({"res": "Connector not found"}), 400)


@app.route("/data/<connector>", methods=["POST"])
def insert_data(connector):
    req = {}
    for data in request.get_data().decode("utf-8").split("&"):
        data = data.split("=")
        req[data[0]] = data[1]

    print("Request : ", request.get_data())
    if connector in INFO:
        return make_response(jsonify({"res": "Connector already exists!!!"}), 200)
    INFO.update({connector: req})
    return make_response(jsonify({"res": INFO}), 200)


@app.route("/data/<connector>", methods=["DELETE"])
def delete_info(connector):
    if connector not in INFO:
        return make_response(jsonify({"res": "Connector does not exists!!!"}), 200)
    del INFO[connector]
    return make_response(jsonify(INFO), 200)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
