'''
    File name: __init__.py
    Author: /u/robbychampagne, ThePyrotechnic
    Date created: 9/29/2018
    Date last modified: 9/29/2018
'''
from twisted.internet import task


class RobbysPlayerPlugin:
    ''' Player plugin for DayZ servers'''

    def __init__(self, instance):
        self.bec = instance

        # Create a Task that calls the function Send_PlayerCount each 15 min.
        self.PlayerCount_Task = task.LoopingCall(self.Send_PlayerCount)
        self.PlayerCount_Task.start(900, False)

    def get_players(self):
        return self.bec.Bec_playersconnected

    def Send_PlayerCount(self):
        '''Send a message to all players in game.'''
        players = self.get_players()
        if len(players) > 1:
            rcon_msg = 'Say -1 There are %i players online' % len(players)
        else:
            rcon_msg = 'Say -1 There is 1 player online'
        self.bec._Bec_queuelist.append(rcon_msg)


def start(x):
    RobbysPlayerPlugin(x)
