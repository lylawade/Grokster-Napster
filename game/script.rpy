# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image building = "newsbuilding.jpg"
image desk = "messydesk.jpg"
image intern = "intern.png"

define i = Character('Me', color="#c8c8ff")
                                       

label start:
    
    scene building
    
    "There you are!"
    
    scene desk
    show intern
    
    i "Oh! Hi Boss!"
    
    "Boss" "The Grokster case has just concluded. I need you to get the lowdown on what happened
            and why so I can write a killer article and take all of the credit."
    
    "Boss" "Uh... of course I would let you write some of it too I guess... It could be your first article
            at the paper. Not a lot of interns get published you know!"

