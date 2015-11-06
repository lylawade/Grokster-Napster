# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image building = "newsbuilding.jpg"
image courtroom = "courtroom.jpg"
image desk = "messydesk.jpg"
image library = "library.jpg"
image dorm="dorm.jpg"

image judge = "judge.png"
image boss = "boss.png"
image kurumi = "kurumi.png"
image kurumi_2 = "kurumi2.png"
image lawBook = "lawbook.png"

image tswift = "tswift.png"
image lawStudent = "lawStudent.png"

image judy = "judgejudy.png"

define i = Character('Me', color="#c8c8ff")
define k =Character('Kurumi')
                                       
label start:
    play music "Shirobako OST Ending 2- Platinum Jet Instrumental.mp3"
    
    scene building
    
    "There you are!"
    
    scene desk
    show boss
    
    i "Oh! Hi Boss!"
    
    "Boss" "The Grokster case has just concluded. I need you to get the lowdown on what happened
            and why so I can write a killer article and take all of the credit."
            
    "Boss" "Uh... of course I would let you write some of it too I guess... It could be your first article
            at the paper. Not a lot of interns get published you know!"

    i "I'm on it!"
    
    scene courtroom
    with dissolve
    
    stop music fadeout 1.0
    
    i "Guess I should start here!"
    
    show judy
    
    "Judge Name" "Well what did you want to ask me?"
    
    scene library
    with dissolve 
    play music "Clannad Soundtrack- Track 8- Hurry Starfish.mp3"
    i "well I guess I better start studying oh.. hey it's kurumi with her ever bodacious outfit"
    "You realize that the library is about to close and that you only have enough time to either talk to Kurumi or look for a book on your case"
    
menu:
    
    "Talk to Kurumi":
        jump KurumiScene
    
    "Research Books":
        jump SearchBooksScene
        
label KurumiScene:

        show kurumi
        k "well well fancy seeing you here"
        i " what are you up to?"
        k "Oh nothing just pretending to study"
        i "haha, well I actually have to study the Sony Case"
        hide kurumi
        show kurumi_2
        k "You mean Sony Corporation of America v. Universal City Studios, Inc? I know everything there is to know about the case, so ask away!"
        i "Wow well I guess my first question would be what is the basis of the case?"
        k "Well the basis of the case was whether or not Sony's Betamax infringed upon copyrighted works by allowing users to record copyrighted works"
        k "Sony sought money damages and an equitable accounting of profits from Universal Studios and petitioners, as well as an injunction against the manufacture and marketing of Betamax VTRs" 
        k "Sony argued that the recording capabilities of the Betamax was well within Fair Use"
        k "The Supreme Court concured with Sony in that the Betamax was within Fair Use and that the Betamax itself had substantial noninfringing potential"

label KurumiMenu:
menu:
    "Ask Kurumi about Fair use":
        jump FairUse
    "Ask Kurumi about the Betamax's noninfringing potential":
        jump BetaMax
    "I think I've got enough information!":
        jump DormRoomScene
        

label FairUse:

label BetaMax:



label SearchBooksScene:

      "After searching a while you find a book that perfectly describes Sony Corporation of America v. Universal City Studios, Inc"
      show lawBook
      i "wow this book literally has what I'm looking for!"

jump DormRoomScene

label DormRoomScene:
    i "Thanks for the info Kurumi, see you tomorrow, maybe"
    scene dorm
    i "After an exhausting day I think it's time to go to bed"
        
    
    
    
    
    
