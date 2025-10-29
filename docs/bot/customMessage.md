# About custom messages

This was a feature added to apply rules to certain commands, commands such as whitelist off or others that can disrupt the game's balance.

An example is provided in [telegram folder](../../telegram_utils/commands/commands.yaml) this very example contains all current possibilities.

For the time being, 'confirm' does not do anything, but will in next update.

# Q&A

## Q: If a command is defined in the yaml file but not in the bot logic will it work?

No, you must provide functionality, for a quick example you may copy [myid operation](../../telegram_utils/robot.py), then from that example you could move forward to perform the desired functionality.

## Q: If a command is not defined in the list but is on the bot logic

Then no rule will be applied. Command will execute as it is.

## Q: That Yaml seems a little bit confusing for me, is mandatory?

Absolutely not, you can remove it and bot will just accept any command.

## Q: Can the bot restart the server?

Good question, I wanted to do that for the first version but, since I wanted to keep it simple it will remain as it is for now, for the moment,you as an administrator will always have a script on server side to quickly execute via ssh either a start command, a restart, stop or status.

TLDR. Not now but maybe a next version will.