# encoding=utf8
import os, sys, time, json, datetime
from orator import DatabaseManager, Model
from webwhatsapi import WhatsAPIDriver
from time import sleep



profiledir=os.path.join(".","firefox_cache")
pic_path=os.path.join(".","marketing.jpeg")
wppDriver = WhatsAPIDriver(username="devlabs", profile=profiledir)

print("Waiting for QR")
wppDriver.wait_for_login()

print("Bot started")
wppDriver.save_firefox_profile()
config = {
    'postgres': {
        'driver': 'postgres',
        'host': '35.247.235.153',
        'database': 'tbc_wpp',
        'user': 'hifenhur',
        'password': 'numero04',
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)



class Driver(Model):
	 __table__ = 'drivers'
	 pass
print("Buscando motoristas...")
contacts = wppDriver.get_contacts()
print(str(len(contacts)) + " Contatos")
drivers = Driver.where_raw('options_stage = 0').get()

phones_that_received = map(lambda x: x.phone, drivers)

new_contacts = [a for a in contacts if a.id not in phones_that_received]

print(str(len(new_contacts)) + "Novos contatos esperando mensagens")
print(datetime.datetime.now())


iteraction = 0
for driver in new_contacts:    
    print("iteração: "+ str(iteraction))
    iteraction += 1
     if iteraction == 1000:
         print("chegou nos mil")
         raise "error"
     try:
         db.table('drivers').insert(phone=driver.id, name=driver.name, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
     except:
         print("erro no usuário "+ driver.id)

    
print(datetime.datetime.now())
    