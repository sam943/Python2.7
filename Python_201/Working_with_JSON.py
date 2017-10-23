#Working_with_JSON
import json
import urllib

url =  "Downloading from someurl"
response = open("/root/Python2.7/Python_201/hotels.json","r")
json_string = response.read()
try :
	data = json.loads(str(json_string))
except:
	data = None
	print "Issue with JSON"
if ( data ):
	print "'%s' Street position  is %s" % (data['markers'][0]['name'], data['markers'][0]['position'])

	print "'%s' Street position  is %s" % (data['markers'][1]['name'], data['markers'][1]['location'])
	print "'%s' Street position  is %s" % (data['markers'][2]['name'], data['markers'][2]['location'])

# Creating JSON Structure
data = { 
	"course_name" : "python" ,
	"videos" : ["strings","classes","json"],
	"id" : 5
	}
json_string = json.dumps(data, indent =4)

# Write to a file 
file = open("/root/Python2.7/Python_201/course.json","w")
file.write(json_string)
file.close()
