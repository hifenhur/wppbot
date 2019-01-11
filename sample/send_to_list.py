import os
import sys
import time

from webwhatsapi import WhatsAPIDriver

driver = WhatsAPIDriver(username="hifenhur")
for x in arr:
    chat = driver.get_chat_from_phone_number(x, True)
    driver.send_message_to_id(chat.id, "testando velocidade do envio")