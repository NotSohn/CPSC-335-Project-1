# CPSC-335-Project-1

# Project 1: Implementing Algorithm

# Fall 2023 CPSC 335.02/CPSC 335.09 - Algorithm Engineering

## Group Members:

    Student 1:
    Student 2:
    Student 3:

## Abstract

### Develop a pseudocode for an algorithm; analyze your pseudocode mathematically; implement the algorithm in Python or C++; test your implementation; and describe your results.

### The Problem

    Matching Group Schedules The group schedule matching takes two or more arrays as input. The arrays represent slots that are already booked and login/logout time of group members. It outputs an array containing intervals of time when all members are available for a meeting for a minimum duration expected.

## The group schedule matching takes following inputs:

1. Busy_Schedule: A list of list that represent the persons existing schedule (they can’t plan any
   other engagement during these hours)
2. Working_period: Daily working periods of group members. (login,logout)
3. Duration of the meeting

It outputs a list of list containing intervals of time when all members are available for a meeting for the minimum duration of the meeting required.

### Assume there are two persons in your class project group. You want to schedule a meeting with another group member. The members decide to provide you with (a) a schedule of their daily activities, containing times of planned engagements. They are not available during these periods. (b) the earliest and latest times at which they are available for meetings daily. Your schedule and availability are provided too.

### Write an algorithm that takes in your schedule, your daily availability (earliest time, latest time) and that of your group member (or members), and the duration of the meeting you want to schedule. Time is given and should be returned in military format. For example: 9:30, 22:21. The given times(output) should be sorted in ascending order.Inputs are also in sorted order.

### An algorithm for solving this problem involves combing the two sub-arrays into an array containing of a set unavailability, with consideration of the daily active periods.

# Sample input

- person1_busy_Schedule =[ [’12:00’, ’13:00’], [’16:00’, ’18:00’]]
- person1_work_hours = [‘9:00’, ’19:00’]
- person2_busy_Schedule = [[‘9:00’, ’10:30’], [’12:20’, ’14:30’], [’14:30’, ’15:00’], [’16:00’, ’17:00’]]
- person2_work_hours = [‘9:00’, ’18: 30’]
- duration_of_meeting =30

# Sample output

- [[’10:30’, ’12:00’], [’15:00’, ’16:00’], [’18:00’, ’18:30’]]

# Implementation

## Have following files

    1. Project1_starter.py or project1_starter.cpp that defines functions for the algorithm
    described above. You will need to develop and write the functions. Describe how to run your
    program in the ReadMe file
    2. Input.txt containing the sample input files. Use these sample files to run your program to see
    whether your algorithm implementations are working correctly. Have a new line character
    separating the sample test cases (10)
    3. Output.txt – load the sample test case result to output.txt

## To Do

    1. Create a Readme file and include your name(s) and email address(es). The Readme file
    should also contain instructions on how to run your program.
    2. Study the sample input and output above. Write your own complete and clear code for an
    algorithm to solve this problem.
    3. Analyze your code for the algorithm mathematically and prove its efficiency class.
    4. Implement your algorithm using either Python or C++.
    5. Run your code using different data inputs

## Finally, produce a brief written project report in PDF format. Your report should include the following:

    1. Your names, CSUF email address(es), and an indication that the submission is for project 1.
    2. A screenshot showing the output of your code for a minimum of 10 test cases defined by
    yourself.
    3. Link to your github repo. Keep it private until due date. Make it public after due date(No
    code commits allowed post due date, any code change after due date will not be considered
    for grading)
    4. A brief proof argument for the time complexity of your algorithm, including step-counts

## Mathematical Analysis

    Analyze your algorithm mathematically. You should prove a specific big-O efficiency class for the
    algorithm. The analysis should be routine, similar to the ones we have done in class and in the
    textbook. The algorithm’s efficiency class will be one of 𝑂(𝑛), 𝑂(𝑛2), 𝑂(𝑛3), or 𝑂(𝑛4).
    Can we do better? What changes do you think can be made to your algorithm to increase its time
    complexity/efficiency? Will an increase in 𝑛 change the complexity class? 𝑛 is the number of persons
    in the group.

## Grading Rubric

The suggested grading rubric is below.

1. Algorithm design and implementation = 50 points, divided as follows:
   a. Clear and complete code = 20 points
   b. Complete and clear README.md file = 3 points
   c. Successful compilation = 15 points
   d. Produces accurate result = 12 points
2. Analysis = 50 points, divided as follows
   a. Mathematical analysis and proof, including step count =22
   b. Report document presentation = 20 points
   c. Screenshot = 5 points
   d. Comments on possible improvements = 3

## Ensure your submissions are your own works. Your submissions will be checked for similarities using a software.

# Submitting your code

## Submit your project as a zip folder with following format <Team_member_name1_member_2_member_3>.zip to the Project 1 link on Canvas. It allows for multiple submissions. Include following files in the zip folder:

    1. Readme
    2. Input.txt
    3. Project1_starter.py or project1_starter.cpp
    4. Output.txt

# Deadline

    The project deadline is October 2,2023 11:59 pm on Canvas.
    Penalty for late submission is as stated in the syllabus. Projects submitted more than 48 hours after
    the deadline will not be accepted.
