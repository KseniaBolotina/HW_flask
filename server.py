import flask
from flask import request, jsonify
from models import Session, Ad
from sqlalchemy.exc import IntegrityError

app = flask.Flask('Ad')
class HttpError(Exception):
    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message

@app.errorhandler(HttpError)
def error_handler(err: HttpError):
    http_response = jsonify({'error': err.message})
    http_response.status_code = err.status_code
    return http_response

def get_ad_by_id(ad_id: int):
    ad = request.session.get(Ad, ad_id)
    if ad is None:
        raise HttpError(404, 'ad not found')
    return ad

def add_ad(ad: Ad):
    request.session.add(ad)
    try:
        request.session.commit()
    except IntegrityError:
        raise HttpError(409, 'ad already exist ')

@app.before_request
def before_request():
    session = Session()
    request.session = session
@app.after_request
def after_request(response: flask.Response):
    request.session.close()
    return response



@app.route('/ad/<int:ad_id>', methods=['GET'])
def get_ad(ad_id: int):
    ad = get_ad_by_id(ad_id)
    return jsonify(ad.dict)

@app.route('/ad/', methods=['POST'])
def post_ad():
    json_data = request.json
    ad = Ad(**json_data)
    add_ad(ad)
    return jsonify(ad.id_dict)

@app.route('/ad/<int:ad_id>', methods=['PATCH'])
def patch_ad(ad_id: int):
    json_data = request.json
    ad = get_ad_by_id(ad_id)
    for key, value in json_data.items():
        setattr(ad, key, value)
    add_ad(ad)
    return jsonify(ad.id_dict)

@app.route('/ad/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id: int):
    ad = get_ad_by_id(ad_id)
    request.session.delete(ad)
    request.session.commit()
    return jsonify({'status': 'deleted'})

app.run()
