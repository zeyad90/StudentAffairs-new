web: gunicorn college_management_system.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate