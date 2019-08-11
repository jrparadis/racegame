# racegame
a python / flask script that generates a horse racing tournament

example at http://jasonrparadis.xyz:5000 - refresh to generate new games and statistics

words.py is just a list of random words to make horse names from - I watched some thing about race horses and the goofy names inspired me to write a script to generate horse names, and it kind of winded it's way into this. The stats are basically pointless, horse races don't really work like this, but it's not suppose to be realistic anyway.

example:

```
You are sitting in a factory. You see lots of horse parts. You start assembling them.
*time passes*

...DAYS LATER

You have 8 horses. Some are assembled incorrectly, like a leg sticking out of their head, or two heads, or multiple tails, or extra legs. You can't rush art, man.
Why do people give their horses such goofy names? The world may never know.
Suddenly, they start forming a group and acting impatient. you get the impression they would like to compete. alright then.
These are your horses.

Serve Board Slide
Strength: 2
Endurance: 6
Agility: 14


Self Response Actor
Strength: 17
Endurance: 7
Agility: 12


Traffic End Tennis
Strength: 9
Endurance: 10
Agility: 7


Dream Routine Most
Strength: 9
Endurance: 3
Agility: 9


Farm Reason
Strength: 9
Endurance: 6
Agility: 19


Guest Tongue Lock
Strength: 9
Endurance: 11
Agility: 19


Baseball Entry
Strength: 9
Endurance: 16
Agility: 1


Variety Contribution Bone
Strength: 3
Endurance: 19
Agility: 13


Traffic End Tennis ran longer than Self Response Actor. 23 vs 84. Self Response Actor removed
Traffic End Tennis ran longer than Farm Reason. 23 vs 44. Farm Reason removed
Baseball Entry ran longer than Guest Tongue Lock. 10 vs 60. Guest Tongue Lock removed
Self Response Actor ran longer than Guest Tongue Lock. 84 vs 60. Guest Tongue Lock removed
Self Response Actor won!

HORSE ENDURANCE TEST

-----------------------\\\                                                 
Serve Board Slide    
-------------------------\\\                                                 
                          \\\--------------------------\\\                        
                             Self Response Actor 
                          ///----------------------------\\\                        
-------------------------///                              \\\                        
Self Response Actor    
-----------------------///                                  \\\------------------------\\\
                                                              Self Response Actor 
-----------------------\\\                                  ///--------------------------\\\
Traffic End Tennis 
-------------------------\\\                              ///                              \\\
                          \\\----------------------------///                                \\\
                             Traffic End Tennis 
                          ///--------------------------///                                    \\\
-------------------------///                                                                  \\\
Dream Routine Most
-----------------------///                                                                       \\\--------------------\\\\
                                                                                                    Self Response Actor 
-----------------------\\\                                                                       ///--------------------////
Farm Reason
-------------------------\\\                                                                   ///
                          \\\--------------------------\\\                                    ///
                             Guest Tongue Lock 
                          ///----------------------------\\\                                ///
-------------------------///                              \\\                              ///
Guest Tongue Lock
-----------------------///                                  \\\--------------------------///
                                                              Guest Tongue Lock 
-----------------------\\\                                  ///------------------------///
Baseball Entry
-------------------------\\\                              ///                        
                          \\\----------------------------///                        
                             Variety Contribution Bone 
                          ///--------------------------///                        
-------------------------///                                                  
Variety Contribution Bone
-----------------------///

Self Response Actor WON


    
Name                          MPH            Value
Serve Board Slide             8              ||||||||
Self Response Actor           24             ||||||||||||||||||||||||
Traffic End Tennis            19             |||||||||||||||||||
Dream Routine Most            12             ||||||||||||
Farm Reason                   15             |||||||||||||||
Guest Tongue Lock             20             ||||||||||||||||||||
Baseball Entry                25             |||||||||||||||||||||||||
Variety Contribution Bone     22             ||||||||||||||||||||||


Name                          Running Time   Value
Serve Board Slide             0.57           
Self Response Actor           3.52           |||
Traffic End Tennis            1.22           |
Dream Routine Most            1.4            |
Farm Reason                   2.95           ||
Guest Tongue Lock             3.03           |||
Baseball Entry                0.42           
Variety Contribution Bone     0.97           


Name                          Miles Ran      Value
Serve Board Slide             4              ||
Self Response Actor           84             ||||||||||||||||||||||||||||||||||||||||||
Traffic End Tennis            23             |||||||||||
Dream Routine Most            16             ||||||||
Farm Reason                   44             ||||||||||||||||||||||
Guest Tongue Lock             60             ||||||||||||||||||||||||||||||
Baseball Entry                10             |||||
Variety Contribution Bone     21             ||||||||||
```
