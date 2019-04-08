from flask import Blueprint, jsonify, request
import pandas as pd
import json
from models.model import db
from models.model import PostProcessing

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def apple_store():
    if request.method == 'POST':
        try:
            apple_store = pd.read_csv('files/AppleStore.csv')
        except Exception as ex:
            return f'Erro na leitura do AppleStore.csv - Erro {ex}', 400

        top_10_music = apple_store[apple_store['prime_genre'] == 'Music']\
            .sort_values('rating_count_tot', ascending=False).head(10)
        top_10_book = apple_store[apple_store['prime_genre'] == 'Book']\
            .sort_values('rating_count_tot', ascending=False).head(10)

        for index, row in pd.concat([top_10_book, top_10_music]).iterrows():
            post_processing = PostProcessing(track_name=row['track_name'],
                                             n_citacoes=row['rating_count_tot'],
                                             size_bytes=row['size_bytes'],
                                             price=row['price'],
                                             prime_genre=row['prime_genre'])

            db.session.add(post_processing)
        db.session.commit()
        return "Dados inseridos com sucesso", 201
    else:
        result = []
        query = db.session.query(PostProcessing).all()
        for idx, item in enumerate(query):
            result.append({
                "prime_genre": item.__dict__['prime_genre'],
                "track_name": item.__dict__['track_name'],
                "n_citacoes": item.__dict__['n_citacoes'],
                "size_bytes": item.__dict__['size_bytes'],
                "price": item.__dict__['price']

            })

        return jsonify(result), 200

