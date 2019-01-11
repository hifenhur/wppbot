from orator import DatabaseManager, Model

from webwhatsapi import WhatsAPIDriver

driver = WhatsAPIDriver(username="hifenhur")
    
config = {
    'postgres': {
        'driver': 'postgres',
        'host': '35.247.235.153',
        'database': 'tbc_wpp',
        'user': 'hifenhur',
        'password': 'numero04',
    }
}
class Driver(Model):
    pass

db = DatabaseManager(config)
Model.set_connection_resolver(db)

