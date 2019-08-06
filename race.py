#make a horse racing text game

#give horses a goofy name with a fake data library (ie boaty mcgee)
#generate a random arena name ie the arena in louisville kentucky
#give them stats
#str, agility, endurance, charisma (THE CROWD CHEERS!), int or wis (randomly distracted events for low int or wis)

import words
import random
import math
import csv
from flask import Flask
import string
import words as werds


def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain"
    return response


app = Flask(__name__)
@app.after_request

class horse:
    def pickaname(loops):
        
        if loops == 1:
            loops = random.randrange(1,3)
        temp = ''
        for each in range(loops):
            temp += random.choice(werds.nouns).capitalize()
            if each is not (loops-1):
                temp += ' '
        return temp

    def stats():
        stre = random.randrange(1,20)
        inte = random.randrange(1,20)
        end = random.randrange(1,20)
        agl = random.randrange(1,20)
        char = random.randrange(1,20)
        wis = random.randrange(1,20)
        return stre, inte, end, agl, char, wis
        
    def __init__(self):
        self.name = horse.pickaname(random.randrange(1,4))
        tempstats = horse.stats()
        self.str = tempstats[0]
        self.end = tempstats[1]
        self.agl = tempstats[2]
        self.char = tempstats[3]
        self.int = tempstats[4]
        self.wis = tempstats[5]
        self.runningtime = (self.agl * self.str) + self.end
        self.mph = self.str + self.end
        self.distance = math.floor(self.mph * (self.runningtime / 60))

@app.route('/')
def race():
    oldhorselist = [horse() for each in range(8)]
    horselist = oldhorselist.copy()
    matches = []
    last = ''

    total = ['you are sitting in a factory. you see lots of horse parts. you start assembling them.','*time passes*\n\ndays later...',
             'you have 8 horses. some are assembled incorrectly, like a leg sticking out of their head, or two heads, or multiple tails, or extra legs. you can\'t rush art, man.',
             'why do people give their horses such goofy names? the world may never know.','suddenly, they start forming a group and acting impatient. you get the impression they would like to compete. alright then.']
    print('These are your horses:')
    total.append('These are your horses.\n')
    for each in horselist:
            print('{}\nStrength: {}\nEndurance: {}\nAgility: {}\n\n'.format(each.name,each.str, each.end, each.agl))
            total.append('{}\nStrength: {}\nEndurance: {}\nAgility: {}\n\n'.format(each.name,each.str, each.end, each.agl))
    while(len(horselist) > 1):
        for i, each in enumerate(horselist):
            #print('{} ran for {} miles in {} minutes at {} mph'.format(each.name, each.distance, each.runningtime, each.mph))
            try:
                if horselist[i].distance > horselist[i+1].distance:
                    print('{} ran longer than {}. {} vs {}. {} removed'.format(horselist[i].name, horselist[i+1].name,horselist[i].distance,horselist[i+1].distance, horselist[i+1].name))
                    matches.append(horselist[i].name)
                    del horselist[i+1]
                    total.append('{} ran longer than {}. {} vs {}. {} removed'.format(horselist[i].name, horselist[i+1].name,horselist[i].distance,horselist[i+1].distance, horselist[i+1].name))
                else:
                    print('{} ran longer than {}. {} vs {}. {} removed'.format(horselist[i+1].name, horselist[i].name,horselist[i+1].distance,horselist[i].distance, horselist[i].name))
                    matches.append(horselist[i+1].name)
                    del horselist[i]
                    total.append('{} ran longer than {}. {} vs {}. {} removed'.format(horselist[i+1].name, horselist[i].name,horselist[i+1].distance,horselist[i].distance, horselist[i].name))
            except:
                pass

                    
    '''
    elif horselist[i+1].distance > horselist[i].distance:
                    print('{} ran longer than {}. {} vs {}. {} removed'.format(horselist[i+1].name, horselist[i].name,horselist[i+1].distance,horselist[i].distance, horselist[i].name))
                    matches.append(horselist[i+1].name)
                    del horselist[i]
    '''


    print('{} won!'.format(horselist[0].name))
    total.append('{} won!'.format(horselist[0].name))

    chart = '''
HORSE ENDURANCE TEST

-----------------------\\\\\\                                                 
{}    
-------------------------\\\\\\                                                 
                          \\\\\\--------------------------\\\\\\                        
                             {} 
                          ///----------------------------\\\\\\                        
-------------------------///                              \\\\\\                        
{}    
-----------------------///                                  \\\\\\------------------------\\\\\\
                                                              {} 
-----------------------\\\\\\                                  ///--------------------------\\\\\\
{} 
-------------------------\\\\\\                              ///                              \\\\\\
                          \\\\\\----------------------------///                                \\\\\\
                             {} 
                          ///--------------------------///                                    \\\\\\
-------------------------///                                                                  \\\\\\
{}
-----------------------///                                                                       \\\\\\--------------------\\\\\\\\
                                                                                                    {} 
-----------------------\\\\\\                                                                       ///--------------------////
{}
-------------------------\\\\\\                                                                   ///
                          \\\\\\--------------------------\\\\\\                                    ///
                             {} 
                          ///----------------------------\\\\\\                                ///
-------------------------///                              \\\\\\                              ///
{}
-----------------------///                                  \\\\\\--------------------------///
                                                              {} 
-----------------------\\\\\\                                  ///------------------------///
{}
-------------------------\\\\\\                              ///                        
                          \\\\\\----------------------------///                        
                             {} 
                          ///--------------------------///                        
-------------------------///                                                  
{}
-----------------------///

{} WON\n\n
    '''.format(
        oldhorselist[0].name,
                     matches[0],
        oldhorselist[1].name,
                                 matches[4],
        oldhorselist[2].name,
                     matches[1],
        oldhorselist[3].name,
                                               horselist[0].name,
        oldhorselist[4].name,
                     matches[2],
        oldhorselist[5].name,
                                 matches[5],
        oldhorselist[6].name,
                     matches[3],
        oldhorselist[7].name,
        horselist[0].name)

    for each in chart.splitlines():
        print(each)
        total.append(each)

    mph = {}
    runningtime = {}
    distance = {}
    for each in oldhorselist:
        temp = '{},{},{},{}\n'.format(each.name, round(each.runningtime / 60, 2), each.mph, each.distance)
        mph[each.name] = each.mph
        runningtime[each.name] = round(each.runningtime / 60, 2)
        distance[each.name] = each.distance



    temp = '{}{}{}'.format(str.ljust('Name',30),str.ljust('MPH',15),'Value')
    print(temp)
    total.append(temp)
    for speed in mph:
        temp = '{}{}{}'.format(str.ljust(speed,30),str.ljust(str(mph[speed]),15),mph[speed]*'|')
        print(temp)
        total.append(temp)
    print('\n')
    total.append('\n')
    temp = '{}{}{}'.format(str.ljust('Name',30),str.ljust('Running Time',15),'Value')
    print(temp)
    total.append(temp)
    for time in runningtime:
        temp = '{}{}{}'.format(str.ljust(time,30),str.ljust(str(runningtime[time]),15),int(runningtime[time])*'|')
        print(temp)
        total.append(temp)
    print('\n')
    total.append('\n')
    temp = '{}{}{}'.format(str.ljust('Name',30),str.ljust('Miles Ran',15),'Value')
    print(temp)
    total.append(temp)
    for length in distance:
        temp = '{}{}{}'.format(str.ljust(length,30),str.ljust(str(distance[length]),15),int((distance[length]/2))*'|')
        print(temp)
        total.append(temp)
    returny = ''
    for each in total:
        returny += each + '\n'
    return returny

