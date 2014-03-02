import time
from os import system

def pp(message, mtype='INFO'):
    mtype = mtype.upper()
    print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(channel, message, username):
    print '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, username.lower(), message)

def pbot(message, channel=''):
    if channel: 
        msg = '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, 'BOT', message)
    else: 
        msg = '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), 'BOT', message)

    print msg

def pbutton(message_buffer):
    system('cls')
    print '\n\n'
    print '\n'.join(['     {0:<12s}   {1:>9s}'.format(message['username'][:12].title(), message['button'].lower()) for message in message_buffer])
    
def pframe(stats):
    system('cls')
    print '\n\n'
    frame = []
    
    for message in stats.message_buffer:
        if not message['username'] is '':
            seconds = '{0:>3}s'.format(int(stats.lastMessage[message['username'].lower()][1]['timeDiff']))
            multFactor = 'x{0:<3}'.format(stats.userTally[message['username'].lower()])
        else:
            seconds = ''
            multFactor = ''
        name = message['username'][:12].title()
        button = message['button'].lower()
        
        frame.append(' {0:>4s} {1:<12s}   {2:>9s} {3:<4}'.format(seconds, name, button, multFactor))
        
    print '\n'.join(frame)