# Project Name
AIRBNB clone
![alt text](image.png)

## Description
The goal of this project is to deploy on your server a simple copy of the AirBnB website.

## The console
This will be the first step in cloning the website. It will help backend developers to:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
## Command Interpreter
The command interpreter is a console application built using Python. It can be used in both interactive and non-interactive mode.

### How to Start
To start the command interpreter in interactive mode, run the following command:
```
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit count  create  all show update 

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```