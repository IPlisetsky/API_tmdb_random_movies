from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import random
import json
from flask import request
import time

app = Flask(__name__)
CORS(app)


def escolher_linha_aleatoria():

    generos_dic = {
        0: "",
        1: "Action",
        2: "Adventure",
        3: "Animation",
        4: "Comedy",
        5: "Crime",
        6: "Drama",
        7: "Fantas",
        8: "Horror",
        9: "Romance",
        10: "Science Fiction",
        11: "Thriller"
    }


    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    request_genero = request.args.get('generos', type=int)
    
    request_ano = request.args.get('ano-inicio', type=int)
    request_ano_fim = request.args.get('ano-fim', type=int)

    
    genero = generos_dic[request_genero]
    print(f"\n\n\nGENERO ESCOLHIDO: {genero}\n\n\n")
    print(f"\n\n\nANO: {request_ano}\n\n\n")
    print(f"\n\n\nANO: {request_ano_fim}\n\n\n")
    
    query = f"""SELECT * FROM moviesdatabase WHERE GENERO LIKE '%{genero}%' 
    AND ORIGEM LIKE '%US%'  
    AND ANO BETWEEN {request_ano} AND {request_ano_fim}
    """
    cursor.execute(query)

    #cursor.execute("SELECT * FROM moviesdatabase WHERE GENERO LIKE '%%'")
    rows = cursor.fetchall()
    ids = []
    for i in rows:
        id = i[1]
        ids.append(id)

    numero = random.choice(ids)
    cursor.execute("SELECT * FROM moviesdatabase WHERE ID = ?", (numero,))
    linha = cursor.fetchone()
    conn.close()

    if linha:
        try:
            return {
                "id": linha[1],
                "titulo": linha[0],
                "ano_lancamento": linha[7],
                "genero": linha[3].split(","),
                "link": linha[6], 
                "poster": linha[2] 
            }
        except Exception as e:
            print("ERRO NO GENERO", e)
    else:
        escolher_linha_aleatoria()
        return {"error": "Nenhum filme encontrado"}


@app.route('/gerar', methods=['GET'])
def gerar():
    return jsonify(escolher_linha_aleatoria())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
