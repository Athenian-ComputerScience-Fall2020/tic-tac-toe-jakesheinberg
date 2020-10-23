# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.
def mt_tik_tak_toe():
    print("  a b c")
    print("1  |  | ")
    print("  –+––+–")
    print("2")
    print("  –+––+–")
    print("3  |  |")

locations={'a1':' ', 'a2':' ','a3':' ','b1':' ', 'b2':' ', 'b3':' ', 'c1':' ', 'c2':' ','c3':' '}

def game_play():
    mt_tik_tak_toe()
    if locations['a1']==locations['a2']==locations['a3'] or locations['b1']==locations['b2']==locations['b3'] or locations['c1']==locations['c2']==locations['c3'] or locations['a1']==locations['b1']==locations['c1'] or locations['a2']==locations['b2']==locations['c2'] or locations['a3']==locations['b3']==locations['c3'] or locations['a1']==locations['b2']==locations['c3'] or locations['a3']==locations['b2']==locations['c1']:
        print("Game Over!")
    else:
        
