import yaml
import os

class Chat():

    def __init__(self):
        self.chat_config = self.read_commands()

    @staticmethod
    def read_commands():

        try:

            current_dir = os.path.dirname(__file__)
            yaml_path = os.path.join(current_dir, "commands.yaml")

            with open(yaml_path) as f:
                data = yaml.safe_load(f)
                print("Custom rules found!")
                return data
        except Exception as e:
            print("Chat custom rules could not be loaded, default config is applied...")
            return {}
    
    def check_mc_command(self, command):

        if self.chat_config == {}:
            return True, ""

        cnf = self.chat_config['mc']['commands']
        cmd = command.split(' ')[0]
        attr = ''
        if len(command.split(' '))>1:
            attr = command.split(' ')[1]
        
        
        if cmd not in cnf.keys():
            return True, ""
        else:
            if cnf[cmd]['onSubAttr'] == {}: # Check whole command
                
                cnf_msg = cnf[cmd]['msg']
                if cnf[cmd]['banned']:
                    return False, cnf_msg
                else: 
                    return True, cnf_msg                

            else: # Check subattr
                if attr in cnf[cmd]['onSubAttr'].keys():
                    cnf_sub = cnf[cmd]['onSubAttr'][attr]

                    cnf_msg = cnf_sub['msg']
                    if cnf_sub['banned']:
                        return False, cnf_msg
                    else: 
                        return True, cnf_msg 

    
    def get_help(self, admin=False):
        cnf = self.chat_config
        msg = ''
        for cmd in cnf.keys():
            
            if admin:
                msg += '• /' + cmd + f': {self.return_operation_desc(cmd)}' + '\n'

            elif cnf[cmd]['admin'] == False:
                msg += '• /' + cmd + f': {self.return_operation_desc(cmd)}' + '\n'
        return msg


    def return_operation_desc(self, operation):

        cnf = self.chat_config
        if operation not in cnf.keys():
            return "That is not an operation."
        
        else:
            return cnf[operation]['description']

        

        
        


