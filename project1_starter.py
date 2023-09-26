from datetime import datetime

###
# with open("input.txt", 'r') as file:
# content = file.read()
# words = content.split()
# file.close()
# print(content)


def schedule():
    busyInput1 = #1st busy time goes here
    workInput1 = #1st work time goes here
    busyInput2 = #2nd busy time goes here
    workInput2 = #2nd work time goes here
    duration = #duration goes here

    #find min time for work hours
    start_time = max(workInput1[0], workInput2[0])
    end_time = min(workInput1[1], workInput2[1])
