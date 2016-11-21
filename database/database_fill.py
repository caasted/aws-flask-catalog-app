from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///productcatalog.db')
base.Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a first user for entering items
user = user.User(name="Secret User", email="somebody@email.com")
session.add(user)
session.commit()

# Create a first store to associate products with
store = store.Store(name="Virtual Reality Store", user_id=1)
session.add(store)
session.commit()

# Create items to populate the product list
# Item information compiled from Amazon.com and Steampowered.com
item = product.Product(name="Samsung Gear VR", 
				category="Hardware", 
				description="""Light weight so you can play and watch more 
				comfortably. Easy to use touch pad wide field of view, precise 
				head-tracking and low latency brings reality to the virtual. Be 
				transported to amazing new worlds, in games, video and images. 
				Thousands of 360 degree panoramic photos. Compatible with: 
				Samsung Galaxy S7, S7 edge,Note5,S6 edge+,S6,S6 edge. Improved 
				fit, including room for most eyeglasses and improved padding for 
				extra comfort and durability.""", 
				price="$59.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item2 = product.Product(name="Plustore 3D Virtual Reality Glasses", 
				category="Hardware", 
				description="""Revolutionary optical system - it completely 
				eliminates the feel of vertigo. Fit everyone's eyes: Pupil 
				settings for the best 3D experience, even to those near-sighted. 
				Innovative design comfortable wearable - Adjustable straps for 
				flexible wear, Super Lighter Weight of 156g. Turn your 
				smartphone into a virtual reality viewer. Enjoy real 360-degree 
				videos and immersive world of VR from the comfort of your home. 
				Adaptable - adaptable for adroid and ios smart phones with the 
				screen size being "4.7-6" inches and pixels over 1280*720.""", 
				price="$16.88", 
				store_id=1, 
				user_id=1)
session.add(item2)
session.commit()

item3 = product.Product(name="SARLAR 3D VR Glasses", 
				category="Hardware", 
				description="""TAKE CARE OF YOUR EYES AND PUT ZERO 
				PRESSURE-Lower eyelid is the weakest part of the eyes. It's 
				based on human engineering, redesign the position on basis of 
				regurlar headband to re lieve the load of nose bridge and eyelid 
				so as to allevate feeling of fatigue. OVERSIZED VISUAL ANGLE 
				GETS YOU IMMERSIVE-FOV102 panoramic view and the screen is 
				magnified 5.2 times than before,the super vision will give you 
				unlimited world, an incredible visual fidelity and immersive 
				feeling. NO ADJUSTMENTS ARE NEEDED FOR THE MIDDLE LINE OF DOUBLE 
				SCREENS-The supporting structure for mobile phones in the left 
				and right together with gear adjustment can perfectly immobilize 
				the phone.Also,it supports phones with larger size.There is no 
				need to adjust the position of moble phones after the first 
				adjustment.The middle line adjustment is so simple!The design is 
				just humanized and awesome. ASPHERIC LENS DESIGN,FRAMES WILL BE 
				MORE COMFORTABLE-Aspheric lens design,the frame has no 
				abnormalities and perfectly fit for the visual habits,no 
				spinning sensation will generate when wearing.High adjustment no 
				ghosting. COMPATIBLE WITH ALMOST ALL MOBILE PHONES-Sarlar vr 
				glasses is with small size but it supports large size phones 
				will various brands and types,compatibles with almost all mobile 
				phones.It is suitable for any smart phone which screen size is 
				from 4.0-6.5",more than that you cannot call it mobile phone,it 
				is compatible with mobile phones which length doesn't exceed 
				175mm and width doesn't exceed90mm.""", 
				price="$19.99", 
				store_id=1, 
				user_id=1)
session.add(item3)
session.commit()

item4 = product.Product(name="Cellay 3D VR Goggles", 
				category="Hardware", 
				description="""Glasses-free: Without wearing the glasses if your 
				visual acuity is under 600 degree. IMAX Effect: Anti-distortion 
				aspheric design, lowering down the distortion and enjoying 3D 
				IMAX world. Adjustable Distance:VR virtual reality headset is 
				able to adjust focal length and pupil distance according to 
				different people. T-shaped Strap: It helps you reduce the 
				pressure around your eyes and almost suitable for everyone. 
				Compatible with: VR helmet fit for smartphone just as Apple and 
				Android phone and screen between 4.0~6.5 inches.""", 
				price="$33.45", 
				store_id=1, 
				user_id=1)
session.add(item4)
session.commit()

item5 = product.Product(name="Google Cardboard", 
				category="Hardware", 
				description="""GOOGLE CARDBOARD is the primary experience 
				version of 3D VR Glasses. It's made from the AAA grade 
				corrugated paper which is the strongest material. Our product.Product is 
				the highest quality for this price in the market. HAVING 
				ADVANCED GOOGLE CARDBOARD according to the advice from customers 
				and tested it over 80 times. We add the longer head strap,
				suction cups and forehead pad. So far, we have sold more than 
				500,000 sets. COMPATIBLE FOR all the 3.5"- 6.0" smartphones.
				Whether your phone system is Android system or other systems, 
				you can use the TOPMAXION Cardboard to watch Left-right 3D 
				movies on Video Player and play varieties of VR games. IN ORDER 
				TO EXPERIENCE HIGH QUALITY 3D FEELING, you'd better use high 
				resolusion smartphones. Experience a truly stunning, engrossing 
				VR experience with cinematic HD visuals from your smart phone's 
				screen using the included biconvex lenses offering a 37 mm focal 
				length for the best visuals! THE PERFECT SOLUTION for Virtual 
				Reality on a budget!Box-style package with good portability, 
				easily take anywhere.""", 
				price="$9.99", 
				store_id=1, 
				user_id=1)
session.add(item5)
session.commit()

item = product.Product(name="Oculus Rift", 
				category="Hardware", 
				description="""Oculus Rift's advanced display technology 
				combined with its precise, low-latency constellation tracking 
				system enables the sensation of presence. Customizable, 
				comfortable, adaptable, and beautiful, Rift is technology and 
				design as remarkable as the experiences it enables. Every aspect 
				of Rift was designed to be easy, inviting, and comfortable to 
				use - and that extends to the VR environment we've created as a 
				starting point for your journeys. Discover and download games 
				across genres ranging from action RPGs, sci-fi shooters, 
				mind-bending puzzle games, and more - and play them from an 
				entirely new perspective. Lucky's Tale is included with every 
				Rift purchase. Windows PC and an internet connection are 
				required for Oculus Rift - please review recommended system 
				specs.""", 
				price="$599.00", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="HTC Vive", 
				category="Hardware", 
				description="""Vive is built from the ground up for room-scale 
				VR, which allows you to physically move around objects in the 
				virtual space. With more than 500 games and growing for SteamVR, 
				everything you love about Steam is now available in VR. The 
				Gallery: Call of the Starseed, Tilt Brush and Zombie Training 
				Simulator come with Vive for free. An adjustable headset and 
				multiple eye relief adjustments, including lens distance and 
				IPD, to make Vive comfortable and clear. Wireless controllers 
				designed specifically for VR make interactions with objects 
				natural and intuitive. Enjoy a safe, convenient experience with 
				Chaperone bounds of your play area, a front-facing camera to 
				view the real world and notifications from your phone in VR. 
				Compatible Windows computer and internet connection 
				required-refer to the recommended computer specs below.""", 
				price="$799.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Virtual Reality Insider: Guidebook for the VR Industry", 
				category="Reference", 
				description="""Virtual reality is as explosive a technology as 
				the Internet! Are you working in the VR industry, or curious to 
				find out more about it? VR Insider is an overview and guidebook 
				for consumer virtual reality. For the industry veteran, it is 
				the perfect book to stir up new ideas and see how the big 
				picture fits together. For newcomers to VR, it is the fastest 
				way to catch up on what is happening and figure out how to apply 
				your skills. Affordable virtual reality hardware finally exists, 
				and this book will help you create its content! Best of all, 
				this book is readable in 1-2 hours!""", 
				price="$8.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="""Learning Virtual Reality: Developing Immersive 
				Experiences and Applications for Desktop, Web, and Mobile""", 
				category="Reference", 
				description="""As virtual reality approaches mainstream consumer 
				use, a vibrant development ecosystem has emerged in the past few 
				years. This hands-on guide takes you through VR development 
				essentials for desktop, mobile, and browser-based applications. 
				You'll explore the three go-to platforms-OculusVR, Gear VR, and 
				Cardboard VR-as well as several VR development environments, 
				programming tools, and techniques. If you're an experienced 
				programmer familiar with mobile development, this book will help 
				you gain a working knowledge of VR development through clear and 
				simple examples. Once you create a complete application in the 
				final chapter, you'll have a jumpstart on the next major 
				entertainment medium.""", 
				price="$26.01", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="The VR Book: Human-Centered Design for Virtual Reality", 
				category="Reference", 
				description="""Without a clear understanding of the human side 
				of virtual reality (VR), the experience will always fail. The VR 
				Book bridges this gap by focusing on human-centered design. 
				Creating compelling VR applications is an incredibly complex 
				challenge. When done well, these experiences can be brilliant 
				and pleasurable, but when done badly, they can result in 
				frustration and sickness. Whereas limitations of technology can 
				cause bad VR execution, problems are oftentimes caused by a lack 
				of understanding human perception, interaction, design 
				principles, and real users. This book focuses on the human 
				elements of VR, such as how users perceive and intuitively 
				interact with various forms of reality, causes of VR sickness, 
				creating useful and pleasing content, and how to design and 
				iterate upon effective VR applications. This book is not just 
				for VR designers, it is for managers, programmers, artists, 
				psychologists, engineers, students, educators, and user 
				experience professionals. It is for the entire VR team, as 
				everyone contributing should understand at least the basics of 
				the many aspects of VR design. The industry is rapidly evolving, 
				and The VR Book stresses the importance of building prototypes, 
				gathering feedback, and using adjustable processes to 
				efficiently iterate towards success. With extensive details on 
				the most important aspects of VR, more than 600 applicable 
				guidelines, and over 300 additional references, The VR Book will 
				bring a strong foundation for anyone and everyone involved in 
				creating VR experiences.""", 
				price="$71.96", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="""The Real Reason Facebook Acquired Oculus Rift: How 
		Virtual Reality Will Disrupt Every Industry and Why You Should Care""", 
				category="Reference", 
				description="""What is Facebook's interest in acquiring a gaming 
				platform for $2 Billion? In this book I make bold predictions 
				that will be reality within the next five years. Regardless of 
				what industry you work in today, this will affect you. Learn 
				the history of virtual reality and the 4 simple steps necessary 
				for you to profit off of this massively game-changing 
				technology.""", 
				price="$9.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="The Lab", 
				category="Software", 
				description="""Set in a pocket universe of Aperture Science, 
				The Lab offers a wide range of ways to enjoy VR, all in one 
				application.  - Slingshot : Begin your career as a 
				Calibration Trainee by recklessly destroying everything in the 
				Aperture Storage Annex using the Core Calibration slingshot. 
				 - Longbow : Use your archery skills to defend your noble 
				castle gate from a rampaging but adorable and equally noble 
				horde of attackers.  - Xortex : Are you a bad enough 
				dude to become a Xortex ace? Relive the golden era of gaming -- 
				only this time, it's all around you.  - Postcards : 
				Visit exotic, far-off locales from the comfort of your own head. 
				 - Human Medical Scan : Explore the intricate beauty of 
				the human body through a highly detailed model created from a 
				series of CT medical scans.  - Solar System : Why watch 
				shows about the vast majesty of space when you can jump in and 
				see it for yourself? Have educational space-fun while putting 
				Neil Degrasse-Tyson out of business.  - Robot Repair : 
				Can you repair a robot? Good, because Aperture Science's Human 
				Diversity Outreach Program is now hiring.  - Secret Shop 
				: The fantasy equivalent of a twenty-four-hour convenience 
				store is now open for business! Peruse artifacts, shop for 
				familiars and cast a spell or two at Dota's Secret Shop!""", 
				price="Free", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Keep Talking and Nobody Explodes", 
				category="Software", 
				description="""In Keep Talking and Nobody Explodes, one player 
				is trapped in a virtual room with a ticking time bomb they must 
				defuse. The other players are the "Experts" who must give the 
				instructions to defuse the bomb by deciphering the information 
				found in the bomb defusal manual. But there's a catch: the 
				experts can't see the bomb, so everyone will need to talk it 
				out - fast! Rounds are fast-paced, tense, occasionally silly, 
				and almost always loud. Everybody has a role to play whether 
				they are defusing the bomb or not. Swap out between rounds and 
				share the experience with all of your friends! Puzzle solving 
				and communication skills - and maybe a few friendships - will 
				be put to the test as players race to defuse bombs while 
				communicating quickly, clearly, and effectively.""", 
				price="$14.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Space Pirate Trainer", 
				category="Software", 
				description="""Space Pirate Trainer is the official trainer for 
				wannabe space pirates on the HTC Vive.  Remember those awesome 
				classic arcade cabinets? Imagine if those were immersive... 
				Space Pirate Trainer puts you in one of those; fighting off 
				relentless waves of droids with all the weapons and gadgets you 
				would ever need as a Space Pirate. You better dodge some of 
				those incoming lasers though, since just using your shields 
				won't get you in the top rankings. Pick up your blasters, put 
				on your sneakers, and dance your way into the Space Pirate 
				Trainer hall of fame. No real droids where harmed during the 
				creation of this game. Use your straps and stay in your VR area 
				to make sure no humans will be harmed.""", 
				price="$14.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Vanishing Realms", 
				category="Software", 
				description="""Vanishing Realms: Rite of Steel is an immersive 
				Role Playing Game designed from the ground up for Virtual 
				Reality play. Use one-to-one motion controls and movement so 
				that you are fully in control of combat. To swing, duck and 
				block, you don't hit a button, but physically move to perform 
				these actions as if you were there - because you are! Treasure 
				chests, weapon shops, a horde of undead foes, mystic writings, 
				banished gods, lost artifacts, ancient tombs and moonlit forest 
				- it's all here waiting to be discovered in a beautifully 
				hand-crafted VR realm.""", 
				price="$19.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="The Body VR", 
				category="Software", 
				description="""The Body VR is an educational virtual reality 
				experience that takes the user inside the human body. Travel 
				through the bloodstream and discover how blood cells work to 
				spread oxygen throughout the body. Enter one of the billions 
				of living cells inside our body and learn how the organelles 
				work together to fight deadly viruses.""", 
				price="Free", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Anyland", 
				category="Software", 
				description="""Anyland is an open virtual reality universe to 
				create your home, chat with others, explore & live in! Made 
				from the ground up for Vive, and shaped by all of us together. 
				Anyland is a blank canvas for your imagination with no 
				predefined stories and themes... it's up to all of us together 
				to invent the world. Build, script, share, collect, meet 
				friends, have parties, play games, watch videos, explore areas, 
				and make history in a new reality! We are two indie devs & VR 
				enthusiasts and this is our labor of love. We hope to say hi to 
				you in Anyland! If there's anything you need, let us know 
				please, and thanks for being in Anyland! """, 
				price="$11.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Waltz of the Wizard", 
				category="Software", 
				description="""Waltz of the Wizard is a virtual reality 
				experience that lets you feel what it's like to have magical 
				powers. Combine arcane ingredients into a boiling cauldron with 
				the help of an ancient spirit trapped in a human skull. Unleash 
				creative or destructive wizardry upon a fully interactive 
				virtual world. Travel to new places, finding yourself in 
				mysterious circumstances full of detail and unforgettable 
				atmosphere.""", 
				price="Free", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Portal Stories: VR", 
				category="Software", 
				description="""Portal Stories: VR is a brand new mini story set 
				in the Portal Universe. It features 10 brand new puzzles, 
				specifically designed to work using the 360 degrees room scale 
				that SteamVR offers. Inside Aperture, you'll be able to use the 
				new "Aperture Science Instant Teleportation Device" and the 
				"Aperture Science Apparatus Retrieval Tool" to solve the new 
				tests. Powered by Unreal Engine 4, Portal Stories: VR gives the 
				Aperture Science facility a whole fresh look. With new models, 
				textures, particles and more! """, 
				price="Free", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

item = product.Product(name="Zombie Training Simulator", 
				category="Software", 
				description="""Are you really ready for the zombie apocalypse? 
				Zombie Training Simulator is the dominant authority and world's 
				most advanced zombie preparation tool. We train you with real 
				world weapons, tactics and scenarios to ensure that you are well 
				equipped when the day comes. Are zombies coming on space ships? 
				Do zombies possess super powers? Will animals become zombies? 
				Nope! We've done the research on the most likely zombie 
				characteristics and are here to make sure you're prepared. 
				Train and unlock powerful weapons including pistols, shotguns 
				and machine guns. Learn the incredible zombie stopping power of 
				each weapon. See how much zombies love fresh meat, sound and 
				explosives. Combining these tactics will make you a truly 
				distinguished zombie apocalypse survivor. Play our speed tests 
				to prepare your wicked accuracy, and try survival mode to 
				practice surviving the ever increasing zombie hoards before 
				it's time to run. Our integrated global leaderboard system 
				displays your progress and capabilities around the world. Will 
				you be the first person your friends will call when the day 
				comes? When the news reports the zombies are here and your 
				friend gives you a call, "They're here. I need you," how will 
				you respond? That's right, you'll say "I'll be right over. 
				We've got this thanks to ZTS!" We hope you're as excited as we 
				are to prepare the world for the impending zombie invasion. Are 
				you truly prepared?""", 
				price="$19.99", 
				store_id=1, 
				user_id=1)
session.add(item)
session.commit()

print "Added products to database!"
