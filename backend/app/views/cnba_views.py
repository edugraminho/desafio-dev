from flask import Blueprint, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from http import HTTPStatus
# from sqlalchemy.exc import IntegrityError
from app.services.insert_into_db import insert_list_transfers
from app.services.http import build_api_response
from config import DATA_PATH, EXTENSIONS


bp = Blueprint('api', __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONS
           

@bp.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
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


            return build_api_response(HTTPStatus.OK)
        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@bp.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(DATA_PATH, name)


# if __name__ == '__main__':
#     app.run()