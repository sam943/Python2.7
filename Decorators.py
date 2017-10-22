"""
Decorators are used to change the basic behaviour of a class, function or method, without having to redefine those things

Decorators are mostly used in Django or flask Frameworks

Below is the use case withpout Decorators, to understand how to use Decorators

import time
import urllib2

def download_webpage():
	url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com'
	response = urllib2.urlopen(url,timeout = 60)
	return response.read()
def elapse_time():
	t0 = time.time()
	webpage = download_webpage()
	t1 = time.time()
	print "Elasped time %s\n" % (t1- t0)

elapse_time()

"""
import time
import urllib2

def elapsed_time(function_to_time):
	def wrapper():
		t0 = time.time()
		function_to_time()
		t1 = time.time()
		print "Elasped time %s\n" % (t1- t0)
	return wrapper
@elapsed_time # Decorator function that will be called and passed the subsequent functioas variable to decorator function
def download_webpage():
        url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com'
        response = urllib2.urlopen(url,timeout = 60)
        return response.read()
webpage = download_webpage()

@elapsed_time
def another_function():
	print "Doing something else"
	for i in range(1,100000):
		pass
another_fn = another_function()
