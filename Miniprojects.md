# Mini Projects in Python
 
### Projects on Classes and Functions

1. Write a To Do List Manager console application, using classes in Python that let's a user perform the following: 
	 1. Create new To Do List
	 2. Add a new task to the list
	 3. Mark a particular task as done.
	 4. See the list of all tasks when needed.


   **Technical Specifications:**
   	
Write a python class namely 'ToDoList' to manage all data and functionalities of the application.
   
- Attributes
	- **list_name**: is a 'string' that stores the to_do lists' name.
	- **to_do**: must be a list of all the to do statements.
	- **done**: Must be a list of all the completed to dos.

- Methods
	- **add**: when called on the to_do_list object, should prompt for a new task and append it to the to_do attribute.
	- **mark_done**: when called on a particular task from to_do attribute, should move the element to the done attribute.
	- **see_tasks**: when called shows a list of all the tasks under respective titles i.e., "TO DO" and "DONE"


- How it works:
	1. Create a module with the specified class and import it in an another script which is called 'main.py' where your application logic lies.
	2. When main.py is executed the application must ask the user what to do. 
	3. Based on the input perform the required action.

-----------------------------------------------------------------------------------------------------------------------------

2. Write a Meeting Manager console application, using classes in Python which performs the following:
	1. Check available time slots and display those time slots to the user
	2. Ask for a time slot from the user
	3. Schedule a time to a user
	4. Send a message saying "meeting has been scheduled"


	**Technical Specifications:**
	Write a Python Class namely 'MeetingManager' to manage all data and functionalities of the application.
	
- Attributes
       
	- **dictionary_name:** is a string that stores all the time-slots available to schedule a meeting.
	- **input_from_user:** take a key from the user and print the message saying "this time-slot has been allocated to you".
	- **dictionary_name2:** append this dictionary with the time-slots already set and remove that key-value pair from dictionary-name.
	
- Methods
       
	- **time_view**: when called gives the available time slots.
	- **schedule**: when called schedules a meeting with respect to the available time slots and print the message to say the meeting is scheduled.

- How it works:
       
	1. Create a module with the specified class and import it in another script where your application logic lies.
	2. When the script is executed, the application must do whatever the user asks to do.
	3. Based on the input, perform the required action.

-----------------------------------------------------------------------------------------------------------------------------

3. Write a Console Game, using classes in Python which performs the following:
	1. Create a 2 dimensional matrix and enter random numbers in the size of 8x8 format.
	2. Check take an input from a user.
	3. If the number is present in the 2 dimensional matrix, then the user is out.

	**Technical Specifications**:
	 
 Write a Python class namely 'ConsoleGame' to manage all the data and functionalities of the application.


- Attributes

	- **list_name**: A 2D list to store all the values.
	- **input_from_user**: takes an integer value and stores it in a variable
		
- Methods
	 
	- **run**: executes the program in this one function. The process carried out is, to compare the input number with all the elements in the 2D list. If the input number is found in the 2D list, print a message saying "You lost! :P". Else if the input number is not found print a message saying "Yay! You won! :)".

- How it works:
   
	Create a module with the specified class and import it in another script where your application logic lies.
	When the script is executed, the application must do whatever the user asks to do.
	Based on the input, perform the required action.

-----------------------------------------------------------------------------------------------------------------------------

4. Write an application to detect the points where a rocket launched towards Mars has reached, using classes in Python which performs the following:
	1. Create a dictionary with parameters, distance as key and reach point as value.
	2. Take input as object from user in terms of distance travelled by the rocket. 
	3. Depending on the input given print output message.

- **Technical Specifications:**

	Write a Python class namely 'MarsMissionDetector' to manage all the data and functionalities of the application.

- Attributes

	**dictionary_name**: is a string to store the key value pairs.
	**input_from_user**: take the key as input in the form of object from the user.

- Methods

	Discover what methods you can write and try to figure out the logic of how you can go ahead with the problem. If you find any difficulty, feel free to contact us and schedule a Skpye Call or you can schedule a meeting with us at our office.

-----------------------------------------------------------------------------------------------------------------------------

5. Create an hierarchy of classes - abstract class Employee and child classes HourlyEmployee, SalariedEmployee, Manager and Executive. Everyone's pay is calculated differently, research a bit about it. After you've established an employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire, fire and raise employees.

**NOTE**: You can use functions instead of child classes.

 Try to figure out everything in this problem. If you face any difficulty you know what you should do. 


> Try solving all the problems. These problems are framed in such a way that you will get competent with the concepts of Functions and Classes after solving all these problems. 


> You will have to compulsorily solve 3 problems. You will not be needing more than 5 hours over the duration of 10 days.
