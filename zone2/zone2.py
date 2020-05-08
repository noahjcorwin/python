#import os
#import subprocess
from flask import Flask
from flask_restful import Resource, Api
from mp import mplayer
from stations import callsigns

app = Flask(__name__)
api = Api(app)

class ZoneTwo(Resource):
    def get(self, station):
        stream = mplayer(station,callsigns[station])
        if station == 'stop':
            stream.stop()
            return {'stop': 'mplayer'}
        else:
            stream.play()
            return {station: callsigns[station]}

api.add_resource(ZoneTwo, '/zone2/<station>')

if __name__ == '__main__':
     app.run(host= '0.0.0.0',port=80)
