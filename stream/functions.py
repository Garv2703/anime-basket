import requests, json
from django.conf import settings

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