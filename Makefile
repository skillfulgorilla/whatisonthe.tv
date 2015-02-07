ENTER_VENV := . ../venv/bin/activate
VENV_BIN := ../venv/bin/activate

pip:
	$(ENTER_VENV); pip install -r requirements
run: 
	$(ENTER_VENV); python manage.py runserver 0.0.0.0:8010 --settings=listings.dev

tests:
	$(ENTER_VENV); python manage.py test tv --settings=listings.test 

migrations:
	$(ENTER_VENV); python manage.py makemigrations tv --settings=listings.dev

syncdb:
	 $(ENTER_VENV); python manage.py syncdb --settings=listings.dev

migrate:
	$(ENTER_VENV); python manage.py migrate tv --settings=listings.dev

