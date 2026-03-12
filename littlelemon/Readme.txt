# Required packages:
 - django
 - mysqlclient
 - djangorestframework
 - djoser
 
# To run the poject execute following commands (MacOS):
python -m venv .venv
source .venv/bin/activate
pip install django mysqlclient djangorestframework djoser

# Open littlelemon/settings.py and setup USER / PASSWORD for your MYSQL database
# Run migrations and start server
cd littlelemon
python manage.py migrate
python manage.py runserver

# Endpoints to be tested:
http://127.0.0.1:8000/restaurant
http://127.0.0.1:8000/restaurant/menu
http://127.0.0.1:8000/restaurant/booking
http://127.0.0.1:8000/restaurant/booking/tables