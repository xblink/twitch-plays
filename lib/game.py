
import time, win32api, win32con

class Game:

    keymap = {
        'up': 0x30,
        'down': 0x31,
        'left': 0x32,
        'right': 0x33,
        'a': 0x34,
        'b': 0x35,
        'start': 0x36,
        'select': 0x37,
        'democracy': None,
        'anarchy': None,
        'start9': None
    }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()
    
    def is_political(self, button):
        return button in ['anarchy','democracy','start9']

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(.15)
        win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)