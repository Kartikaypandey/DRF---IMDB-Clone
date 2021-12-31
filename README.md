# DRF---IMDB-Clone
Created a REST api similar to IMDB , implemented Permissions , Token Authentication/ JWT Authentication, added Pagination, Filtering , Searching , Ordering , Throttling to the Model 

IMDB Clone using Django REST Framework 
Models -
Models.py
1) Watchlist - Collection of Movies , Tv Series .
2) Streaming Sites - Collections of Streaming Sites
3) Reviews - Reviews and Ratings Posted by user

Serializer.py-
Contains Serializers for the Three Models

Code is Present For Function based + Class Based views

Permissions -

Only admin can add movies , streaming sites
Admin can edit any reviews
User can add Reviews ( 1 review per movie )

Token Authentication-
DRF Documentation for implementing Token Authentication .
token "token hash" in Postman for sending request

JWT Authentication-
django-simplejwt for implementing JWT Authentication , Access Token Refresh Token

Throttling
Anon Throttle , User Throttle , Custom Throttle

Filtering , Searching , Ordering 
Using django-filter for all the Above three (only possible if you use generic class views )

Pagiantion-
By page (1 , 2 , 3 ......)
by offset ( start = 1 , size = 10)
by cursor (Next Prev only)
