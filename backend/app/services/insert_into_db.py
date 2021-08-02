from app.models.cnba_models import Transfers, db

from app.services.http import build_api_response
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError


from .txt_treatment import read_files_data

def insert_list_transfers():
    print(f'********* Iniciando a Insercao no DB ***********')

    transfers_list = read_files_data()
    db.create_all()
    db.session.commit()

    # {'trans_type': 3, 'date': '01/03/2019', 'value': 1920000, 'cpf': 84515254073, 'card': '6777****1313', 'hour': '17:27:12', 'store_owner': 'marcos pereira', 'store_name': 'mercado da avenida'}

    for transfer in transfers_list:
        print('****************************************', transfer)
        record = Transfers(
            trans_type= int(transfer['trans_type']), 
            date = transfer['date'], 
            value = int(transfer['value']), 
            cpf = int(transfer['cpf']), 
            card = transfer['card'], 
            hour = transfer['hour'], 
            store_owner = transfer['store_owner'], 
            store_name = transfer['store_name'])

        # try:
        db.session.add(record)
        #     return build_api_response(HTTPStatus.CREATED)
        # except IntegrityError:
        #     return build_api_response(HTTPStatus.BAD_REQUEST)
        db.session.commit()