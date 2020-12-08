from flask_restful import Resource

class Features(Resource):

	def get(self, note_id):
		return '{"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[-7485586.996581525,-226235.48735737102],[-6305296.5676016435,-2244564.1766917016],[-8932993.786875354,-1147342.2853650213],[-8648270.63382734,78293.21631647227],[-7485586.996581525,-226235.48735737102]]]},"properties":null}]}', 200

	def put(self, note_id):
		pass

