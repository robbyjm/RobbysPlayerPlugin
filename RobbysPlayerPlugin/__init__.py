'''
    File name: __init__.py
    Author: /u/robbychampagne, ThePyrotechnic
    Date created: 9/29/2018
    Date last modified: 9/29/2018
'''
from twisted.internet import task

CONFIG = {
	'interval': 15,
	'message_singular': 'There is 1 player online',
	'base_message': 'There are {} players online'
}


class RobbysPlayerPlugin:
    ''' Player plugin for DayZ servers'''

    def __init__(self, instance):
        self.bec = instance

        # Create a Task that calls the function Send_PlayerCount each 15 min.
        self.player_count_task = task.LoopingCall(self.send_player_count)
        self.player_count_task.start(CONFIG.get('interval')*60, False)

    def get_players(self):
        return self.bec.Bec_playersconnected

    def send_player_count(self):
        '''Send a message to all players in game.'''
        player_count = len(self.get_players())
        if player_count == 0:
        	return

        elif player_count == 1:
        	message = CONFIG.get('message_singular')

        else:
            message = CONFIG.get('base_message').format(len(player_count))

        command_to_fire = 'say -1 {}'.format(message)
        self.bec._Bec_queuelist.append(command_to_fire)

def start(x):
    RobbysPlayerPlugin(x)
