import telepot
import time
import types

class Telegame(telepot.Bot):
    private_command_func = dict()
    group_command_func = dict()

    def _init_(self, token):
        super().__init__(token)

    def private_command(self, command):
        if not isinstance(command, str):
            def decoratorloop(func):
                for c in command:
                    self.private_command_func[c] = func
            return decoratorloop
        def decorator(func):
            self.private_command_func[command] = func
        return decorator

    def group_command(self, command):
        def decorator(func):
            self.group_command_func[command] = func
        return decorator

    def __handle(self, msg):
        if 'text' in msg.keys() and msg['text'][0] == '/':
            command = msg['text']
            content_type, chat_type, chat_id = telepot.glance(msg)
            if chat_type == 'group':
                if command.split(' ')[0][1:] in self.group_command_func.keys():
                    self.group_command_func[command.split(' ')[0][1:]](msg)
                else:
                    self.default(msg)
            else:
                if command.split(' ')[0][1:] in self.private_command_func.keys():
                    self.private_command_func[command.split(' ')[0][1:]](msg)
                else:
                    self.default(msg)
        else:
            print("LOG" + msg)
    def start(self):
        self.message_loop(self.__handle)

        # Listen to the messages
        while 1:
            time.sleep(10)

    def default(self, msg):
        self.sendMessage(msg['chat']['id'], 'This command does not exist, send "/ help" to see the list of commands')
