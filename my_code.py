# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.
locations={'a1':' ', 'a2':' ','a3':' ','b1':' ', 'b2':' ', 'b3':' ', 'c1':' ', 'c2':' ','c3':' '}
def mt_tik_tak_toe(locations):
    print("  a b c")
    print( "1",locations['a1'] + "|" +locations['b1']+ "|" + locations['c1'])
    print("  –+–+–")
    print("2",locations['a2']+ "|" +locations['b2']+ "|" +locations['c2'])
    print("  –+–+–")
    print("3",locations['a3'] + "|" +locations['b3']+ "|" +locations['c3'])

mt_tik_tak_toe(locations)#prints initial blank board
x=0
while x<=9:
    if locations['a1']==locations['a2']==locations['a3']!=' ' or locations['b1']==locations['b2']==locations['b3']!=' ' or locations['c1']==locations['c2']==locations['c3']!=' ' or locations['a1']==locations['b1']==locations['c1']!=' 'or locations['a2']==locations['b2']==locations['c2']!=' ' or locations['a3']==locations['b3']==locations['c3']!=' ' or locations['a1']==locations['b2']==locations['c3']!=' ' or locations['a3']==locations['b2']==locations['c1']!=' ':
            mt_tik_tak_toe(locations)#prints final status of game
            print("Game Over!")
            break
    elif x==9:
            print("Its a tie")
            mt_tik_tak_toe
            break
    else:
            spot=input("select the square you would like to play: ")
            if x%2==0:
                mark='O'
            else:
                mark='X'
            try:
                if locations[spot]==' ':
                    locations[spot]=mark
                    mt_tik_tak_toe(locations)#uses variable to skip all the if statements
                    x=x+1
                else:
                    print("Spot is already taken. Try again.")
            except:
                print("Input is invalid. Try again.")
