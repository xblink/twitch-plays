
import time
from config.config import config

debug = False                                       #You'll want this set to false.

class Stats:
    
    
    
    def __init__(self):
        self.messagehistory = []
        self.config = config
        self.message_buffer = [{'username': '', 'button': ''}] * self.config['misc']['chat_height']
        self.tally = {
            'a': 0, 'b': 0,                             #A/B totals
            'up': 0, 'down': 0, 'left': 0, 'right': 0,  #Direction Totals
            'start': 0, 'select': 0,                    #Start/Select Totals
            'anarchy': 0, 'democracy': 0, 'start9': 0,  #Total Votes
            'message': 0 }                              #Total Non-Commands
        
        self.voteTally = { 'a' :0, 'd': 0, 's': 0 }     #Vote counts for past 2k
        self.userTally = {}                             #Total messages by User           
        self.lastMessage = {}                           #Last message sent by User
        self.botSuspect = []                            #Suspected Bots
        self.voteBuffer = [0]*2000                      #Vote history
    
    def set_message_buffer(self, message):
        self.message_buffer.insert(self.config['misc']['chat_height'] - 1, message)
        self.message_buffer.pop(0)
        
    def tally_message(self, username, message):
        validButtons = self.tally.keys()
        validButtons.remove('message')
        voteButtons = ['anarchy', 'democracy', 'start9']
        button = message.lower()
        
        if button in validButtons:                                              #if not a button
            self.set_message_buffer({'username': username, 'button': button})
        else: self.tally['message'] += 1                                        #increment message tally
        if button in voteButtons:
            self.vote(button)
        self.tally_user(username, button)                                       #tally message with user
        
        
    def tally_user(self, username, message):
        if not username in self.userTally.keys():                       #check if not existing
            self.userTally.update({username: 1})                                #add to tally lists
            #print self.userTally.keys()
            self.reset_input_time(username, message)
        
        
        elif self.lastMessage[username][0] == message:                    #check for repeat
            self.userTally[username] += 1                               #increment repeat count
            self.update_input_time(username)
        else:
            self.userTally[username] = 1                                #reset tally count
            self.update_input_time(username)
            
            
            
    def update_input_time(self, username):
        currTime = time.time()
        prevTime = self.lastMessage[username][1]['currTime']
        if not prevTime == 0:
            timeDiff = time.time() - prevTime
        else:
            timeDiff = 0
        
        self.lastMessage[username][1]['currTime'] = currTime
        self.lastMessage[username][1]['prevTime'] = prevTime
        self.lastMessage[username][1]['timeDiff'] = timeDiff
        self.lastMessage[username][1]['totaledTime'] += timeDiff
        
#        meanTime = mean(self.lastMessage[username][1]['totaledTime'],
#                        self.userTally[username])

    def reset_input_time(self, username, message):
        self.lastMessage.update({username:  [message,{
                                            'currTime': time.time(),
                                            'prevTime': 0,
                                            'timeDiff': 0,
                                            'totaledTime': 0 }]})
    
    
    def vote(self, vote):
        self.tally[vote] += 1                                                   #Counts vote command
        
        oldVote = self.voteBuffer.pop()                                              #removes 2001th vote
        self.voteTally[vote[0]] += 1                                            #recalculates vote tallies
        if not oldVote is 0:
            self.voteTally[oldVote] -= 1
        
        self.voteBuffer = [vote[0]] + self.voteBuffer                           #adds to beginning of 2k list
    
    
    def mean(self, n, m):
        return float(n / m)
    
    
    
    
    
    
    
    
    
    
    
    