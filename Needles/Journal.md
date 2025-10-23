<h2>October 23rd 2025 - IT WORKS??</h2>
A friend* came over and let me put needles in their arm this morning. It was the first time I've ever done it and I was really scared (more scared than they were, since they've done this plenty of times before) and I kinda messed it up and made it hurt more than it needed to but I did it!!! (sorry friend.)<br>

<br>Friend was extremely patient and had many good ideas. We talked for a while about sanitation - obviously having needles touching wires that have been all over the place is NOT sanitary, and I'm not trying to give them an infection. My idea was that wires would only be connected to the part of the needle that doesn't go through the end (the part with the cap) so the needle part that passes through the body doesn't "touch" the wires, but the wires are still kind of bumping up against the insesrtion point, so we opted for... a less sanitary approach, which some kink people would definitely chew me out about. Wiping the wires down with alcohol before touching them to the needle (maybe should get a spray bottle for this?) and then wiping/spinning the needle with a swab with alcohol on it before withdrawing it from the skin was the solution. 

My original theory was that the circuit would only work if needles were on the same side of the wire, which did indeed work!!!! But at one point friend suggested I attatch it to the other side of the wire - which ALSO WORKED! So current is being conducted THROUGH human skin (which I thought would be too resistant) and 3.3V is not enough to burn or cause discomfort. Certainly wires connected on each end is the hottest/prettiest way for it to look... and also more bondage-y looking. Literally wired into the computer. Very cyborg, very cool. Some good Testuo the Iron Man inspo happening here. 

[i can't get images to load in here no matter what i do for some reason?]

As suspected, capacitive sensor... didn't work. Or rather it did, but extremely weirdly? I was expecting it to fully not recieve any information and for the LED to remain either off or on entirely without changing... But instead it sort of flickered on and off unpredictably? We tried testing it with movement, with outside touch, staying still, etc, and there wasn't any sort of real predictive pattern to the thing... Which is very odd. But I learned this with my past plant synth project - working with bioelectric systems is actually wildly unpredictable because biological things do not function like computers at all! So... maybe this stays as a chaos element? 

Tilt sensor worked perfectly! I was wondering if needle being jostled in the skin would be too painful but either friend is an insane masochist (possible) or skin is an insane organ (seems likely) - he was showing me how you could turn the whole needle basically 90 degrees before it even started to become uncomfortable. So the little movements from the wire attatched to the needle weren't particularly noticable for him.

Something fun though - HE wanted to do more of the controlling of the sensors? I had the wires intentionally long so I would be able to connect without causing harm and explore - but he wanted to move his arm around and cause the sensor to activate. 

Which brought up some fun ideas for future collaboration, since friend is down to keep working with me on this!! I was originally evisioning something that I move around/manipulate/twist/cause pain for someone else, and they immediately jumped to wanting to move around or figuring out how to navigate in ways such that would avoid triggering sensors (like a typical sort of predicament scenario)... 

So:
Does this become a game with win/lose states? Not super thrilled about that... 
Want it to be collaborative between top and bottom!! We both want to play with the circuit and have agency over it :) (Maybe that's something I need to give up though? Should I be adding things to the circuit during play or is it a set it up and let it go situation?) 
Friend's suggestion - multiple triggers need to be activated at the samae time in order to achieve "success" (LED going on? or perhaps off?) "What if one edge of the connection is weaker/not activated, and you have to move in order to make the connection?"
Is the circuit something to "solve"? Idk if I like that either... 

<h3>Future concerns: </h3>
What am I actually doing this for/what am I trying to say? I kinda didn't expect this to actually work, now what?? 
If new components need more power, will voltage be too uncomfortable to withstand??
How to connect raspberry pi and power source to human body so rest of circuit halo is wearable?
Rethink wired connection. Currently using a very thick hard to manipulate wire, is that the best option? I want something sturdy to support different sensors/components... 

<br>*They want to remain annoymous and will be referred to only as friend :) 

<h2>October 20th 2025 - Progression and Failure</h2>
Okay, spent a bit programming and testing a tilt switch. Pretty simple, pull down schematic, when sensor is flat nothing happens, when it is moved (kinda far - at least 90 degrees it seems) it prints to the console and a LED lights up. 

Thinking this will be more effective than a capacitive sensor.. Since by default the touch sensor will be touching skin (it'll be inside skin!) something that requiries more in terms of movement might be more effective/actually work.

My concerns are that the level of tilt required would be way too painful?? I'm going to have the sensor out on some wires, so it's not like the needle in someone's skin needs to be bent, but I'm unsure what that pressure will feel like for the controller person.

Thought maybe let's try something more senstiive, so started building out something with the MPU6050 sensor, that has a gyroscope that senses position and acceleration... which would be cool to try and get more articulate information, and maybe have the LED set to light up with a lesser tilt, but... I can't hook this big ass chip to someone's skin??? At least I don't think so. And it's the whole chip that needs to be tilted. It'd look ugly - just a random circuitboard and 4 gangly wires going back to the Pico W... Cool to work/learn with a new sensor though. This would def work better embedded in something, so maybe we're going back to a clothing wearable....?

I've been testing the needles sans-skin by sticking them in my pants and wiring up from there. I forgot I had one in there and stabbed myself a little bit, which... I dunno, good be interesting to incorporate that sort of bodily awareness/intentionality on purpose. Especially since then it wouldn't depend on getting someone over to stab with needles, which isn't like super inconvenient, but not something I can do entirely independently. 

<h2>October 16th 2025 - Initialization</h2>

Had to reference my own past work for the easiest way to get the MPR 121 sensor set up again properly, so that was nice. Haha. Also decided to work with Thonny rather than PyCharm, I have no idea why an old prof insisted on PyCharm, but it's so bulky and unnecessary for what I'm doing, Thonny has a built in very very simple terminal system and is so helpful. (Bidirectional framing coming in strong here.) 

Surprised/intrigued that needle still works when going through cloth. I mean I guess it's not that surprising, since cloth isn't a particularly strong resistor, but the fact that it can penetrate something and still work on either side is cool. Currently using cheap sewing needles rather than piercing needles but presumably the effect will be the same, but we're still in deep prototype mode. 

I need to find someone else to either put a needle in me or let me put a needle in them to test the circuit, which feels tricky right now. I might be able to do this myself but that feels a bit precarious and like I'm doing too much - I don't want to be moving around a lot fixing circuitry if I'm also part of the circuit, that seems way too easy for something to fall apart. 

Also what do I want this to LOOK like on a human body? I want it to be a beautiful adornment, halo like wires... Where is the wiring for the LED(s) gonna go, since it's not exactly directly connected to the needle other than through the Pico W. 

So next steps: thoughts on visuals. Also other sensors other than touch - want to do a tilt sensor or something, so it alerts when it's jostled... Again causing discomfort if it's in someone's skin. 

<h2>October 2nd 2025 12:49 AM - Idea Generation</h2>
ALRIGHT. IM BORED OF SCREENS. WHATS THE SCREEN GONNA DO FOR ME ANYMORE??? 

i want to try this thing that might be a terrible , dangerous and entirely ineffective idea 

ive been tossing it around in my head but want to jot it down:

doing some sort of bdsm needle play that ends up being an electronic interactive adornment. would be amazing to have some capacitive touch wires attached to needles in someone’s skin, and touch making an led light up / move around to different LEDs on other parts of the body. 

the person who becomes(???) the “controller” experiences painful/pleasurable sensation when played with… something something embodiment but make it really really literal 

many issues: human skin is resistant first of all, so all wiring would have to be on the part of needle before it enters skin barrier. this is better for sanitary reasons tho. risk of accidental short circuit and causing unintentional burns… low voltage required to power an LED probably not enough to burn? (not trying to cause harm, just pain!) 

this feels highly inappropriate in an academic context? is it even appropriate in a kink context? seems minimally qualified for safe/sane/consenual? 

goals for the weekend are bust out some needles and see if i can get a circuit working sans human body
crafting bdsm scenes is basically game design (u got a magic circle, particular win conditions, pre determined rules, fantastical scenarios….)
