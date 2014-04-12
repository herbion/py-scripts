execfile('auth.py')

audios = vk.method("audio.get", {}).items()[1][1]
i = 0
while i < len(audios):
	a = audios[i]
	try:
		if not a['artist'].lower() == a['artist']:
			vk.method('audio.edit', { "owner_id":157373213, "audio_id": a["id"], "title": a["title"].lower(), "artist": a['artist'].lower() })
			sleep(1)
		i += 1
		print a
	except Exception, e: 
		print e
		print a
		sleep(5)