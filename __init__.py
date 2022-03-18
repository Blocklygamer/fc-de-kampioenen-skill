from mycroft import MycroftSkill, intent_file_handler


class FcDeKampioenen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kampioenen.de.fc.intent')
    def handle_kampioenen_de_fc(self, message):
        self.speak_dialog('kampioenen.de.fc')


def create_skill():
    return FcDeKampioenen()

