# NOTE: For this project we are using celery and celery beats, so we will be running three terminals at the same time for this project 

- Terminal_1-> py manage.py runserver
- Terminal_2-> celery -A backend beat -l info
- Terminal_3-> celery -A backend worker -l info --pool=solo (using solo is recommended for windows, but for linux or mac, you don't need --polo=solo
