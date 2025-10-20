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
