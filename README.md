# NOTE: For this project we are using celery and celery beats, so we will be three terminals running for this project 

- Terminal_1-> py manage.py runserver
- Terminal_1-> celery -A backend beat -l info
- Terminal_1-> celery -A backend worker -l info --pool=solo (using solo is recommended for windows, but for linux or mac, you don't need --polo=solo
