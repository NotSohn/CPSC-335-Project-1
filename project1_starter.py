from datetime import datetime

###
# with open("input.txt", 'r') as file:
# content = file.read()
# words = content.split()
# file.close()
# print(content)


def schedule():
    person1_busy_Schedule = #1st busy time goes here
    person1_work_hours = #1st work time goes here
    person2_busy_Schedule = #2nd busy time goes here
    person2_work_hours = #2nd work time goes here
    duration = #duration goes here

    #convert inputs to datetime objects
    format = "%H:%M"
    workInput1 = [datetime.strptime(x, format) for x in person1_work_hours]
    busyInput1 = [[datetime.strptime(x, format) for x in y ] for y in person1_busy_Schedule]
    workInput2 = [datetime.strptime(x, format) for x in person2_work_hours]
    busyInput2 = [[datetime.strptime(x, format) for x in y ] for y in person2_busy_Schedule]

    #find min time for work hours
    start_time = max(workInput1[0], workInput2[0])
    end_time = min(workInput1[1], workInput2[1])
