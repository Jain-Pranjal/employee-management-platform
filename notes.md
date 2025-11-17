
# how to setup the django project using docker and postgresql

to check if the req is installed inside the container or not
```py
pip list
```

1. req.txt add  karo and along with that add dockerfile and docker-compose.yml file
2. docker compose build 
3. move inside the web contianer 
```py
docker compose run web bash
```

4. ab shell ke ander jake we can create the django project using 
```py
django-admin startproject core .
```
5. then run the docker compose up command to start the server
```py
docker compose up
```