


class Stats:
    
    self.messagehistory = []
    self.bTally = {
        'a':0,
        'b':0,
        'up':0,
        'down':0,
        'left':0,
        'right':0,
        'start':0,
        'select':0,
        'anarchy':0,
        'democracy':0,
        'start9':0
        }
    
    self.uTally = {}
    self.lastMessage = {}
    
    def tallyButton(username, button):
        #Tally button press
        self.bTally[button] += 1
        
        #if the username isn't in one of the dictionaries, make sure it's in both
        if not username in self.uTally.keys() or not username in self.lastMessage.keys():
            self.uTally[username] = 1
            self.lastMessage[username] = message
            
        #otherwise, if the message is the same as their last, increment the count 1
        elif self.lastMessage[username] is message:
            self.uTally[username] += 1
            
        #if it's a new message, reset the count
        else:
            self.uTally[username] = 1

    def tallyMessage(username, message):
        #Tally message
        pass

