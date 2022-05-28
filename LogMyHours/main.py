
from Log.Logprogress import Log
from Service.LogService import Service
from Database.Database import Database

db1 = Database()

service1 = Service(db1)

log1 = Log(service1)

log1.run()
