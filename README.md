# INTRODUCTION
This is a student’s management app. Teachers can add new students, delete and update existing students’ data. The app lists students alongside activities they can participate in. Teachers can only list their students. School activities are global. Any teacher can list, create, delete and update school activities


# AUTHENTICATION
This app uses Django-rest Token authentication to authenticate its users. Only authenticated users-teachers are allowed to use the app.


# ENDPOINTS
# Register
 * Method : 'POST'
 * 'base/register/'
 * Required: {'email', 'password'}
#Login
 * Method : 'POST'
 * 'base/login/'
 * required: {'username', 'password'} -email as username
Add Activities
 * Method : 'POST'
 * 'base/activities/'
 * required {'name', 'category'}
List Activities
 * Method :'GET'
 * 'base/activities/'
Add New Student
 * Method : 'POST'
 * 'base/students/'
 * required: {'second_name', 'second_name', 'student_ID(unique)', 'activity'} -Activity has to exist in the activity model
List Studenst
 * Method :'GET'
 * '/base/students/'
Filter Student By Student ID
 * Method : 'GET'
 * '/base/students/?search=search_params'
 * required: student_ID in place of search_params 
Delete Student
 * Method : DELETE
 * '/base/students/<str:id/'
 * required: id
Update Student
 * Method : 'PATCH'
 * 'base/students/<str:id>/'
 * required : id


# REQUIREMENTS
The apps requirements are listed in the requirements.txt file. Alongside the listed requirements, the app also requires installation of Postman. 


# GETTING STARTED
 * Install the requirements listed in the requirements.txt
	Pip install -r requirements
* Once all requirements have been installed, run server
	Python manage.py runserver
* Install Postman
Using postman, import 'Students Management.postman_collection' to access the apps endpoints


# THANK YOU
