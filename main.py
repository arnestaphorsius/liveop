from flask import request
from sqlalchemy.exc import SQLAlchemyError

from app import *  # @UnusedWildImport
from models import *  # @UnusedWildImport
from geoalchemy2.elements import WKTElement
from geoalchemy2 import func


@app.route('/api/objecten/<object_id>/', methods=['GET'])
def get_bag_object(object_id):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_ALCHEMY_URI_LOC']

    try:
        db_object = Object.query.filter_by(bag_id=str(object_id)).first()

    except SQLAlchemyError as exc:
        return sqlalchemy_error(exc)

    if db_object is None: return not_found(404)

    return pretty_print(db_object.serialize())


@app.route('/api/objecten', methods=['GET'])
def get_bag_object_by_adres():
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_ALCHEMY_URI_LOC']

    x_coord = request.args.get('x', None)
    y_coord = request.args.get('y', None)
    postcode = request.args.get('postcode', None)
    straat = request.args.get('straat', None)
    huisnummer = request.args.get('huisnummer', None)

    query = Object.query.order_by(Object.orienteren_check, Object.risicovol_type)

    if postcode:
        query = query.filter(Object.adres_postcode == postcode)

    if straat:
        query = query.filter(Object.adres_straatnaam == straat)

    if huisnummer:
        query = query.filter(Object.adres_huisnummer == huisnummer)

    if x_coord and y_coord:
        point = WKTElement('POINT({0} {1})'.format(x_coord, y_coord), srid=28992)

        query = query.filter(func.ST_DWithin(Object.geometry_center_geo, point, 200)) \
            .order_by(func.ST_Distance(Object.geometry_center_geo, point)) \

    try:
        db_objects = query.limit(20) \
            .all()

    except SQLAlchemyError as exc:
        return sqlalchemy_error(exc)

    if db_objects is None or len(db_objects) == 0:
        return not_found(404)
    elif len(db_objects) == 1:
        return pretty_print(db_objects[0].serialize())

    return jsonify({'objecten': Serializer.serialize_list(db_objects)})


if __name__ == '__main__':
    app.run(debug=True)
