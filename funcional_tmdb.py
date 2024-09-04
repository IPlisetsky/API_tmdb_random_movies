import requests
import streamlit as st
import random
import subprocess

#def open_streamlit():
#    try:
#        comando = f"streamlit run a.py"
#        subprocess.Popen(comando, shell=True)
#        print("Aplicativo Streamlit iniciado com sucesso!")
#        executando = True
#    except subprocess.CalledProcessError as e:
#        print(f"Erro ao executar o comando: {e}")


def get_api_key():
    """Chave API"""
    while True:
        api_key = ("token")
        # Validação
        return api_key
        
def ui():    
    def card_movie(api_key):
        
        query = random.randint(1,9999)
        print(query)
        url = f"https://api.themoviedb.org/3/movie/{query}?language=pt-BR&with_genres=28"
        #url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres=28&primary_release_date.gte=2022-01-01&language=pt-BR&sort_by=popularity.desc"
        url2 = f"https://themoviedb.org/movie/{query}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        params = {
            "with_original_language": "en"
        }
        response = requests.get(url, headers=headers, params = params)
        print(response)

        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            card_movie(api_key)

        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            if response.status_code == 200:
                pass

            data = response.json()
            ano = data['release_date']
            ano = ano[:4]            
            st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
            st.markdown('', unsafe_allow_html=True)
            if data is not None:
                st.markdown(f'''
                <div class="card text-bg-dark mb-3" style="max-width: 18rem;">
                    <div class="card-body">
                        <img class="poster w-full" src="https://media.themoviedb.org/t/p/w300_and_h450_bestv2{data['poster_path']}", height = 300px, width = 200px>    
                        <h5 class="card-title">{data['original_title']} ({ano})</h5>
                        <h7 class"card-title">{data['origin_country']} {data['genres']} </h7>
                        <a href="{url2}" class="btn btn-primary">Ver Filme</a>
                    </div>
                </div>
                ''', unsafe_allow_html=True)
                #<p class="card-text">{data['overview']}</p> SINOPSE
                if st.button("Gerar"):
                    print("Clicou")
                    card_movie(api_key)

        except Exception as e:
            pass

    def main():
        """Prompts the user for API key, search query, and displays results."""
        api_key = get_api_key()

        card_movie(api_key)

    if __name__ == "__main__":
        main()

ui() 
