import re

import re

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]

def getEventsOrder(team1, team2, events1, events2):

    print(team1, team2, events1, events2)

    result = []
    menit = []

    for i in events1:
        result_team1 = team1 + " " + i
        # print(result_team1)
        result.append(result_team1)
        # print(re.findall('\d+', i))
        # menit.append(re.findall('\d+', i))
    for _ in events2:
        result_team2 = team2 + " " + _
        # print(result_team2)
        result.append(result_team2)

    print(result)
    # my_list = ['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
    result.sort(key=natural_keys)
    for a in result:
        menit.append(re.findall('\d+', a))
        for passnum in range(len(menit) - 1, 0, -1):
            for i in range(passnum):
                if menit[i] > menit[i + 1]:
                    temp = menit[i]
                    menit[i] = menit[i + 1]
                    menit[i + 1] = temp
        print(menit)

        print(a)

    return result

if __name__=='__main__':
    print("Simple Program to Sorting Events in a Football Match \n")
    print("There are 4 possible events, Goal (G), Yellow Card (Y), Red Card (R), Subtitution (S)")
    print("Writing format, ex: Team1= /"Liverpool/" with events record: \n events1=[/"Firmino 12 G/", /"Henderson 45+2 Y/"]")
    print("PlayerName, Minutes, Events")

    team1 = input("TEAM1 NAME: ")
    team2 = input("TEAM2 NAME: ")

    events1_count = int(input("Number of events for TEAM1 in the match: ").strip())
    events1 = []

    for _ in range(events1_count):
        events1_item = input("Events for Team1: ")
        events1.append(events1_item)

    events2_count = int(input("Number of events for TEAM1 in the match: ").strip())
    events2 = []

    for _ in range(events2_count):
        events2_item = input("Events for Team2: ")
        events2.append(events2_item)

    result = getEventsOrder(team1, team2, events1, events2)

    print(result)