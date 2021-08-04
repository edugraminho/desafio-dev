from flask import Blueprint, request, flash, redirect, session, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import cross_origin
import os

from app.services.insert_into_db import insert_list_transfers
from app.services.http import build_api_response
from app.services.txt_treatment import allowed_file
from app.models.cnba_models import Transfers, TransfersSchema, db
from http import HTTPStatus

from config import DATA_PATH


bp = Blueprint('api', __name__)

transfers_schema = TransfersSchema(many=True)

from app.services.http import build_api_response
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError



@bp.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if 'file' not in request.files:
        flash('Sem arquivo')
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash('Sem arquivo selecionado')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(DATA_PATH, filename))

        insert_list_transfers()

    try:
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)

        
@bp.route('/list_all', methods=['GET'])
@cross_origin()
def list_all():
    transfers = Transfers.query.all()

    return {'data' : transfers_schema.dump(transfers)}, HTTPStatus.OK
