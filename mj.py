import json
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.crop
record = db.afterforKD


page = open("C:\\Users\\Admin\\Desktop\\pl\\project20190420\\after_Integrate_forKLine.json", 'r')
parsed = json.loads(page.read())
	
for item in parsed:
	record.insert(item)