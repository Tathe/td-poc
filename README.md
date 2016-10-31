
Assuming we have installed git, python2.7, pip.



pip -r ~/td-poc/requirements.txt

MySQL_PORT : 3306
server_port : 5000
create database provision_service in your mysql account
run python manage.py db init
run python manage.py db update
run python manage.py db upgrade 
run application using python application.py 

### API's

1. get provision account 

URL : "/v1/provision/<provision_id>"
METHOD : GET


2. update provision account 

URL : "/v1/provision/<provision_id>"
METHOD : PUT

3. delete provision account 

URL : "/v1/provision/<provision_id>"
METHOD : DELETE

4. save provision account 

URL : "/v1/provision"
METHOD : POST



