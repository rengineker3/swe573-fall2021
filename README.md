# swe573-fall2021

## SetUp

1. Clone the repo. Which is: 

`git clone https://github.com/rengineker3/swe573-fall2021.git`

* Project needs postgresql and docker. 
* Start with create your virtual environment with:
`python3 -m venv myvenv`  
`source myvenv/bin/activate`  
* Install: `pip install -r requirements.txt`
* Create Database: 
`docker-compose up --build`  
`docker-compose start db`  
`docker exec -it core_db bash`  
`psql -U postgres`  
`CREATE DATABASE learningland;`  
`/l`  (to check if the database is created).

* After database creation run this command:  
`docker-compose up` Check if the containers are up and running.
* Go to your local host port 80 in the browser, 127.0.0.1:80



### Screen Shots of The Website

1. [Home Page](https://ibb.co/QKpVBfz)
2. [Service/Event Update and Delete Page](https://ibb.co/NVJSRCs)
3. [Service Update Page](https://ibb.co/CHG5xZN)
4. [Profile Page](https://ibb.co/JjCswZn)
5. [Profile Edit Page](https://ibb.co/rvJvGM9)
6. [Service/Event Delete Page](https://ibb.co/WW9Jf2W)


