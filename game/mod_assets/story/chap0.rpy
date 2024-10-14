$ switch = True

define switch = True

transform flip:
    xzoom -1.0

label chap_0:
    stop music fadeout 2.0
    uk "Hey!"
    uk "Hey you!"
    scene bg class_day with dissolve
    play music t2
    show sayori 4r at t11
    s "You're finally awake."
    show sayori 1a with dissolve
    "I wake up to the cheerful voice of a girl."
    mc "Sayori?"
    show sayori 4r with dissolve
    s "Welcome back to the real world! Ehehe~."
    "I just had a weird dream."
    "A terrifying one."
    show sayori 2i with dissolve
    s "Were you up all night playing video games again?"
    "One where I had lost all of my friends in the literature club."
    show sayori 2j with dissolve
    s "Hellooo, Earth to [player]!"
    "I stand up and rush to hug Sayori."
    show sayori 4m at h11
    s "Ah!"
    show sayori 4n with dissolve
    s "Ohh!"
    show sayori 1s with dissolve
    s "Ehehe~. This feels nice."
    show sayori 1f with dissolve
    s "Wait.. are you okay, [player]?"
    "I pull back from the hug to look at Sayori."
    mc "Yeah, I'm just relieved."
    mc "It was just a.. bad dream."
    mc "Nothing to worry about."
    s "Do you want to talk about it?"
    mc "Maybe some other time."
    s "Okay..."
    show sayori 1l with dissolve
    s "You slept through class again."
    mc "It's not like I missed anything important."
    show sayori 2j with dissolve
    s "Hey! You need to start paying more attention in class."
    mc "Still need me to do your homework for you?"
    show sayori 5c at s11
    s "N-no... I can do it myself."
    mc "Oh really... Perhaps you could help me with my homework then."
    show sayori 5b with dissolve
    s "{size=-5}On second thought, maybe I do need your help afterall."
    mc "What was that?"
    "I asked with a smirk."
    show sayori 4p at h11
    s "S-stop teasing me!"
    mc "Ahaha, I can't help it."
    mc "Want to head over to the literature club?"
    show sayori 1a at t11 with dissolve
    s "Sure. Hold on, let me grab my things."
    hide sayori
    
    "Sayori shuffles through her backpack, slotting a piece of paper into a notebook."
    "I forgot to write a poem last night. Between homework and video games, my night was pretty much booked."
    "But I still need to turn in a poem like everyone else."
    "Perhaps I can spare a few minutes to write one. Even if it may look sloppy."
    show sayori 1a at flip:
        t11
    mc "You can go on without me, Sayori."
    show sayori 1h with dissolve
    s "Ehh? Why?"
    mc "I uh-"
    show sayori 1i with dissolve
    "Even without me saying it, Sayori seemed to know I haven't written my poem yet."
    ".{w=0.5}.{w=0.5}."
    mc "Just a few minutes, please. I'll be there before you know it."
    "I pleaded, slightly bowing my head."
    show sayori 1a with dissolve
    s "Okay. Just don't make it too short."
    mc "Oh! And, Sayori..."
    s "Huh?"
    mc "Don't tell Monika."
    show sayori 1r with dissolve
    s "Ehehe~! Okay."
    hide sayori with moveoutright
    
    "And with that, she took off."
    "It's been two weeks since I joined the literature club."
    "I wasn't particularly great with poetry or literature in general, yet the girls still accepted me into their club."
    "We worked together to make the festival a success for the sake of our club."
    "Yet, the festival didn't go too well for us."
    "I guess a lot of students don't see the appeal of literature."
    "A while ago, I was one of them."
    "I'm embarassed to say my reason for joining the club were the cute girls."
    "But with time, they opened my eyes to something I never expected to care about."

    scene bg corridor with wipeleft_scene
    "I was very eager to visit the literature club today."
    "Of course, my poetry skills hasn't improved just yet. But I really wanted to see how everyone's doing."
    "Maybe I should hold back on hugging them though."
    "Natsuki would drive her tiny fists through my solar plexus without a moment's hesitation."
    "And Yuri might just pass out instantly."
    "Let's hope I still remember the way to the nurse's office."

    stop music fadeout 2.0
    scene bg club_day with wiperight_scene
    play music t5
    play sound closet_open
    "I peek into literature club."
    "Yuri is sitting quietly in a corner reading a thick novel."
    "In my mind's eye, I see the word 'Dictionary' printed on the surface."
    "I blink in quick succession to correctly discern 'Diary Of--', and the rest were concealed by her fingers."
    "Behind Yuri, Natsuki is rummaging around in the closet with Sayori in tow."
    "It seems Sayori is being used as a temporary bookshelf while Natsuki sorts through her numerous collection."
    "But Sayori does look like her hands might give out under the weight of the mangas she's holding."
    "And Monika isn't present in the clubroom."
    "...I thought {i}I {/i} was late."
    "I plan to say hi to everyone."
    
    menu:
        "But who should I say hi to first?"
        "Natsuki":
            jump natsuki_choice

        "Yuri":
            jump yuri_choice
            

label natsuki_choice:
    "Yuri is too immersed in her novel to notice me, so I walk over to Natsuki."
    scene bg closet with fade
    show natsuki 1g at flip:
        t21
    show sayori 1f at s22
    "Sayori dips as Natsuki adds more books to the heap."
    mc "Here Sayori, let me handle this."
    show sayori 4a at t22
    play sound fall
    "Sayori releases the books into my arms with visible relief." with vpunch
    mc "Whoa! These are quite heavy."
    show sayori 4a at f22
    s "You have so much manga, Natsuki."
    show natsuki 3h at flip with dissolve:
        f21
    show sayori 4a at t22
    n "Yeah, and I've read through most of them."
    show natsuki 3h at flip with dissolve:
        t21
    mc "What do you plan to do with all this?"
    show natsuki 3c at flip with dissolve:
        f21
    n "I'll just sell them, I guess."
    n "I can't keep these at home. And they're really starting to fill up the closet."
    show natsuki 3c at flip with dissolve:
        t21
    mc "You can just give them to me."
    show natsuki 2e at flip with dissolve:
        f21
    n "Haven't you already read these?"
    "I hold back a smile."
    show natsuki 1p at flip:
        hf21
    show sayori 1r with dissolve
    n "You're going to sell them and keep all the profit!"
    "Busted."
    show natsuki 1p at flip with dissolve:
        t21
    show sayori 1a with dissolve
    mc "That's not true. I was going to sell them and give you all the profit."
    show natsuki 1r at flip with dissolve:
        f21
    n "I don't believe you."
    show natsuki 1r at flip with dissolve:
        t21
    mc "I was going to sell them and give you a percentage of the profit."
    show natsuki 1l at flip with dissolve:
        f21
    show sayori 1q with dissolve
    n "Okay, now {i}that {/i} I believe."
    hide sayori with dissolve
    show natsuki 1a at flip with dissolve:
        t21
    "Sayori has left the chat."
    show natsuki 1a at t11
    "I watch Sayori silently wander over to Yuri."
    mc "Are you buying new ones as well?"
    show natsuki 2b with dissolve
    n "Maybe. But I still need to find some space for that."
    mc "How about--{nw}-"
    show natsuki 2e with dissolve
    n "No! I'm not keeping it at your house."
    mc "Eh!? Why not? I'll take good care of it, I promise."
    show natsuki 2q with dissolve
    n "Because I'll have to come over to your house whenever I want to read it."
    mc "Why is that a problem?"
    show natsuki 1t with dissolve
    n "Well.. because.."
    show natsuki 1s with dissolve
    n "..Because.."
    show natsuki 1n with dissolve
    pause(0.5)
    show natsuki 1r with dissolve
    pause(0.5)
    show natsuki 4x with dissolve
    n "Because I don't want to, dummy!"
    "I can't help but laugh."
    show natsuki 4f with dissolve
    n "What's so funny?"
    mc "It's nothing... Nevermind."
    "I was going to call her 'cute', but she's firmly wielding a manga with both hands. It's not hard to imagine what she would do if she gets too flustered."
    scene bg closet with fade
    "Natsuki and I had finished sorting through her list. They were neatly stacked into boxes which she was going to leave behind."
    show natsuki 1a at t11
    mc "When do you plan on selling them?"
    n "This weekend. There's a half price bookstore somewhere in town. I bet they'll be glad to take on this bundle."
    show natsuki 3q with dissolve
    n "But it's going to be difficult getting it from my house to the bookstore."
    mc "Oh, is it far?"
    n "Not really. These boxes are just heavy."
    mc "Maybe I can help."
    show natsuki 1k with dissolve
    n "Really? You'll help me carry it to the bookstore?"
    "She points to the box on the floor."
    mc "I said maybe"
    show natsuki 5u with dissolve
    "Although it looks like a lot of heavy lifting for a girl like Natsuki, I can't promise I'll have time."
    "I have no idea what task might pop up before the weekend."
    "However-"
    mc "If nothing comes up, where should I meet you?"
    show natsuki 5y with dissolve
    n "At the bus stop, you know the one."
    mc "Which one?"
    n "The one closest to my house."
    mc "But I don't know where you live."
    n "Figure it out!"
    mc "You want me to stalk you?"
    show natsuki 5o with dissolve
    mc "I could just follow you home after school."
    show natsuki 5q with dissolve
    n "I'll pass on that."
    show natsuki 1x with dissolve
    n "Fine, I'll tell you which one it is."
    show natsuki 1y with dissolve
    n "..if you make up your mind to help me, meet me at the front gates after school."
    n "I'll even throw in a cookie as a reward."
    mc "You're talking to [player], not Sayori."
    show natsuki 4h with dissolve
    n "Whatever. Let me know if you'll be there."
    hide natsuki with moveoutleft
    "She quickly walks away."
    "I've never tried one of Natsuki's cookies so perhaps I should offer her some help."
    "Not like that's my reason for offering. I just think the cookies are a nice bonus."
    "The cookies... {w=0.5}Yeah."
    "I walk over to Yuri."

    scene bg club_day with fade
    show yuri 1a at t22
    y "Hello!"
    "Yuri perks up as she notices me."
    mc "Doing some light reading I see."
    "Yuri only reacted to that."
    mc "I hope I'm not interupting anything. Maybe I should just go."
    y "N-no, It's fine!"
    hide yuri

    jump continue_1

label yuri_choice:
    show yuri 1a at t22
    y "Hello!"
    "Yuri perks up as she notices me."
    mc "Doing some light reading I see."
    "Yuri only reacted to that."
    mc "I hope I'm not interupting anything. Maybe I should just go."
    y "N-no, It's fine!"
    hide yuri

    scene bg closet with fade
    show natsuki 1g at flip:
        t21
    show sayori 1f at s22
    "Sayori dips as Natsuki adds more books to the heap."
    mc "Here Sayori, let me handle this."
    show sayori 4a at t22
    play sound fall
    "Sayori releases the books into my arms with visible relief." with vpunch
    mc "Whoa! These are quite heavy."
    show sayori 4a at f22
    s "You have so much manga, Natsuki."
    show natsuki 3h at flip with dissolve:
        f21
    show sayori 4a at t22
    n "Yeah, and I've read through most of them."
    show natsuki 3h at flip with dissolve:
        t21
    mc "What do you plan to do with all this?"
    show natsuki 3c at flip with dissolve:
        f21
    n "I'll just sell them, I guess."
    n "I can't keep these at home. And they're really starting to fill up the closet."
    show natsuki 3c at flip with dissolve:
        t21
    mc "You can just give them to me."
    show natsuki 2e at flip with dissolve:
        f21
    n "Haven't you already read these?"
    "I hold back a smile."
    show natsuki 1p at flip:
        hf21
    show sayori 1r with dissolve
    n "You're going to sell them and keep all the profit!"
    "Busted."
    show natsuki 1p at flip with dissolve:
        t21
    show sayori 1a with dissolve
    mc "That's not true. I was going to sell them and give you all the profit."
    show natsuki 1r at flip with dissolve:
        f21
    n "I don't believe you."
    show natsuki 1r at flip with dissolve:
        t21
    mc "I was going to sell them and give you a percentage of the profit."
    show natsuki 1l at flip with dissolve:
        f21
    show sayori 1q with dissolve
    n "Okay, now {i}that {/i} I believe."
    hide sayori with dissolve
    show natsuki 1a at flip with dissolve:
        t21
    "Sayori has left the chat."
    show natsuki 1a at t11
    "I watch Sayori silently wander over to Yuri."
    mc "Are you buying new ones as well?"
    show natsuki 2b with dissolve
    n "Maybe. But I still need to find some space for that."
    mc "How about--{nw}-"
    show natsuki 2e with dissolve
    n "No! I'm not keeping it at your house."
    mc "Eh!? Why not? I'll take good care of it, I promise."
    show natsuki 2q with dissolve
    n "Because I'll have to come over to your house whenever I want to read it."
    mc "Why is that a problem?"
    show natsuki 1t with dissolve
    n "Well.. because.."
    show natsuki 1s with dissolve
    n "..Because.."
    show natsuki 1n with dissolve
    pause(0.5)
    show natsuki 1r with dissolve
    pause(0.5)
    show natsuki 4x with dissolve
    n "Because I don't want to, dummy!"
    "I can't help but laugh."
    show natsuki 4f with dissolve
    n "What's so funny?"
    mc "It's nothing... Nevermind."
    "I was going to call her 'cute', but she's firmly wielding a manga with both hands. It's not hard to imagine what she would do if she gets too flustered."
    scene bg closet with fade
    "Natsuki and I had finished sorting through her list. They were neatly stacked into boxes which she was going to leave behind."
    show natsuki 1a at t11
    mc "When do you plan on selling them?"
    n "This weekend. There's a half price bookstore somewhere in town. I bet they'll be glad to take on this bundle."
    show natsuki 3q with dissolve
    n "But it's going to be difficult getting it from my house to the bookstore."
    mc "Oh, is it far?"
    n "Not really. These boxes are just heavy."
    mc "Maybe I can help."
    show natsuki 1k with dissolve
    n "Really? You'll help me carry it to the bookstore?"
    "She points to the box on the floor."
    mc "I said maybe"
    show natsuki 5u with dissolve
    "Although it looks like a lot of heavy lifting for a girl like Natsuki, I can't promise I'll have time."
    "I have no idea what task might pop up before the weekend."
    "However-"
    mc "If nothing comes up, where should I meet you?"
    show natsuki 5y with dissolve
    n "At the bus stop, you know the one."
    mc "Which one?"
    n "The one closest to my house."
    mc "But I don't know where you live."
    n "Figure it out!"
    mc "You want me to stalk you?"
    show natsuki 5o with dissolve
    mc "I could just follow you home after school."
    show natsuki 5q with dissolve
    n "I'll pass on that."
    show natsuki 1x with dissolve
    n "Fine, I'll tell you which one it is."
    show natsuki 1y with dissolve
    n "..if you make up your mind to help me, meet me at the front gates after school."
    n "I'll even throw in a cookie as a reward."
    mc "You're talking to [player], not Sayori."
    show natsuki 4h with dissolve
    n "Whatever. Let me know if you'll be there."
    hide natsuki with moveoutleft
    "She quickly walks away."
    "I've never tried one of Natsuki's cookies so perhaps I should offer her some help."
    "Not like that's my reason for offering. I just think the cookies are a nice bonus."
    "The cookies... {w=0.5}Yeah."

    jump continue_1

label continue_1:
    scene bg club_day with wipeleft_scene
    "Monika walks in-"
    show noise zorder 5:
        alpha 0.25
    play sound "sfx/s_kill_glitch1.ogg"    
    pause(0.25)
    hide noise
    
    show monika 1f at flip zorder 4:
        t41
    "A strange feeling washed over me. I was suddenly drawn back to events of my dream."
    show natsuki 2e at t43 zorder 3
    n "Took you long enough."
    show sayori 1a at flip zorder 2:
        t42
    s "Piano lessons again?"
    show natsuki 2g at t43 with dissolve
    m "Yeah, I'm really sorry about that."
    show yuri 1j at f44 zorder 1
    y "These lessons seem to take up more of your time these days. You've barely spent any time in the club."
    show monika 1g at flip with dissolve:
        f41
    show yuri 1i at t44 with dissolve
    m "It's getting more complex as I advance. Sorry, I don't really know how to explain it."
    show sayori 3x at flip with dissolve:
        f42
    show monika 1g at flip:
        t41
    s "Maybe I can come watch you play sometime."
    show monika 1n at flip with dissolve:
        f41
    show sayori 3a at flip:
        t42
    m "I don't mind. Don't expect anything spectacular though, I'm half decent at best."
    show monika 2d at flip with dissolve:
        f41
    m "More importantly-"
    "Monika looks at me."
    m "Are you okay, [player]?"
    show natsuki 2c at f43 with dissolve
    show monika 2d at flip:
        t41
    n "Yeah, you look like you've seen a ghost."
    show sayori 3b at flip with dissolve:
        t42
    show yuri 1f at t44 with dissolve
    "I close my eyes and try to {color=#add8e6}calm down"
    scene black with dissolve
    stop music fadeout 1.0
    "It was just a bad dream- and yet part of me feels frightened."
    $ style.say_dialogue = style.edited
    "But it felt so real."
    "She--"
    $ style.say_dialogue = style.normal
    "No! I'm being paranoid."
    "She hasn't given me any reason to panic."
    "Suddenly I get very self conscious. I must look like an idiot right now."
    "{i}*sigh*"
    scene bg club_day with dissolve
    play music t5
    show monika 1f at flip zorder 4:
        t41
    show sayori 1f at flip zorder 2:
        t42
    show natsuki 1c at t43 zorder 3
    show yuri 1n at t44 zorder 1 
    mc "Sorry, I started feeling dizzy all of a sudden."
    show natsuki 2c at f43 with dissolve
    n "That doesn't explain the look of shock-"
    show yuri 1t at f44 with dissolve
    show natsuki 2g at t43
    y "Do you need to go to the nurse's office?"
    show yuri 1t at t44
    mc "It's fine, it's fine."
    show monika 3c at flip with dissolve:
        f41
    m "You can talk to us if something's bothering you."
    "{i}If only you knew."
    show sayori 3c at flip with dissolve:
        f42
    show monika 1c at flip:
        t41
    s "Is this a side effect from staying up late?"
    "{i}Nice save, Sayori!"
    show yuri 1f at f44 with dissolve
    show sayori 1a at flip:
        t42
    y "Uh- I don't think-"
    show yuri 1f at t44
    mc "Yes, that must be it!"
    mc "I was up late working on my poem."
    show natsuki 4b at f43 with dissolve
    n "Really?"
    "I was at least thinking about it."
    show natsuki 4g at t43
    mc "Look, what matters is that I have them right here."
    m "..."
    show monika 2b at flip with dissolve:
        f41
    m "Then I'm sure it was beautifully written."
    show monika 2a at flip:
        t41
    mc "Don't hold your breath. It'll probably be mediocre compared to yours."
    show natsuki 5l at f43 with dissolve
    n "Finally, you're starting to recognize my talent."
    show natsuki 5l at t43
    mc "..Baking?"
    show natsuki 5l at f43 with dissolve
    n "Yes and-"
    show sayori 3r at flip with dissolve:
        hf42
    show natsuki 5p at t43
    s "Being cute!"
    show sayori 3r at flip:
        t42 
    show natsuki 1s at t43 with dissolve
    show yuri 1m at t44 with dissolve
    show monika 1j at flip with dissolve:
        t41
    mc "You took the words right out of my mouth."
    "Yeah"
    $ show_poem(poem_mc1, music=True)
    "Looks decent enough."

define poem_choices = ["sayori", "natsuki", "yuri", "monika"]
define monika_selected = 0

label poem_share:
    if len(poem_choices) == 0:
        return

    menu:
        "Who should I share it to?"
        "Sayori" if "sayori" in poem_choices:
            jump share_sayori
        "Natsuki" if "natsuki" in poem_choices:
            jump share_natsuki
        "Yuri" if "yuri" in poem_choices:
            jump share_yuri
        "Monika" if "monika" in poem_choices:
            if ("sayori" in poem_choices or "yuri" in poem_choices or "natsuki" in poem_choices) and monika_selected == 0:
                "I should show the others first."
                $ monika_selected += 1
                jump poem_share
            elif ("sayori" in poem_choices or "yuri" in poem_choices or "natsuki" in poem_choices) and monika_selected == 1:
                "I can't approach Monika just yet."
                $ monika_selected += 1
                jump poem_share
            elif ("sayori" in poem_choices or "yuri" in poem_choices or "natsuki" in poem_choices) and monika_selected == 2:
                "What is going on with my thoughts today? Other girls first, Monika last!"
                $ monika_selected += 1
                jump poem_share
            elif ("sayori" in poem_choices or "yuri" in poem_choices or "natsuki" in poem_choices) and monika_selected == 3:
                "Dammit! I must be going crazy."
                $ monika_selected += 1
                jump poem_share
            elif ("sayori" in poem_choices or "yuri" in poem_choices or "natsuki" in poem_choices) and monika_selected == 4:
                "I need to get this out of my head this instant!"
                $ poem_choices.remove("monika")
                jump poem_share
            

label share_sayori:
    s "..."
    s "Wow [player], You've gotten really good!"
    mc "You really think so?"
    s "Yeah. When you first joined, I could tell you were writing to impress us."
    s "But now you're starting to really express yourself."
    mc "I'm glad you liked it."
    s "I really do!"
    s "But anyway, here's mine."
    $ poem_choices.remove("sayori")
    if "sayori" not in poem_choices and "yuri" not in poem_choices and "natsuki" not in poem_choices:
        jump share_monika
    else:
        jump poem_share

label share_natsuki:
    n "..."
    n "It's not half bad."
    mc "So you're saying it's half good?"
    n "I'm saying our skills are slowly rubbing off on you."
    mc "You're not wrong about that. I can now add 'accomplised poet' to my resume."
    n "Don't get ahead of yourself.. Not until you read mine first."
    "Natsuki shoves her poem into my hand."
    $ poem_choices.remove("natsuki")
    if "sayori" not in poem_choices and "yuri" not in poem_choices and "natsuki" not in poem_choices:
        jump share_monika
    else:
        jump poem_share

label share_yuri:
    y "..."
    y "Spectacular."
    y "Quite an elaborate writing you have here."
    mc "Why, thank you!"
    y "You're acclimating to the club a lot quicker than I did. It's really impressive."
    mc "I learned from having to spend time with eveyone. I'm glad I've been able to improve."
    y "Well, here's mine. I hope you like it."
    "I take Yuri's poem and read it."
    $ poem_choices.remove("yuri")
    if "sayori" not in poem_choices and "yuri" not in poem_choices and "natsuki" not in poem_choices:
        jump share_monika
    else:
        jump poem_share

label share_monika:
    m "..."
    m "Very interesting."
    m "What did you have in mind when writing this?"
    mc "Oh uhm- Nothing in particular. Just classic teen angst."
    m "You've perfectly represented their emotions on paper. Well done!"
    mc "That's a lot of praise coming from the club president."
    m "Ahaha! Well I like to give credit where its due."
    mc "Can I take a look at yours?"
    m "Sure!"
    m "Monika hands me her poem."
    $ poem_choices.remove("monika")
    jump poem_share



