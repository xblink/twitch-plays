import time

from config.config import config
from lib.irc import Irc
from lib.game import Game
from lib.cui import pbutton, pframe
from lib.gui import GUI
from lib.stats import Stats

class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)
        self.game = Game()
        self.stats = Stats()
        if self.config['features']['gui_stats']:
            self.GUI = GUI(self)

    def run(self):
        throttle_timers = {button:0 for button in config['throttled_buttons'].keys()}

        while True:
            new_messages = self.irc.recv_messages(1024)
            
            if not new_messages:
                continue
            
            for message in new_messages: 
                button = message['message'].lower()
                username = message['username'].lower()
                
                if not self.game.is_valid_button(button):
                    continue
                
                if button in self.config['throttled_buttons']:
                    if (time.time() - throttle_timers[button] <
                            self.config['throttled_buttons'][button]):
                        continue
                    throttle_timers[button] = time.time()
                    
                if not self.game.is_political(button):
                    if (self.config['features']['play_game'] and
                            not button in self.config['misc']['blocked_buttons']):
                        self.game.push_button(button)
                
                self.stats.tally_message(username, message['message'])
            
            if self.config['features']['stats_on']:
                if self.config['features']['gui_stats']:
                    self.GUI.run()
                if self.config['features']['console_stats']:
                    pframe(self.stats)
                    
            elif self.config['features']['buttonpresses_on']:
                pbutton(self.stats.message_buffer)