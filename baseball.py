# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:54:42 2017

@author: dylanmortimer
"""
from random import randint
# Empty bases

FIRST_E = "   < >\n"
SECOND_E = "     < >      \n"
THIRD_E = "< >    "

# Men on bases
FIRST_F = "   <O>    \n"
SECOND_F = "     <O>      \n"
THIRD_F = "<O>    "
HOME = "     < >    \n"

# atbat expectancies
K_EXPECTANCY = 15
BB_EXPECTANCY = 15
BATTED_BALL_EXPECTANCY = 70
HIT_EXPECTANCY = 3

first = FIRST_E
second = SECOND_E
third = THIRD_E

GAME_LENGTH = 8

# Game States
outs = 0
runners = [0,0,0]
runs = 0
inning = 0
team = 0
score = [0,0]

# Players Team 1
ROSTER = [[4,7,6,7,6,10,9,10,12],[8,5,6,5,6,2,3,2,0],[88,88,88,88,88,88,88,88,88],[315,367,333,321,223,254,276,321,145],['Cool Papa Bell', 'Vic Harris', 'Oscar Charleston', 'Josh Gibson', 'Leroy Morney', 'Judy Johnson', 'Jimmy Crutchfield', 'Ches Williams', 'Satchel Paige'],[96,93,92,85,97,93,95,92,96],[3,5,4,7,2,6,3,4,2],[0,1,2,2,0,0,2,1,2],[1,1,3,6,1,1,0,1,0]]

# Players Team 2
ROSTER2 = [[17,27,17,14,15,21,18,20,25],[12,2,12,15,14,8,11,9,4],[71,71,71,71,71,71,71,71,71],[273,329,356,441,303,227,178,280,231],['Jack Marshall', 'Alex Radcliffle', 'Willie Wells', 'Turkey Stearns','Mule Suttles', 'Walter Davis', 'Wilson Redus','Larry Brown', 'Bill Foster'],[97,94,88,86,88,93,98,94,100],[1,4,7,6,5,4,1,2,0],[1,0,2,3,0,1,1,3,0],[1,2,3,5,7,2,0,1,0]]



def input_roster():
    names = [None]*9
    k_roster = [None]*9
    bb_roster = [None]*9
    batted_roster = [None]*9
    hit_roster = [None]*9
    for i in range(1,10):
        names[i-1] = input("Input Player " + str(i) + " Name: ")
        k_roster[i-1] = int(input("Input the k-rate of player " + str(i) + ": "))
        bb_roster[i-1] = int(input("Input the walk-rate of player " + str(i) + ": "))
        batted_roster[i-1] = int(100 - (k_roster[i-1] + bb_roster[i-1]))
        hit_roster[i-1] = (int(input("Input the BA of player " + str(i) + ": ")))
        
    roster = [k_roster,bb_roster,batted_roster,hit_roster,names]
    return roster

def get_rosters():
    roster = [ROSTER,ROSTER2]
    return roster

def print_field(runners):
    first = FIRST_E
    second = SECOND_E
    third = THIRD_E
    
    if runners[0] == 1:
        first = FIRST_F
    if runners[1] == 1:
        second = SECOND_F
    if runners[2] == 1:
        third = THIRD_F
            
    print(second)
    print(third + first)
    print(HOME)
    
def print_scoreboard(outs,score,inning,runners):    
    print("Inning: " + str(inning))
    print("Outs: " + str(outs))
    print("Home: " + str(score[0]) + " Away: " + str(score[1]))
    print_field(runners)
    
    
def hit_outcome(runners,score,team,roster,player):
    hit_list = [None]*100
    for i in range(0,roster[team][5][player[team]]):
        hit_list[i] = 1
    for j in range(roster[team][5][player[team]],roster[team][6][player[team]]):
        hit_list[j] = 2   
    for h in range(roster[team][5][player[team]] + roster[team][6][player[team]],roster[team][7][player[team]]):
        hit_list[h] = 3
    for k in range(roster[team][5][player[team]] + roster[team][6][player[team]] + roster[team][7][player[team]],roster[team][8][player[team]]):
        hit_list[k] = 4
    outcome = hit_list[randint(0,99)]
    if outcome == 1:
        print("he hit a single")
        if runners[2] == 1:
            score[team] += 1
            runners[2] = 0
            print("you scored!")
        if randint(1,4) > 3:
            runners[2] = runners[1]
            runners[1] = runners[0]
            runners[0] = 1
        else:
            if runners[1] == 1:
                score[team] += 1
                runners[1] = 0
                print("you scored from 2nd!")
            if runners[0] == 1:
                runners[2] = runners[0]
                print("your runner at 1st advanced to 3rd")
            runners[0] = 1
    elif outcome == 2:
        print("he hit a double")
        if runners[2] == 1:
            score[team] += 1
            print("you scored!")
        if runners[1] == 1:
            score[team] += 1
            print("you scored!")
        if randint(1,4) > 2:
            runners[2] = runners[0]
            runners[1] = 1
            runners[0] = 0
        else:
            if runners[0] == 1:
                score[team] += 1
                print("you scored from 1st!")
            runners[2] = 0
            runners[1] = 1
            runners[0] = 0 
    elif outcome == 3:
        print("he hit a triple")
        if runners[2] == 1:
            score[team] += 1
            print("you scored!")
        if runners[1] == 1:
            score[team] += 1
            print("you scored!")
        if runners[0] == 1:
            score[team] += 1
            print("you scored!")
        runners[2] = 1
        runners[1] = 0
        runners[0] = 0
    else:
        print("he hit a homerun!")
        score[team] += 1
        print("you scored!")
        if runners[2] == 1:
            score[team] += 1
            print("you scored!")
        if runners[1] == 1:
            score[team] += 1
            print("you scored!")
        if runners[0] == 1:
            score[team] += 1
            print("you scored!")
        runners[2] = 0
        runners[1] = 0
        runners[0] = 0
    return [runners,score]
    

#def at_bat_outcome(batter_k,batter_w,batter_avg,pitcher_k,pitcher_w,pitcher):
def at_bat_outcome_advanced(team,outs,runners,score,roster,player):
    outcome_list = [None] * 100
    for i in range(0,roster[team][0][player[team]]):
        outcome_list[i] = "k"
    for j in range(roster[team][0][player[team]],roster[team][1][player[team]]+roster[team][0][player[team]]):
        outcome_list[j] = "bb"
    for k in range(roster[team][1][player[team]]+roster[team][0][player[team]],roster[team][2][player[team]]+roster[team][1][player[team]]+roster[team][0][player[team]]):
        outcome_list[k] = "bip"
        
    outcome = outcome_list[randint(0,99)]
    #print("It's a " + str(outcome))
    
    if outcome == "k":
        outs += 1
        print("he struck out")
    elif outcome == "bb":
        print("he walked")
        if runners[2] == 1 and runners[1] == 1 and runners[0] == 1:
            score[team] += 1
            print("he scored!")
        for i in range(1,3):
            if runners[i-1] == 1:
                runners[i] = 1
        runners[0] = 1
        
    else:
        hit = randint(0,999)
        if hit < roster[team][3][player[team]]:
            print("he got a hit!")
            state = hit_outcome(runners,score,team,roster,player)
            runners = state[0]
            score = state[1]
            
        else:
            if randint(1,4) > 2:
                # 50%
                if randint(1,4) > 2:
                    print("he grounded out")
                    outs += 1
                    if outs < 2:
                        if randint(1,4) < 2 and runners[0] == 1:
                         #25% dp
                            print("it's a double play")
                            outs += 1
                            if runners[2] == 1:
                                score[team] += 1
                                print("you scored from 3rd on the double play!")
                            runners[2] = runners[1]
                            runners[1] = 0
                            runners[0] = 0
                        else:
                          #75% not dp
                            if outs < 3:
                                if randint(1,4) < 3:
                                    #50% Lead is not out
                                    if runners[2] == 1:
                                        score[team] += 1
                                        print("you scored on the groundout!")
                                    runners[2] = runners[1]
                                    runners[1] = runners[0]
                                    runners[0] = 0
                                    print("out at 1st")
                                else:
                                    #50% Lead is out
                                    if ((runners[0] == 1) or (runners[1] == 1) or (runners[2] == 1)):                       
                                        print("lead runner is out!")
                                    elif (runners[0] == 1 and runners[1] == 0 and runners[2] == 1):
                                        print("lead runner is out!")                                        
                                        runners[2] = 0
                                        runners[1] = 1
                                    elif (runners[0] == 0 and runners[1] == 0 and runners[2] == 1):
                                        print("lead runner is out!")
                                        runners[2] = 0
                                        runners[0] = 1
                # 50%                            
                else:
                    print("he grounded out")
                    outs += 1
                    if outs < 3:
                        if randint(1,4) < 4:
                            #75 percent out at 1st
                            if runners[2] == 1:
                                score[team] += 1
                                print("you scored on the groundout!")
                            runners[2] = runners[1]
                            runners[1] = runners[0]
                            runners[0] = 0
                            print("out at 1st")
                        else:
                            if ((runners[0] == 1) or (runners[1] == 1) or (runners[2] == 1)):                       
                                print("lead runner is out!")
                            
            else:
                outs += 1
                print("he flies out")
                if randint(1,4) > 1:
                    if runners[2] == 1 and outs < 3:
                        score[team] += 1
                        runners[2] = 0
                        print("you scored on a tag up!")
                    runners[2] = runners[1]
                    if runners[1] == 1:
                        runners[1] = 0
                     
                    
    
    return [outs,score,runners]
            




def play_game():
    roster = get_rosters()
    
    inning = 0
    team = 0
    score = [0,0]
    runners = [0,0,0]
    outs = 0
    print_scoreboard(outs,score,inning,runners) 
    player = [0,0]
    start = input("Play Ball! ")
    print("\n")
    while inning < GAME_LENGTH+1 or score[0] == score[1]:
        outs = 0
        runners = [0,0,0]
        inning += .5
        state = [0,[0,0],[0,0,0]]
        
        if team == 0:
            team = 1
        else:
            team = 0
            print_field(runners)
 
        while outs != 3:
            print(str(roster[team][4][player[team]]) + " is up") 
            state = at_bat_outcome_advanced(team,outs,runners,score,roster,player)
            outs = state[0]
            score = state[1]
            runners = state[2]
            
            print_scoreboard(outs,score,inning,runners)   
            if player[team] == 8:
                player[team] = 0
            else:
                player[team] += 1
        
            if outs == 3:
                print("switch!")
            
             
            pause = input("ready for the next at-bat? ")
            print("\n")
    
    
    if score[0] > score[1]:
        print("Team 0 won!!")
    else:
        print("Team 1 won!!")
        
           
