import os

# CONFIG
RCON_HOST = os.getenv('MC_HOST',"127.0.0.1")
RCON_PORT = 25575

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN','')
RCON_PASSWORD = os.getenv('RCON_PASSWORD','')

authorized_users_str = os.getenv('AUTHORIZED_USERS', '')

# Convert string to list of integers
if authorized_users_str:
    AUTHORIZED_USERS = [int(x) for x in authorized_users_str.split(',')]
else:
    AUTHORIZED_USERS = []