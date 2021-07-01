# AirBnB CLONE - THE CONSOLE
![image](https://user-images.githubusercontent.com/70826697/124161186-b8fa6580-da62-11eb-98d7-1334a4128822.png)


Hello! in this repository we are developing the Airb&b clone by means of Python, let's start with this fascinating journey:

One of the first steps is to create the BaseModel Class, in which we use it through Json of the serialization and deserialization of the instances that we create with them.

We create all the necessary classes to introduce and to handle the user's data like State, City, Place ect.

We create the unittes to confirm the outputs of the instances we create through our class.

# Description of files
## CONSOLE
Console.py is a command interpreter in which we can create different objects, the commands contained in this interpreter are:
> - [do_EOF](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : exit the program by typing Ctrl + d.
> - [empty line](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : an empty line + ENTER does not execute anything.
> - [do_quit](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : exits the program.
> - [do_create](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : creates a new instance of a specific class and saves it (in the JSON file).
> - [do_show](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : prints the string representation of an instance based on the class name and id.
> - [do_destroy](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : deletes an instance based on the class name and id.
> - [do_all](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : shows all instances that are located in the .json file based on the class name or not.
> - [do_update](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : update an instance based on the class name and ID by adding or updating an attribute
> - [do_clear](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : clears the console.

# REQUIREMENTS
AirBnB is designed to run in the Ubuntu 14.04 LTS linux, python3 (version3.4.3), you must be able to run python scripts, if you cannot run them contact the administrator for the appropriate permissions

# EXAMPLE OF USE
Run

![image](https://user-images.githubusercontent.com/70826697/124070744-ec59d780-da03-11eb-87a5-fdf7f6cc9b4b.png)

Use Help

![image](https://user-images.githubusercontent.com/70826697/124070848-1612fe80-da04-11eb-8baf-41975afcf3e8.png)


Creates a new instance of BaseModel

![image](https://user-images.githubusercontent.com/70826697/124070913-3773ea80-da04-11eb-8446-83ed6efff695.png)



# MODELS FOLDER
	This folder contains all the moodulos of the class and of the folder called engine.


#  TEST
	This folder contains all tests that we develop for UNITTEST, in which the tests of each module are included.

# IN INTERACTIVE MODE:

**![](https://lh3.googleusercontent.com/p5GeSdaJ_k3LdDugRsGgZ-rY5lipLgVn_1JsH33JBPBtDISW6HMAXs-gPHVn7n8XB3UNMJIYtc1qq6SZ0KhDiPfOWrCLSTgiA0wagWMV5_0_LKKP8FICF4yb_4yqyC99wrN2E6fA)**


# IN INTERACTIVE MODE:
**![](https://lh5.googleusercontent.com/vDYYzino6J4-Ve84YPMsJXpx587Uf5sZ7ZLTXVrcW7K4Oj5lfQUH2hB84wSLDn9QgiFj2PBGHRpcdImHPQiXf1OaDdgvacTZ_tGbwGKFSZ6nU0snjw_konyz9jLEP4z921s27djZ)**

# AUTHOR
* Jordan bonnett
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=bonnett93&layout=compact&theme=vue&langs_count=6" alt="My github stats"/>
* Julio C Arenas
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=jihuder&layout=compact&theme=vue&langs_count=6" alt="My github stats"/>


# UML diagrams

You can render UML diagrams  For example:

![image](https://user-images.githubusercontent.com/70826697/124066401-30e27480-d9fe-11eb-94dd-df0ee206f983.png)

# AirBnB CLONE - THE CONSOLE
![image](https://user-images.githubusercontent.com/70826697/124161186-b8fa6580-da62-11eb-98d7-1334a4128822.png)


Hello! in this repository we are developing the Airb&b clone, let's start with this fascinating journey.

This project consists of several stages, together they will simulate the backend and the fronend of a complex project such as AirBnB, in this first stage we develop the following:

1. The first steps was to create the directories to contain our modules and convert them into a single package, the estructure is the next one:

	> + AirBnB_clone
	 * /models
	   *  /engine
		 * init.py
		 * file_storage.py
	   + base_model.py
	   + user.py
	   + state.py
	   + place.py
	   + amenity.py
	   + review.py
	 + console.py

2. The **BaseModel** class is the principal of other, all other classes will inherit it's functions, attributes and methods.  We create all the necessary classes to introduce and to handle the data: User, State, City, Place, Review and Amenity.

3. Whit the module **file_storage.py** we use a separated file storage management, in which we use it through Json of the serialization and deserialization of the instances that we create with the console.

4. The module **console**  allow manipulate a powerful storage system, the console it's a command interpreter itself, and it is where the user will interact with our **models** and our **file storage managmend.**

4. The **test** directory has the same structure than **models**, but all the directories and files have the prefix "test_" . We create the unittes to confirm the outputs of the instances we create through our class.

# REQUIREMENTS
AirBnB is designed to run in the Ubuntu 14.04 LTS linux, python3 (version3.4.3), you must be able to run python scripts, if you cannot run them contact the administrator for the appropriate permissions

# Description of files
## CONSOLE
Console.py is a command interpreter in which we can create different objects, the methods started with "do_" allow us to use them as commands (see examples of use).  The methods contained in this interpreter we create of modify are.

> - [empty line](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : an empty line + ENTER does not execute anything.
> - [precmd](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : hook method executed just before the command line is interpreted.           Modify to allow comands in the way arg.command() .
> - [do_all](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : shows all instances that are located in the .json file based on the class name or not.
> - [do_show](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : prints the string representation of an instance based on the class name and id.
> - [do_create](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : creates a new instance of a specific class and saves it (in the JSON file).
> - [do_destroy](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : deletes an instance based on the class name and id.
> - [do_update](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : update an instance based on the class name and ID by adding or updating an attribute
> - [do_count](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : retrieve the number of instances of a class
> - [do_quit](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : exits the program.
> - [do_EOF](https://github.com/bonnett93/AirBnB_clone/blob/main/console.py) () : exit the program by typing Ctrl + d.

![flow_1](https://imagizer.imageshack.com/v2/419x387q90/923/5RqzjM.jpg)

### EXAMPLE OF USE
Run

![image](https://user-images.githubusercontent.com/70826697/124070744-ec59d780-da03-11eb-87a5-fdf7f6cc9b4b.png)

Use Help

![image](https://user-images.githubusercontent.com/70826697/124070848-1612fe80-da04-11eb-8baf-41975afcf3e8.png)


Creates a new instance of BaseModel

![image](https://user-images.githubusercontent.com/70826697/124070913-3773ea80-da04-11eb-8446-83ed6efff695.png)


### INTERACTIVE MODE:

**![](https://lh3.googleusercontent.com/p5GeSdaJ_k3LdDugRsGgZ-rY5lipLgVn_1JsH33JBPBtDISW6HMAXs-gPHVn7n8XB3UNMJIYtc1qq6SZ0KhDiPfOWrCLSTgiA0wagWMV5_0_LKKP8FICF4yb_4yqyC99wrN2E6fA)**


### NON-INTERACTIVE MODE:
**![](https://lh5.googleusercontent.com/vDYYzino6J4-Ve84YPMsJXpx587Uf5sZ7ZLTXVrcW7K4Oj5lfQUH2hB84wSLDn9QgiFj2PBGHRpcdImHPQiXf1OaDdgvacTZ_tGbwGKFSZ6nU0snjw_konyz9jLEP4z921s27djZ)**


# MODELS FOLDER
	This folder contains all the moodulos of the class and of the folder called engine.

* The BaseModel is the unique class with instace attributes, all the rest have only class attributes in way we provide easy class description, provide default value of any attribute and in the future, provide the same model behavior for file storage or database storage.



#  TEST
	This folder contains all tests that we develop for UNITTEST, in which the tests of each module are included.

# AUTHOR
* Jordan bonnett
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=bonnett93&layout=compact&theme=vue&langs_count=6" alt="My github stats"/>
* Julio C Arenas
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=jihuder&layout=compact&theme=vue&langs_count=6" alt="My github stats"/>


# UML diagrams

You can render UML diagrams  For example:

![image](https://imagizer.imageshack.com/v2/419x387q90/923/5RqzjM.jpg)

