from os import getenv

# TELEGRAM
USERID = int(getenv('USERID'))
if USERID is None:
    raise Exception("Por favor configura tu Moodle User ID") 
