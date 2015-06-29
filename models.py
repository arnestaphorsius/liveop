from sqlalchemy import inspect, BigInteger, Column, Integer, Text
from app import app, db

class Serializer(object):
    
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    
    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]        

class Object(db.Model, Serializer):
    
    __tablename__ = app.config['DB_BAA_TABLENAME']
    
    hub_object_id = Column(Integer)
    hub_object_bk = Column(BigInteger)
    hub_object_naam = Column(Text)
    object_functie = Column(Text)
    adres_bouwjaar = Column(Integer)
    adres_gemeentenaam = Column(Text)
    adres_huisletter = Column(Text)
    adres_huisnummer = Column(BigInteger)
    adres_huisnummertoevoeging = Column(Text)
    adres_postcode = Column(Text)
    adres_straatnaam = Column(Text)
    adres_woonplaats = Column(Text)
    risicovol_type = Column(Text)
    risicovol_soort = Column(Text)
    risicovol_categorie = Column(Text)
    risicovol_naam = Column(Text)
    alternatieve_toegang_geregeld = Column(Text)
    voldoende_opstelplaats_bij_ingang = Column(Text)
    alternatieve_toegang_omschrijving = Column(Text)
    aanwezigheid_sleutelkluis = Column(Text)
    aangewezigheid_correcte_sleutel = Column(Text)
    aanwezigheid_bluswater = Column(Text)
    aanwezigheid_voedingspunt_droge_blusleiding = Column(Text)
    bijzondere_gevaren = Column(Text)
    overige_gevaren = Column(Text)
    foto_per_gevaar = Column(Text)
    foto_neveningang = Column(Text)
    foto_brandweer_hoofdingang = Column(Text)
    zuurstof_opslag = Column(Text)
    bag_id = Column(Text, primary_key=True)
    orienteren_check = Column(Text)
    geometry_center_geo = Column(Text)
    geometry_rd_x = Column(Text)
    geometry_rd_y = Column(Text)
    #geometry_center_geo = Column(Geometry(geometry_type='POINT', srid=28992))
    
    def __repr__(self):
        return '<BAG id: %r>' + self.bag_id
