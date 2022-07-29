from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
# semantic/src/models/predict.py
from src.models.predict import MostSimilarWord , MostSimilarVerse

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# This will enable CORS for all routes
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)

# routes to apis 
api.add_resource(MostSimilarWord, '/api/semantic/similar-word/<string:word>')
api.add_resource(MostSimilarVerse, '/api/semantic/similar-verse/<string:query>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
