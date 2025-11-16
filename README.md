📌 To-Do List Application (Python – Console Based)

A simple yet powerful console-based To-Do List Manager built using Python.
This application allows users to add tasks, assign priority levels, mark tasks as completed, search tasks, sort tasks, and delete tasks.
All tasks are stored in a text file ensuring persistent data across sessions.

✨ Features
✔ Add New Tasks

Add tasks with priority levels (High / Medium / Low).

✔ View Tasks

Display all tasks with color-coded output:

🟡 Pending tasks

🟢 Completed tasks

✔ Mark Tasks as Completed

Instantly update any task to “Completed”.

✔ Remove Tasks

Delete tasks by their number.

✔ Search Tasks

Search for tasks using keywords.

✔ Sort Tasks

Sort tasks by priority in the order:

High

Medium

Low

✔ Persistent Storage

All tasks are saved in tasks.txt using file handling.

✔ Colorful CLI (Using Colorama)

Improves readability and makes the console UI more attractive.

🛠 Technologies Used

Python

Colorama (for colored output)

File handling (open, read, write)

Lists & Dictionaries

📂 Project Structure
/project-folder
│── todo.py
│── tasks.txt
│── README.md

🚀 How to Run the Project
1️⃣ Install Colorama
pip install colorama

2️⃣ Run the Application
python todo.py

📘 Usage Guide

After running the program, you will see a menu:

===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Remove Task
4. Mark Task as Completed
5. Search Task
6. Sort Tasks by Priority
7. Exit


Choose the appropriate number to perform an action.
