
## Assignment 1 

Create a docker compose file that runs the following services:  
* Postgres (PG) database, version 13.8
* PGAdmin 4, version 6.13

The Postgres database should have a mounted data folder on your machine.  
You should be able to access the PGAdmin tool from your browser.   
From within the PGAdmin tool you should be able to access the PG database.  


## Assignment 2 

Create a docker compose file that runs the following services:
* Python, version 3.11
* MySQL, version 8.0.34
* Adminer, version 4.8.1

The Python service should be mounted to a folder ./scripts on your local machine.  
MySQL data folder should be mounted on your local machine.  
You should be able to access the MySQL database via Adminer using your browser.  

Create a Python script that, when executed, pulls data from the ISS api (http://api.open-notify.org/iss-now.json), flattens the JSON and inserts it into a table called `iss.iss_now`. If the database or table does not exist, the script should first create them. 