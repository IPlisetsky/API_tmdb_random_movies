import requests
import streamlit as st
import random
import subprocess
import sqlite3
import os

api_key = ("")


dados = []
for id in range(35000,40000):
    try:
        url = f"https://api.themoviedb.org/3/movie/{id}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        params = {
            "with_original_language": "en"
        }
        os.system('cls')
        response = requests.get(url, headers=headers, params = params)
        if response.status_code == 200:
            data = response.json()
            id = data['id']
            #movie = data['original_title']
            #poster = data['poster_path']
            #genero = data['genres']
            #origem = data['origin_country']
            #id_imdb = data['imdb_id']
            ano = data['release_date']
            ano = ano[:4]
            #link = f"https://themoviedb.org/movie/{id}"
            print("="*30)
            #print(movie)
            print(id)
            #print(poster)
            #print(genero)
            #print(origem)
            #print(id_imdb)
            print(ano)
            print("="*30)

            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            try:
                cursor.execute("ALTER TABLE moviesdatabase ADD COLUMN ANO INTEGER")
            except:
                pass
            cursor.execute(f"""
            UPDATE moviesdatabase SET ANO = {ano} WHERE ID = {id}
            """)
            

            conn.commit()


            
            
            

        else:
            print(f"Error: API request failed with status code {response.status_code}")

    except Exception as e:
        print(f"ERRO: {e}")

