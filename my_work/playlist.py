platlist={
	'title':"spotify",
	'author':"shubham",
	'songs':[
		{'title':"song1","artist":"red, blue","time":2.13},
		{'title':"song2","artist":["green"],"time":4.20},
		{'title':"song3","artist":["purple"],"time":8.20},

		]
	}


for song in platlist['songs']:
	print(f"{song['title']}  {song['artist']}   {song['time']}")
	print(song['title'])