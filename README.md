# Restaurant Project

Breakdown




1. Create your Python final project
1. Define the applications that will be needed
1. Admin and anonymous user
1. Create the applications
1. Modify the settings.py file to include the 1. application classes
1. Define the view functions that will be needed
1. Write the basic structure for each view function that will return a string identifying the view 1. function (i.e. About, Contact, Search, etc.)
1. Create the applications urls.py files and define the route (path) for each view function
1. Modify the project's urls.py file to include each application's urls.py file
1. Confirm that the basic navigation works


App design: 

Applications needed
Admin
1. /admin
1. Name: admin
1. CRUD available restaurants.
Normal User
/
Name: app-restaurants
Search, random, and preferential restaurants etc...

View Functions (Controller)

Admin
1. Create
1. Read
1. Update
1. Delete


Normal users
1. Read restaurants
    1. getAll()
1. Get random 1. restaurant (from 1. available)
    1. getRandom()
1. Search restaurants
    1. searchAvailable1. (input)
1. Get recommendation
    1. getRecommended(input)


Templates (views)
Admin
CRUD restaurants view
Normal users
Get restaurants view
Restaurants results view
