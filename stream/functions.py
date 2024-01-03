import requests, json

class Functions():
	def get_anime():
		url = "http://localhost:3000/anime/gogoanime/top-airing"
		response = requests.get(url, params={"page": 1})
		data = response.json()
		 
		return(data)

	def get_popular_anime():
		url = "http://localhost:3000/anime/gogoanime/top-airing"
		response = requests.get(url, params={"page": 2})
		data = response.json()
		 
		return(data)

	def get_recent_anime():
		url = "http://localhost:3000/anime/gogoanime/recent-episodes"
		response = requests.get(url, params={"page": 1})
		data = response.json()
		 
		return(data)

	def get_anime_details(animeId):
		url = "http://localhost:3000/anime/gogoanime/info/" + animeId
		response = requests.get(url)
		data = response.json()
		 
		return(data)

	def get_anime_episode(episodeId, server=None):
		url = "http://localhost:3000/anime/gogoanime/watch/" + episodeId
		if server == None:
			response = requests.get(url)
		else:
			response = requests.get(url, params={"server": server})
		data = response.json()
		 
		return(data)

	def get_search_results(query):
		url = "http://localhost:3000/anime/gogoanime/" + query
		response = requests.get(url)
		data = response.json()
		 
		return(data)