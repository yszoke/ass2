import sqlite3
from flask import Flask
from flask import jsonify
from flask import request
import mybackend

app = Flask(__name__)

"""need to change- its from the lesson"""
@app.route('/',methods=['GET'])
def view():
    startlocation = request.args.get('startlocation',type = str)
    timeduration = request.args.get('timeduration',type = int)
    k = request.args.get('k',type = int)
    if not startlocation or (type(timeduration)!=int and type(timeduration)!=float) or type(k)!=int:
        return "mistake"
    results = database.find_recommends(startlocation, timeduration, k)
    ##return results as json
    # for row in rows:
    #     print (row)
    # return jsonify(rows)
    return results


if __name__ == "__main__":
    database=mybackend.Database()
    app.run(host='127.0.0.1', port=5000)
