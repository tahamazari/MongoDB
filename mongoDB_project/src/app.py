import pymongo

uri = "mongodb://127.0.0.1:27017"  #local server name and the port name
client = pymongo.MongoClient(uri)  #client instance, has access to database on machine. URI holds address of database
database = client['fullstack']  #name of database we are accessing
collections = database['students']  #name of collection 'students' within our database 'fullstack'

students = collections.find({})   #find values on our collection

for student in students:    #loop for printing information of students in database
    print(student)
