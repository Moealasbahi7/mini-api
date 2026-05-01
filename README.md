# Mini API Project

This project is a FastAPI application developed as part of a mini project.  
It provides simple API endpoints and integrates with Google Cloud services.
The application is containerized using Docker and deployed on Google Cloud Run.

## Team Members
Moe Al Asbahi API development and Cloud deployment  
Mia Teixeira Docker setup  
Sana Zouaoui AI integration  

The project was initially done using separate branches for each of us . However, I (moe) did a small error by sending API key to the github which required cleaning but i did not know tht it will delete all the  history. During this process. As a result only the final version of the project is visible in the master branch but you can see the other branchs. (sanas work and mias work), agian I am sorry for that sir and it was made at the final check up and i just deleted the api key.

## Endpoints

GET /hello returns a welcome message  
GET /status returns server date and time  
GET /data retrieves stored data from Google Cloud Storage  
POST /data adds new data to Google Cloud Storage  

## Run Locally

bash
uvicorn app:app --reload