import requests
from django.conf import settings
from .models import Reviews

class Functions():
	def get_anime():
		url = settings.API_URL + "top-airing"
		response = requests.get(url, params={"page": 1})
		data = response.json()
		
		return(data)

	def get_popular_anime():
		url = settings.API_URL + "popular"
		response = requests.get(url, params={"page": 1})
		data = response.json()
		
		return(data)

	def get_recent_anime():
		url = settings.API_URL + "recent-episodes"
		response = requests.get(url, params={"page": 1})
		data = response.json()
		
		return(data)

	def get_anime_details(animeId):
		url = settings.API_URL + "info/" + animeId
		response = requests.get(url)
		data = response.json()
		
		return(data)

	def get_anime_episode(episodeId, server=None):
		url = settings.API_URL + "watch/" + episodeId
		if server == None:
			response = requests.get(url)
		else:
			response = requests.get(url, params={"server": server})
		data = response.json()
		
		return(data)

	def get_search_results(query):
		url = settings.API_URL + query
		response = requests.get(url)
		data = response.json()
		
		return(data)

	def get_available_servers(episodeId):
		url = settings.API_URL + 'servers/' + episodeId
		response = requests.get(url)
		data = response.json()
		
		return(data)
	
	def get_hero_content():
		anime_ids = ['one-piece', 'naruto', 'kimetsu-no-yaiba']
		url = settings.API_URL + 'info/'

		response = []

		for i in range(len(anime_ids)):
			info_url = url + anime_ids[i]
			data = requests.get(info_url)
			response.append(data.json())

		return response
	
	def get_episode_comments(episode_id):
		reviews = Reviews.objects.filter(episode_id=episode_id).values()
		return reviews