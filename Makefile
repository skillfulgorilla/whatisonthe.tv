ENTER_VENV := . venv/bin/activate
VENV_BIN := venv/bin/activate

pip:
	export CFLAGS=-Qunused-arguments; export CPPFLAGS=-Qunused-arguments; 
	$(ENTER_VENV); pip install -r requirements.txt
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

create_listings:
	$(ENTER_VENV); python manage.py create_listings --settings=listings.dev
