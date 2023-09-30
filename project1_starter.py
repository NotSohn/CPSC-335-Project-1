from datetime import datetime


def schedule(person1_busy_Schedule, person1_work_hours, person2_busy_Schedule, person2_work_hours, duration):
    # convert inputs to datetime objects
    format = "%H:%M"
    workInput1 = [datetime.strptime(x, format) for x in person1_work_hours]
    busyInput1 = [[datetime.strptime(x, format)
                   for x in y] for y in person1_busy_Schedule]
    workInput2 = [datetime.strptime(x, format) for x in person2_work_hours]
    busyInput2 = [[datetime.strptime(x, format)
                   for x in y] for y in person2_busy_Schedule]

    # find min time for work hours
    start_time = max(workInput1[0], workInput2[0])
    end_time = min(workInput1[1], workInput2[1])

    # create an array of unavailable time from the two inputs and sort it
    unavailable_time = busyInput1 + busyInput2
    unavailable_time.sort()

    available_time = []

    # find the time intervals when all members are available
    if (unavailable_time[0][0] - start_time >= timedelta(minutes=duration)):
        available_time.append ((start_time, unavailable_time[0][0]))

    for i in range (1, len(unavailable_time)):
        time_difference = unavailable_time[i][0] - unavailable_time[i-1][1] 
        if (time_difference >= timedelta(minutes=duration)):
            available_time.append ((unavailable_time[i-1][1], unavailable_time[i][0]))
        
    if (end_time - unavailable_time[len(unavailable_time) - 1][1] >= timedelta(minutes=duration)):
        available_time.append((unavailable_time[len(unavailable_time) - 1][1], end_time))

    # convert datetime objects back into time strings to display 
    output = [[i.strftime(format) for i in l] for l in available_time]
    print(output)


def main():
    # Read input from file
    with open("input.txt", 'r') as file:
        content = file.readlines()
        file.close()

    compareTime = True
    while compareTime:
        if len(content) == 0:
            compareTime = False
            break
        elif len(content) == 1:
            compareTime = False
            file.remove(content[0])
            break
        else:
            person1_busy_Schedule = content[0]
            person1_work_hours = content[1]
            person2_busy_Schedule = content[2]
            person2_work_hours = content[3]
            duration = content[4]
            # prepare the next input
            content.remove(content[5])
            schedule(person1_busy_Schedule, person1_work_hours,
                     person2_busy_Schedule, person2_work_hours, duration)
            content.remove(content[0])
            content.remove(content[1])
            content.remove(content[2])
            content.remove(content[3])
            content.remove(content[4])


if __name__ == "__main__":
    main()
