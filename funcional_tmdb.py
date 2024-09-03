import requests
import random



#url = "https://api.themoviedb.org/3/discover/movie"

def movie_random():
    global movie_id
    movie_id = random.randint(1,9999)
    print(movie_id)
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        url2 = f"https://themoviedb.org/movie/{movie_id}"
        token = "TOKEN"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)
        print(response)

        if response.status_code == 200:
            data = response.json()
            print(data)
            movie = data.get('title')
            print("-" * 30)
            print(f"Title: {movie}")
            print(f"Overview: {data.get('overview')}")
            print(f"ID: {data.get('id')}")
            print(f"Link: {url2}")
            print("-" * 30)  # Separator for readability
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            movie_random()
    except Exception as e:
        print(f"ERRO: {e}")
movie_random()


