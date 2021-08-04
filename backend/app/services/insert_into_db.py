from app.models.cnba_models import Transfers, TransfersSchema, db

from app.services.http import build_api_response
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError


from .txt_treatment import read_files_data

def insert_list_transfers():
    print(f' Iniciando a Insercao no DB ')

    transfers_list = read_files_data()
    db.create_all()
    db.session.commit()


    for transfer in transfers_list:
        record = Transfers(
            trans_type= transfer['trans_type'],
            date = transfer['date'], 
            value = int(transfer['value']), 
            cpf = int(transfer['cpf']), 
            card = transfer['card'], 
            hour = transfer['hour'], 
            store_owner = transfer['store_owner'], 
            store_name = transfer['store_name'])

        db.session.add(record)

