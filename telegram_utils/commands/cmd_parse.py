class CmdParse():

    def check_command(cmd, rsp):

        print(rsp.split('/'))
        if cmd == 'help':   #Helps parse the help information to be more presentable to the user

            msg = ''
            for c in rsp.split('/'):
                msg += ("- " +c+"\n")
            return msg

        else:
            return rsp

