# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image building = "newsbuilding.jpg"
image courtroom = "courtroom.jpg"
image desk = "messydesk.jpg"
image library = "library.jpg"
image dorm="dorm.jpg"
image campus = "collegecampus.jpg"
image blankpage = "blankpage.jpg"
image saving = "saving.png"

image weke = "weke.png"
image judge = "judge.png"
image boss = "boss.png"
image computer = "laptop.jpg"

image kurumi = "kurumi.png"
image kurumi_2 = "kurumi2.png"
image lawBook = "lawbook.png"


image tswift = "tswift.png"
image lawStudent = "lawStudent.png"

image judy = "judgejudy.png"

image makina1 = "makina1.png" 
image makina2 = "makina2.png"

define i = Character('Me', color="#c8c8ff")
define k =Character('Kurumi',color="#ff3333")
define m = Character('Makina',color="ffcc33")
                                       
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
    
    stop music fadeout 1.0

    scene library
    with dissolve 
    play music "Clannad Soundtrack- Track 8- Hurry Starfish.mp3"
    i "Well I guess I better start studying Oh.. Hey it's Kurumi with her ever bodacious outfit!"
    "You realize that the library is about to close and that you only have enough time to either talk to Kurumi or look for a book on your case"

label ResearchMenu:    
menu:
    
    "Talk to Kurumi":
        jump KurumiScene
    
    "Research with books":
        jump SearchBooksScene
        
    "I'm done researching":
        jump DormRoomScene
        
label KurumiScene:

        show kurumi
        k "Well well, fancy seeing you here!"
        i "What are you up to?"
        k "Oh nothing, just pretending to study."
        i "(Haha) Well I actually have to study the Sony Case."
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
        jump KurumiDormRoomScene
        

label FairUse:
    k "Fair Use is based on four main principles: " 
    jump KurumiMenu

label BetaMax:
    k "The court found that the Betamax had many non-infringing use potential (such as educational purposes)."
    jump KurumiMenu

label SearchBooksScene:

      "After searching a while you find a book that perfectly describes Sony Corporation of America v. Universal City Studios, Inc."
      show lawBook
      i "Wow this book literally has what I'm looking for!"
      i "Book Contents:\n\nSony v. Universal Studios:\n- Case decided in 1984\n- Decided in Sony's favor\n- Betamax technology was in line with fair use doctrine\n- Technology had substantial non-infringing potential\n"
      hide lawBook
      jump ResearchMenu


label KurumiDormRoomScene:
    i "Thanks for the info Kurumi, see you tomorrow, maybe!"
    jump DormRoomScene

label DormRoomScene:
    scene dorm
    i "After an exhausting day I think it's time to go to bed."
    with dissolve
    scene dorm
    "It's morning and you decide to go to campus and ask other students if they remember Napster."
    
label CollegeCampus:
        scene campus
        i "Hmm lets see....."
        i "Oh that person looks like they've used Napster before!"
        "You pull aside an innocent looking girl and decide to interrogate her."
        show makina1
        m "Whaaa??"
        i "So do you know anything about Napster?"
        hide makina1
        show makina2
        m "Oh Napster? I loved Napster!! It was a cool p2p technology software that made it easy to share music !!!"
        m "In fact alot of the music that's in my IPOD was downloaded off of Napster!"
        "You decide to question Makina more about Napster."
        
label Questionaaire:
menu:
    "Could you guess about what percentage of the music was actually legal?":
        jump QuestionOne
    "Did you use Napster for space shifting?":
        jump QuestionTwo
    "Have you heard of the new artist program?": 
        jump QuestionThree
    "Do you know what happened to Napster?":    
        jump QuestionFour
    "What do you use now instead of Napster?":
        jump QuestionFive    
label QuestionOne:   
    m "This is anonymous right?? I think about 80\% of the music I used to get off Napster wasn’t legal."
    jump Questionaaire

label QuestionTwo:
    m "Oh space shifting? That's when you store music on a server from one device and then access on it another device.\nI did use Napster for that, but instead of just holding onto my music and accessing it from everywhere, I could get music from other people!"
    jump Questionaaire

label QuestionThree:
    m "Yeah I heard about it, but I really didn’t use Napster for that honestly. I already know what music artists I like!!"
    jump Questionaaire

label QuestionFour:
    m "I heard they got sued or something and went out of business!!"
    jump Questionaaire     

label QuestionFive:
    m "Instead of Napster I started using Grokster’s Swaptor application.  It made it easy for me to quickly do the stuff I used to do on Napster with Grokster.  Though I heard they got sued too, so I’m not sure what’s next…"
    "Alright! Thanks for your help!"
    m "Uh... yeah sure..."
    hide m
    jump NapsterConclusion
    
label NapsterConclusion:
    scene blankpage
    "Well I better put together my research on the Napster case...\n"
    
    "1. Case was decided in US District Court in 2000 against Napster."
    "2. Judge Patel found that Napster’s service was not protected by Sony ruling and that the substantial noninfringing use did not apply."
    "3. The claims of fair use regarding space shifting and sampling by Napster were also dismissed since Napster made permanent copies of uploaded
     files (not sampling) and made said files available to other users (not protected as space shifting)."
    "4. Napster’s claims for permissive distribution were accepted and those features of Napster were allowed to continue."
    "5. Also found that Napster was held for contributory infringement because while they “terminated users” offering the copyrighted files, the files
     themselves remained available to other users. "
    "6. Napster also planned on benefiting from this service commercially."
    "7. Court ends up granting plaintiff's request for a preliminary injunction."
    "8. Napster ends up declaring bankruptcy in 2002."
    
    scene saving
    "Alright that looks great! Let me get started on the meat of this story, the Grokster and Streamcast Supreme Court ruling!"
    "I guess the first place I’ll start is the internet to get some background"
    jump Grokster

label Grokster: 
        scene weke
        i "Hmm this looks like a good website"
        
        scene computer
        i "Found out Grokster and StreamCast Networks were two companies that offered similar p2p services"
        i "And both being sued by MGM and other copyright holders!!"
        i "Ruled in generally in favor of Grokster and StreamCast at the District and Appellate Court level "
        i "These lower courts said Grokster and StreamCast were protected partially under Sony and that since their software system was decentralized they did not have specific knowledge of the infringing acts"
        i "In addition, there was potential for noninfringing uses"
        
        i "Hmm even though the lower courts ruled in favor of these companies, they lost once they reached the Supreme Court.  I guess I should look at the opinions of all the judges then"
        
        scene courtroom
        i "This looks interesting, there seems to be three main opinions.  Who should I start with first?"
        jump Opinions        
        
        
label Opinions:
menu: 
        "Justice Souter": 
                 jump Souter
        "Justices Ginsburg, Rehnquist, and Kennedy":
                  jump Ginsburg
        "Justices Breyer, Stevens, and O’Connor":
                 jump Breyer
        
        
        
label Souter: 
        i "Justice Souter had the main opinion so let’s see what he had to say"
        #show souter
        "First , the lower courts had misapplied the Sony rulings.  Grokster and StreamCast are not protected by that ruling."
        "Grokster and StreamCast knew that most of their downloads were from copyrighted material"
        "They even tried to induce their users to freely infringe through their services"
        "The fact that they both had a commercial goal by trying to tap into Napster’s old customer base clearly reflects their intentions"
        "In addition neither company also took any real initiative to tackle the infringing activities"
        "Thus, Grokster and StreamCast are held liable for their actions"
        jump Opinions
        
label Ginsburg: 
        i "Let’s see what Justice’s Ginsburg’s opinion was"
        #show ginsburg
        "I’m going to be honest, the Sony case does not protect these companies in this situation regardless of whether Grokster nor StreamCast induced their customers or not"
        "I’m going to be honest, the Sony case does not protect these companies in this situation regardless of whether Grokster nor StreamCast induced their customers or not"
        "The lower courts erred in taking a few examples of legal use of the services to conclude that Grokster and StreamCast are protected under Sony"
        "In addition, the lower courts also focused too much on deciding the legality of the technology when instead they should have debated the legality of the services themselves."
        "Thus Grokster and StreamCast are held liable for the infringing acts of users. In addition, the Sony decision should be more strictly applied going forward."
        jump Opinions
        
label Breyer: 
        i "Hmm, I wonder what these three had to say…"
        #show breyer
        "Justice Ginsburg and Justice Souter are correct in finding Grokster and StreamCast liable for contributory infringement.  However, this only because Grokster and StreamCast induced their users to commit to the copyright infringement"
        "Even though only 10\% of the files were not copyrighted material, that in and of itself is enough to meet the benchmark set by Sony."
        "There is no concrete reason to interpret and apply the outcome of the Sony case more strictly than  before."
        "As a result, Grokster and Streamcast are held liable for their actions and the actions of their users."
        jump Opinions
        

    
