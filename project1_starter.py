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
