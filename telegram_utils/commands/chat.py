import yaml

class Chat():

    def __init__(self):
        chat_config = self.read_commands()

    @staticmethod
    def read_commands():

        try:
            with open("commands.yml") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            print("Chat custom rules could not be loaded, default config is applied...")
            return {}
    
    def check_mc_command(self, command):

        cnf = self.chat_config
        
        if cnf == {}:
            return True, ""
        elif command not in cnf['mc']['commands']:
            return True, ""
        else:

            print("TODO")


        
    def return_operation_desc(self, operation):

        cnf = self.chat_config
        if operation not in cnf.keys():
            return "That is not an operation."
        
        else:
            cnf[operation]['description']

        

        
        


