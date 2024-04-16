# App Desc: Users will be able to keep track of a list of items that need completing within a certain time period as well as be supplied with motivational phrases to complete their tasks. The index page will produce a random phrase from an api to assist in motivating the user to get tasks done as well as have a scrollable list of those tasks. The motivational phrases will be on a carousel so that the user can change the phrase at will to one to their liking. The index page will also have an area where the user can add a new task, a delete button where they can remove a completed or no longer needed task, an edit button where they can update the title, details, or date/time due, and a completed checkbox where the task will be listed as completed, but not yet deleted. The show page will show the explicit details of the task that they selected. This area will also contain buttons that will allow the user to update, delete, or otherwise manipulate the information for a specific task. There will be a footer that contains the developer's information, such as a link to their linkedIN and a link to their github.
# Once MVP is met and styling to satisfaction, User Authentication will be added for a more personal experience for the user.

-------------------------------------------------------------
# BACKEND

## Dependencies
- Vue.js
- Vue Router
- Vue Carousel (TBD which one)
- vue-infinite-scroll
- Axios
- Vuex (maybe)
- Vuelidate (maybe)
- Python
- Django
- Django Rest Framework
- dj_database_url
- environ
- os
- psycopg2-binary
- gunicorn


## ERD
![Schema](./images/CapERD.png)

## Route Map
| Route Name | Endpoint | Method | Description            |
| ---------- | -------- | ------ | ---------------------- |
| Create Account | / | POST | Create a new Task Account |
| User Auth | / | GET | Sign In to Account
| Index | /task | GET | All tasks |
| Create | /task | POST | Add a task |
| Index Update | /task | PUT | Change a task |
| Index Delete | /task | DELETE | Remove a task |
| Show | /:id | GET | Details for One task |
| Show Update | /:id | PUT | Change a task |
| Show Delete | /:id | DELETE | Remove a task |

------------------------------------------------------------
# FRONTEND

## Tree
![Tree](./images/Tree.png)

----------------------------------------------------
# User Auth
![UserAuth](./images/UserLogInandCreate.png)

----------------------------------------------------
# New Account
![NewAccount](./images/NewAccountCreation.png)

----------------------------------------------------
# Index
![Index](./images/Index.png)

----------------------------------------------------
# Show
![Show](./images/Show.png)