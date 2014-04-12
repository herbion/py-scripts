import sys

def safe_call(method):
	done = False
	result = None
	while not done:
		try:
			result = method()
			done = True
		except Exception, e:
			print "Caught exeption sleeping for 3 secs", e
			sleep(3)
	return result

def clr_scr(f, size=50): 
	def pretty_print(message):
		sys.stdout.write("\r" + (" " * size) + "\r")
		return f(message)
	return pretty_print
@clr_scr
def printer(message): sys.stdout.write(message)
