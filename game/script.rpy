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
image sony = "sony.png"
image kurumi = "kurumi.png"
image kurumi_2 = "kurumi2.png"
image lawBook = "lawbook.png"
image published = "published.jpg"


image tswift = "tswift.png"
image lawStudent = "lawStudent.png"

image judy = "judgejudy.png"

image makina1 = "makina1.png" 
image makina2 = "makina2.png"

define i = Character('Me', color="#c8c8ff")
define k =Character('Kurumi',color="#ff3333")
define m = Character('Makina',color="ffcc33")

image souter = "brownpigeon.png"
image breyer  = "dirtypigeon.png"
image ginsburg = "whitepigeon.png"
                           
label start:
    play music "Shirobako OST Ending 2- Platinum Jet Instrumental.mp3"
    
    scene building
    
    "Boss""There you are!"
    
    scene desk
    show boss
    
    i "Oh! Hi Boss!"
    
    "Boss" "The Grokster case has just concluded. I need you to get the lowdown on what happened
            and why so I can write a killer article and take all of the credit."
            
    "Boss" "Uh... of course I would let you write some of it too I guess... It could be your first article
            at the paper. Not a lot of interns get published you know!"

    i "I'm on it!"
    "You decide that the first place to go to do some research is the Library"
    stop music fadeout 1.0

    scene library
    with dissolve 
    play music "Clannad Soundtrack- Track 8- Hurry Starfish.mp3"
    i "Well I guess I better start studying Oh.. Hey it's Kurumi with her ever bodacious outfit!"
    
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
        k "Respondents sought money damages and an equitable accounting of profits from petitioners, as well as an injunction against the manufacture and marketing of Betamax VTRs" 
        k "Sony argued that the recording capabilities of the Betamax was well within Fair Use and that capabilities did not constitute copyright infringement"
        k "The Supreme Court concurred with the decision of the District Court in that Sony in that the Betamax was within Fair Use and that the Betamax itself had substantial noninfringing potential"

label KurumiMenu:
menu:
    "Ask Kurumi about Fair use":
        jump FairUse
    "Ask Kurumi about the Betamax and it's noninfringing potential":
        jump BetaMax
    "Search for books on the Sony case":
        jump KurumiSearchBooksScene
    "I think I've got enough information!":
        jump KurumiDormRoomScene
        

label FairUse:
    k "Fair Use is based on four main principles " 
    k "The purpose and character of the use"
    k "Nature of the copyrighted work"
    k"Amount and substantiality"
    k"The effect of the use upon the work's value"
  
    jump KurumiMenu

label BetaMax:
    k "The District Court found that respondents failed to demonstrate harm to the market for their copyrighted works "
    k "The District Court also found that the Betamax had substantial noninfringing potential"
    k " An injunction to prevent the production of the Betamax would deprive the public of the ability to use the Betamax for noninfringing purposes "
    
    jump KurumiMenu
label KurumiSearchBooksScene:
    i "Thanks for the info Kurumi, see you tomorrow! maybe"
    hide kurumi_2
    jump SearchBooksScene
    
label SearchBooksScene:

      "After searching a while you find a book that perfectly explains Sony Corporation of America v. Universal City Studios, Inc."
      show lawBook
      i "Wow this book literally has what I'm looking for!"
      hide lawBook
      show sony  
      i "Book Contents:\n\nSony v. Universal Studios:\n- Case decided in 1984\n- Decided in Sony's favor\n- Betamax technology was in line with fair use doctrine\n- Technology had substantial non-infringing potential\n"
      hide sony
      jump ResearchMenu


label KurumiDormRoomScene:
    
    i "Thanks for the info Kurumi, see you tomorrow, maybe!"
    
    jump DormRoomScene

label DormRoomScene:
    scene dorm
    i "After an exhausting day I think it's time to go to bed."
    with dissolve
    scene dorm
    with dissolve
    "It's morning and you decide to go to campus and ask other students if they remember Napster."
    
label CollegeCampus:
        scene campus
        with dissolve
        stop music fadeout 1.0
        play music "Clannad Soundtrack- Track 12- Country Lane.mp3"
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
    "I think I've I asked all the questions I wanted to ask!":
        jump NapsterConclusion
label QuestionOne:

    
         jump Questionaaire
  # jump Grokster        

m "This is anonymous right?? I think about 80\% of the music I used to get off Napster wasn’t legal."
jump Questionaaire


label QuestionOne:   
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
    
    jump Questionaaire
    
label NapsterConclusion:
    
    i "Alright! Thanks for your help!"
    m "Uh... yeah sure...weirdo"
    
    scene blankpage
    with dissolve
    stop music fadeout 1.0
    play music "Pokemon Ruby-Sapphire-Emerald- Littleroot Town.mp3"
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
    with dissolve
    i"Alright that looks great! Let me get started on the meat of this story, the Grokster and Streamcast Supreme Court ruling!"
    i"I guess the first place I’ll start is the internet to get some background"
    jump Grokster


label Grokster: 
        scene weke
        i "Hmm this looks like a good website.....I think"
        
        scene computer
        i "Found out Grokster and StreamCast Networks were two companies that offered similar p2p services"
        i "And both being sued by MGM and other copyright holders!!"
        i "Ruled in generally in favor of Grokster and StreamCast at the District and Appellate Court level "
        i "These lower courts said Grokster and StreamCast were protected partially under Sony and that since their software system was decentralized they did not have specific knowledge of the infringing acts"
        i "In addition, there was potential for noninfringing uses"
        
        i "Hmm even though the lower courts ruled in favor of these companies, they lost once they reached the Supreme Court.  I guess I should look at the opinions of all the judges then"
        
        scene courtroom
        with dissolve
        stop music fadeout 1.0
        play music "Date A Live OST - 04 - DAL Pancake.mp3"
        i "This looks interesting, there seems to be three main opinions.  Who should I start with first?"

 #       jump Opinions        

        jump Opinions        
        
        
label Opinions:
menu: 
        "Justice Souter": 
                 jump Souter
        "Justices Ginsburg, Rehnquist, and Kennedy":
                  jump Ginsburg
        "Justices Breyer, Stevens, and O’Connor":
                 jump Breyer
        "Done asking all the judges": 
                 jump doneOpinions 
        
        
        
label Souter: 
         "Justice Souter had the main opinion so let’s see what he had to say"
         show souter
         "Justice Souter:" "First , the lower courts had misapplied the Sony rulings.  Grokster and StreamCast are not protected by that ruling."
         "Justice Souter:" "Grokster and StreamCast knew that most of their downloads were from copyrighted material"
         "Justice Souter:" "They even tried to induce their users to freely infringe through their services"
         "Justice Souter:" "The fact that they both had a commercial goal by trying to tap into Napster’s old customer base clearly reflects their intentions"
         "Justice Souter:" "In addition neither company also took any real initiative to tackle the infringing activities"
         "Justice Souter:" "Thus, Grokster and StreamCast are held liable for their actions"
         hide souter
         jump Opinions
        
label Ginsburg: 
        i "Let’s see what Justice’s Ginsburg’s opinion was"
        show ginsburg
        "Justis Ginsburg:" "I’m going to be honest, the Sony case does not protect these companies in this situation regardless of whether Grokster nor StreamCast induced their customers or not"
        "Justis Ginsburg:" "I’m going to be honest, the Sony case does not protect these companies in this situation regardless of whether Grokster nor StreamCast induced their customers or not"
        "Justis Ginsburg:" "The lower courts erred in taking a few examples of legal use of the services to conclude that Grokster and StreamCast are protected under Sony"
        "Justis Ginsburg:" "In addition, the lower courts also focused too much on deciding the legality of the technology when instead they should have debated the legality of the services themselves."
        "Justis Ginsburg:" "Thus Grokster and StreamCast are held liable for the infringing acts of users. In addition, the Sony decision should be more strictly applied going forward."
        hide ginsburg
        jump Opinions
        
label Breyer: 
        i "Hmm, I wonder what Justis Breyer had to say…"
        show breyer
        "Justis Breyer:" "Justice Ginsburg and Justice Souter are correct in finding Grokster and StreamCast liable for contributory infringement.  However, this only because Grokster and StreamCast induced their users to commit to the copyright infringement"
        "Justis Breyer:" "Even though only 10\% of the files were not copyrighted material, that in and of itself is enough to meet the benchmark set by Sony."
        "Justis Breyer:" "There is no concrete reason to interpret and apply the outcome of the Sony case more strictly than  before."
        "Justis Breyer:" "As a result, Grokster and Streamcast are held liable for their actions and the actions of their users."
        hide breyer
        jump Opinions


label doneOpinions:   
    i "This is a lot of great information, let’s see how I can sum it up!"
    i "Lower court rulings were overturned and Grokster & StreamCast were found liable for contributory infringement"
    i "Grokster and StreamCast both knew about the illegal actions of their users, but never took any real initiative to stop such activities."
<<<<<<< HEAD
    scene published 
    with dissolve
    i "We are done with our research!"
    "Now that you've finished your research you begin to work on the paper"
    "You finish the paper and hand it to the boss"
    "A few days later you see that your paper has been published and it's a smashing success!"
    "The end....for now"
=======
    scene published
    i "We are done with our research!"
        
        
        
        
        
        
>>>>>>> 6573fb541d0731a7360e728ab65493d2fba23f5f
    
        


    
