
class CmdParse():

    @staticmethod
    def parse_command(cmd, rsp):

        

        if cmd == 'help':   #Helps parse the help information to be more presentable to the user

            msg = ''
            for c in rsp.split('/'):
                if '|' in c:
                    attrs = ': \n'
                    for a in c.split('|'):
                        attrs += f'\t -{a}\n'
                    msg += c + attrs
                else:
                    msg += ("• " +c+"\n")
            return msg

        else:
            return rsp

