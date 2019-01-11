# encoding=utf8
import os, sys, time, json
from orator import DatabaseManager, Model
from webwhatsapi import WhatsAPIDriver


def run():
    profiledir=os.path.join(".","firefox_cache")
    pic_path=os.path.join(".","marketing.jpeg")
    driver = WhatsAPIDriver(username="devlabs", profile=profiledir)
    print("Waiting for QR")
    driver.wait_for_login()
    print("Bot started")

    driver.subscribe_new_messages(NewMessageObserver())
    print("Waiting for new messages...")

    """ Locks the main thread while the subscription in running """
    while True:
        time.sleep(60)


class NewMessageObserver:
    def on_message_received(self, new_messages):
        for message in new_messages:
            print(message)
            if message.type == 'chat':
                print("New message '{}' received from number {}".format(message.content, message.sender.id))
            else:
                print("New message of type '{}' received from number {}".format(message.type, message.sender.id))


if __name__ == '__main__':
    run()
