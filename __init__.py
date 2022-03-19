from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking
import random
import os
from os.path import dirname,join

class FcDeKampioenen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        path = join(dirname(__file__),'quotes')
        self.playlist = []
        for roots, dirs, files in os.walk(path):
            for file in files:
                self.playlist.append(join(path,file))

    def initialize(self):
        self.audioservice = AudioService(self.bus)

    @intent_file_handler('kampioenen.de.fc.intent')
    def handle_kampioenen_de_fc(self, message):
        #self.speak_dialog('kampioenen.de.fc')
        quote = random.choice(self.playlist)
        self.audioservice.play(quote)


def create_skill():
    return FcDeKampioenen()

