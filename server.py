from flask import Flask, request
from flask_cors import CORS
import strawberry
from dataserver import Query, getCountries
import json

schema = strawberry.Schema(query=Query)

def server():
    app = Flask(__name__)
    CORS(app)
    @app.route("/", methods=['POST'])
    async def university():
        content = request.form.get('query')
        res = await schema.execute(content)
        return json.dumps(res.data)
    @app.route("/countries", methods=['POST'])
    async def countries():
        res = await getCountries()
        return json.dumps(res)
    return app
    