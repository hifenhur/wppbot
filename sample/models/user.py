from orator import DatabaseManager, Model
from webwhatsapi import WhatsAPIDriver

wppDriver = WhatsAPIDriver(username="hifenhur")

print("Waiting for QR")
wppDriver.wait_for_login()

print("Bot started")
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

drivers = Driver.all()

print("Buscando motoristas...")


for x in drivers:
	chat = wppDriver.get_chat_from_phone_number(str(x.phone), True)
	wppDriver.send_message_to_id(chat.id, "testando velocidade do envio")
    