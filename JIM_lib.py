import time
import json

class JIM:

    def __init__(self):
        self.dict = {'action': '', 'time': time.time()}

    def __repr__(self):
        return(json.dumps(self.dict).encode())

class ClientPresence(JIM):

    def __init__(self, status = 'online', username = 'guest'):
        self.dict = {'time': time.time()}
        self.dict['action'] = 'presence'
        self.dict['user'] = {'account_name': username, 'status': status}

class ServerProbe(JIM):

    def __init__(self):
        super().__init__(self)
        self.dict['action'] = 'probe'

class ClientMessage(JIM):

    def __init__(self, sender, destination, message, encoding = 'UTF-8'):
        super().__init__()
        self.dict['action'] = 'msg'
        self.dict['to'] = destination
        self.dict['from'] = sender
        self.dict['encoding'] = 'encoding'
        self.dict['message'] = message

class JoinChat(JIM):

    def __init__(self, room):
        super().__init__(self)
        self.dict['action'] = 'join'
        self.dict['room'] = '#{}'.format(room)

class LeftChat(JoinChat):

    def __init__(self, room):
        super().__init__(self, room)
        self.dict['action'] = 'leave'

class ChatMessage(ClientMessage):

    def __init__(self, sender, room, message, encoding = 'UTF-8'):
        super().__init__(self, encoding, sender, room, message)
        self.dict['to'] = '#{}'.format(room)

class ServerResponce(JIM):

    def __init__(self, code, message = ''):
        self.dict = {'time': time.time()}
        self.dict['responce'] = code
        self.dict['message'] = message