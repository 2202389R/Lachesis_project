# Lachesis_project

## Useful Commands
**Start the development server** <br />
```
python manage.py runserver
```
<br />

**Initialise Database** <br />
```
python manage.py migrate
```
<br />

**Create superuser** <br />
```
python manage.py createsuperuser
```
<br />

2. Update admin.py to include and register your new model(s). <br />
3. Perform the migration $ python manage.py makemigrations <app_name>. <br />
4. Apply the changes $ python manage.py migrate. This will create the necessary infrastructure
within the database for your new model(s). <br />
5. Create/edit your population script for your new model(s).

