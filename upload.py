# -*- coding: utf-8 -*-
import vk_api, os, common
from time import sleep

execfile('auth.py')

vk_photos = vk_api.VkUpload(vk)

def getAlbumId(vk):
   albums = vk.method('photos.getAlbums')
   print "Fetching albums"
   fmt = lambda a: { 'id': a['id'], 'title': a['title'].encode('utf-8'), 'size': a['size']}
   for a in reversed(sorted(filter(lambda a: a["size"] < 499, albums['items']))):
      print "{id} {size:4} {title}".format(**fmt(a))
   return int(raw_input("Enter album id: "))
def safe_call(method):
	done = False
	result = None
	while not done:
		try:
			result = method()
			done = True
		except Exception, e:
			print "Cought execption sleeping for 3 secs", e
			sleep(3)
	return result

default_path = r'C:\Users\herbion\Downloads\_'
pictures_path = raw_input('Enter path to folder or leave blank [%s]: ' % default_path) or default_path
aid = getAlbumId(vk)

if not pictures_path.endswith(os.path.sep): pictures_path += os.path.sep

pics = filter(lambda pic: any([pic.endswith(ext) for ext in ['jpg', 'jpeg', 'png']]), os.listdir(unicode(pictures_path)))

raw_input("Found %d pics. Go? " % len(pics))
total_pics = len(pics)

while len(pics) > 0:
	part = map(lambda x: os.path.join(pictures_path, x), pics[:5])
	safe_call(lambda:vk_photos.photo(part, album_id=aid))
	pics = pics[5:]
	# print str(len(pics)) + " left"
	common.printer('%{0:3} <> {1}/{2}'.format(int((total_pics - len(pics)) / float(total_pics) * 100), total_pics - len(pics), total_pics))
