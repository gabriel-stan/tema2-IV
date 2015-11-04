test:
	cd tema2_IV && echo "estoy en" pwd && python manage.py makemigrations && python manage.py migrate && python manage.py test
