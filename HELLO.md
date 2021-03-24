왜 READ ME는 편집이 안될까

## EMART 2팀 장고 서버

### run virtual env
window: env\Scripts\activates


### start project
django-admin startproject [project_name] .

### make new app
cd [project_name]
django-admin start app [app_name]

### init project
python manage.py migrate

### make superuser
python manage.py createsuperuser --email [email] --username [username]