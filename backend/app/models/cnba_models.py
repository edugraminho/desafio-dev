from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


class Transfers(db.Model):
    __tablename__ = 'transfers'
    id = db.Column(db.Integer, primary_key=True)
    trans_type= db.Column(db.String, nullable=False)
    date= db.Column(db.String, nullable=False)
    value= db.Column(db.BigInteger , nullable=False)
    cpf= db.Column(db.BigInteger, nullable=False)
    card= db.Column(db.String, nullable=False)
    hour= db.Column(db.String, nullable=False)
    store_owner= db.Column(db.String, nullable=False)
    store_name= db.Column(db.String, nullable=False)



class TransfersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Transfers
            
    id  = ma.auto_field()
    trans_type = ma.auto_field()
    date = ma.auto_field()
    value = ma.auto_field()
    cpf = ma.auto_field()
    card = ma.auto_field()
    hour = ma.auto_field()
    store_owner = ma.auto_field()
    store_name = ma.auto_field()
