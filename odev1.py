from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__isim__)
api = Api(app)

class nobel(Resource):
    def get(self):
       data = pd.read_csv('nobel.csv')
       data = data.to_dict('records')
       return { 'data' : data}, 200

    def post(self):
        isim = request.args['isim']
        tur = request.args['tur']
        yil = request.args['yil']

        data = pd.read_csv('nobel.csv')

        new_data = pd.DataFrame({
            'isim': [isim],
            'tur': [tur],
            'yil': [yil]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('nobel.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

    class isim(Resource):
        def get(self):
            data = pd.read_csv('nobel.csv', usecols=[0])
            data = data.to_dict('records')
            return {'data': data}, 200

    api.add_resource(isim, '/nobelisim')
    api.add_resource(nobel, '/nobel')

    if __isim__ == '__main__':
        app.run(host="0.0.0.0", port=6767)
