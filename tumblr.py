# -*- coding: utf-8 -*-
import pytumblr, os, common, sys
from time import sleep

def clr_scr(f, size=50): 
	def pretty_print(message):
		sys.stdout.write("\r" + (" " * size) + "\r")
		return f(message)
	return pretty_print
@clr_scr
def printer(message): sys.stdout.write(message)

blog = 'empartridge.tumblr.com'
limit = 20
offset = 0
processed_posts = 0
blog = raw_input('enter tumblr: ').split('/')[2]
print 'Ok so blog is? ', blog
client = pytumblr.TumblrRestClient('d2NlorP2LXPPCVIXixZFLVPcbsz9PcfW9aPjMO8NvKY8KN0FK1')
total_posts = client.posts(blog, limit=1, offset=0)['total_posts']
print "found posts:", total_posts
raw_input('Go?')

f = open(blog + '.txt', 'w')
print 
total_pics = 0
while processed_posts < total_posts:
	printer('%{0:3} <> {1}/{2}'.format(int(processed_posts / float(total_posts) * 100), offset, total_posts))
	response = common.safe_call(lambda: client.posts(blog, limit=limit, offset=offset))
	# if response['meta']['status'] == 200:
	# print offset, processed_posts

	for post in response['posts']:
		if post.has_key('photos'):
			photos = [photo['original_size']['url'] for photo in post['photos']]
			total_pics += len(photos)
			f.writelines("\n" + "\n".join(photos))
			f.flush()
		processed_posts += 1
	offset += limit
f.close()
print "\n Ok, done in ", blog + '.txt'
print ' Total pics:', total_pics
raw_input()
