'''
    File name: __init__.py
    Author: /u/robbychampagne
    Date created: 9/29/2018
    Date last modified: 9/29/2018
'''
from twisted.internet import task


class RobbysPlayerPlugin(object):
    ''' Player Plugin for DayZ Servers'''

    def __init__(self, instance):
        self.bec = instance

        self.counter = 0

        ''' Create a Task that calls the function Send_PlayerCount each 15 min. '''
        self.PlayerCount_Task = task.LoopingCall(self.Send_PlayerCount)
        self.PlayerCount_Task.start(900, False)

    def get_players(self):
        return self.bec.Bec_playersconnected

    def Send_PlayerCount(self):
        '''This Function will send aMessage to All Players In game.'''
        x = len(self.get_players())
        if x==1:
            rcon_msg = "Say -1 There is " + str(x) + " player online"
            self.bec._Bec_queuelist.append(rcon_msg)
        else:
            rcon_msg = "Say -1 There are " + str(x) + " players online"
            self.bec._Bec_queuelist.append(rcon_msg)

        if self.counter < 100:
            self.counter += 1
        else:
            # enough Hello World, Stopping the task
            self.PlayerCount_Task.stop()


def start(x):
    RobbysPlayerPlugin(x)