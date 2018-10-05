'''
    File name: __init__.py
    Author: /u/robbychampagne, ThePyrotechnic
    Date created: 9/29/2018
    Date last modified: 9/29/2018
'''
from twisted.internet import task

CONFIG = {
    'interval': 1,
    'message_singular': 'There is one player online',
    'base_message': 'There are {} players online'
}


class RobbysPlayerPlugin:
    def __init__(self, instance):
        self.bec = instance
        self.player_count_task = task.LoopingCall(self.send_player_count)
        self.player_count_task.start(CONFIG.get('interval') * 60, False)

    def get_players(self):
        return self.bec.Bec_playersconnected

    def send_player_count(self):
        player_count = len(self.get_players())
        if player_count == 0:
            return

        elif player_count == 1:
            message = CONFIG.get('message_singular')

        else:
            message = CONFIG.get('base_message').format(player_count)

        command_to_fire = 'say -1 {0}'.format(message)
        self.bec._Bec_queuelist.append(command_to_fire)


def start(instance):
    RobbysPlayerPlugin(instance)
