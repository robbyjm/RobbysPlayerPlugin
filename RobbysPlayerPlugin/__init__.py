'''
    File name: __init__.py
    Author: /u/robbychampagne
    Date created: 9/29/2018
    Date last modified: 9/29/2018
'''
from twisted.internet import task


class RobbysPlayerPlugin:
    ''' Player Plugin for DayZ Servers'''

    def __init__(self, instance):
        self.bec = instance

        # Create a Task that calls the function Send_PlayerCount each 15 min.
        self.PlayerCount_Task = task.LoopingCall(self.Send_PlayerCount)
        self.PlayerCount_Task.start(900, False)

    def get_players(self):
        return self.bec.Bec_playersconnected

    def Send_PlayerCount(self):
        '''Send a message to All Players In game.'''
        players = self.get_players()
        plural = len(players) > 1
        rcon_msg = f'Say -1 There {"are" if plural else "is"} {len(players)} player{"s" if plural else ""} online'
        self.bec._Bec_queuelist.append(rcon_msg)


def start(x):
    RobbysPlayerPlugin(x)
