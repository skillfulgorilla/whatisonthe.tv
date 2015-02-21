ENTER_VENV := . venv/bin/activate
VENV_BIN := venv/bin/activate

pip:
	export CFLAGS=-Qunused-arguments; export CPPFLAGS=-Qunused-arguments; 
	$(ENTER_VENV); pip install -r requirements.txt
run: 
	$(ENTER_VENV); python manage.py runserver 0.0.0.0:8010 --settings=listings.settings.dev

tests:
	$(ENTER_VENV); python manage.py test tv --settings=listings.settings.test 

migrations:
	$(ENTER_VENV); python manage.py makemigrations tv --settings=listings.settings.dev

syncdb:
	 $(ENTER_VENV); python manage.py syncdb --settings=listings.settings.dev

migrate:
	$(ENTER_VENV); python manage.py migrate tv --settings=listings.settings.dev

create_listings:
	$(ENTER_VENV); python manage.py create_listings --settings=listings.settings.dev

open_coverage:
	open cover/index.html 

pylint:
	$(ENTER_VENV); pylint --rcfile=.pylintrc tv 
