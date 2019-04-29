from flask import Flask, request, jsonify, Response
import json

# Declare an application on which we can create endpoints.
app = Flask(__name__)

# Local data structure cache for storing tables.
tables = {1: "blue table", 2: "kitchen table"}


@app.route("/", methods=["POST"])
def hello_world():
    return "Hello world!"


@app.route("/get_table_info_query", methods=["GET"])
def get_table_1():
    """
    Given table_id in query string, return corresponding table_name
    :return: string containing table name
    """

    table_id = request.args.get('table_query')

    print(table_id)

    return tables[int(table_id)]


@app.route("/get_table_info_request", methods=["GET"])
def get_table_2():
    """
    Given table_id in JSON request, return corresponding table_name
    :return: JSON response object containing table_name
    """

    req = request.json
    table_name = tables[req["table_id"]]

    print(table_name)

    return jsonify({"table_type": table_name})


@app.route("/add_new_table", methods=["POST"])
def add_table():
    """
    Add new table to our dict of tables.
    :return: (Response) a Response object containing a
        status code and accompanying message.
    """
    req = request.json
    table_name = req["table_name"]

    # Do this in server w/ UUIDs
    table_id = req["table_id"]

    tables[table_id] = table_name

    content = {"content": "TABLE IS ADDED SUCCESSFULLY"}

    print(tables)

    return Response(json.dumps(content), status=200)


# Run the Flask application as a server.
if __name__ == "__main__":
    app.run(port=5001)