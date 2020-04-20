#    var player_name = 'Eddie Van Bonkhertz';
#    	    var player_location = 'Title Screen';
#    	    var balance = 100;
#    	    var items = ['A copy of the book true Memoirs Of a Disgraced Clown. (You are able to read it by typing "read")', 'Plush Grenade','2 Emergency Tickets to Ocean World'];
#    	    var solved_places = [];
#    	    var player_prompt = '1';
#    	    var quests = [];
#    	    var completed_quests = [];
#    	    var characters = [];
#    	    var game_over = false;
#    	    var taken_items = [];
#    	    var grenade_accomplish = [];
#    	    var omlette_accomplish = [];
#    	    var items_sold = [];
#    	    var tmdc = false;
#    	    var prompt_accomplish = [];
#    	    var prompt_accomplish2 = [];
#    	    var prompt_accomplish3 = [];
#    	    var hidden_accomplish = [];
#    	    var moon_cheese = false;
#    	    var moon_cheese_accomplish = [];
#    	    var cold_turkey = false;
#    	    var cold_turkey_accomplish = [];
#    	    var moon_cheese_cost = 0;
#    	    var death_survivability = 0;
#    	    var h2z456d = false;

# Python Text RPG
#Bonkhertz Game


import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####
class player:
	def __init__(self):
	    self.name = 'Eddie Van Bonkhertz'
	    self.location = 'Title Screen'
	    self.balance = 100
	    self.items = ['A copy of the book True Memoirs Of a Disgraced Clown. (You are able to read it by typing "read")', 'Plush Grenade','2 Emergency Tickets to Ocean World']
	    self.solved_places = {'Title Screen': True,'Gas Station': False, 'The Casino': False,'Milk Store': False,'Picracko Gallery': False,'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
	    self.prompt = '1'
	    self.quests = []
	    self.completed_quests = []
	    self.characters = []
	    self.game_over = False
	    self.taken_items = []
	    self.grenade_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House":False,}
	    self.omlette_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
	    self.items_sold = []
	    self.tmdc = False
	    self.prompt_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
	    self.prompt_accomplish2 = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
	    self.prompt_accomplish3 ={'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
	    self.hidden_accomplish ={'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
	    self.moon_cheese = False
	    self.moon_cheese_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
	    self.cold_turkey = False
	    self.cold_turkey_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
	    self.moon_cheese_cost = 0
	    self.death_survivability = 0
	    self.h2z456d = False
myPlayer = player()









### Game Function ###

def main_game_loop():
	while myPlayer.game_over == False:
		prompt_input()


if myPlayer.solved_places == {'Title Screen': True,'Gas Station': True, 'The Casino': True,'Milk Store': True,'Picracko Gallery': True,'Ocean World': True, 'Payphone': True,'Bowling Alley': True,'India': True,'REDACTED, Russia':True,}:
	myPlayer.game_over == True
	end_game()

## Places Defintion ##
HIDDEN_QUEST = 'hidden quest',
QUEST = 'active quest',
QUEST_PROMPT = 'The prompt that initiates the quest',
EXAMINATION = "examine",
EXAMINATION2 = 'examine 2'
SOLVED = 'solved',
LEFT = 'left'
RIGHT = 'right'
OUTSIDE = 'outside'
ACTIONS = '',
NEXT = 'next'
YES = 'yes'
NO = 'no'
NO2 = 'no 2'
YES2 = 'yes 2'
NO3 = 'no 3'
YES3 = 'yes 3'
PROMPT = 'prompt'
PROMPT2 = 'prompt 2'
PROMPT3 = 'prompt 3'
ADD_ITEMS = ' add items'
ADD_ITEMS2 = 'add items 2'
ADD_ITEMS3 = 'add items 3'
ITEMS = 'items'
ITEMS2 = 'items 2'
ITEMS3 = 'items 3'
HIDDENPROMPT = 'hidden prompt'
HIDDENYES = 'hidden yes'
HIDDENNO = 'hidden no'
HIDDENITEMS = 'Subtracting Items'
HIDDEN_ITEMS = 'hidden items'
HIDDEN_BALANCE = 'money for prompt'
BACK = 'back'
NEXT_PROMPT = 'next prompt'
PROMPT_AFTER = '1prompt'
PROMPT_AFTER2 = 'prompt after prompt2'
PROMPT_AFTER3 = 'prompt after prompt 3'
ADD_ITEMS3_NO = 'add items 3 no'
ITEMS3_NO = 'items 3 no'
ADD_BALANCE = 'add balance'
SUB_BALANCE = 'sub balance'
SUB_BALANCE_PROMPT = 'sub balanc prompt'
ADD_BALANCE_PROMPT = 'add balance prompt'
SUB_BALANCE_PROMPT2 = 'sub balance prompt 2'
ADD_BALANCE_PROMPT2 = 'add balance prompt 2'
ADD_BALANCE2 = 'add balance 2'
SUB_BALANCE2 = 'sub balance 2'
SUB_BALANCE_NO = 'sub balance no'
ADD_BALANCE_NO = 'add balance no'
ADD_ITEMS_PROMPT = ' which prompt add items'
ADD_ITEMS2_PROMPT = 'which prompt add items 2'
ADD_ITEMS3_PROMPT = 'which prompt add items 3'
GRENADE = 'grendae'
OMLETTE = 'omlette'
OMLETTE_ITEMS = 'items recieved from the oml command'
GRENADE_ITEMS = 'items recieved from the boom command'
GRENADE_MONEY = 'money caused by using a plush grenade'
OMLETTE_MONEY = 'Money made from shooting an omlette gun'
HIDDEN_ITEMS_NO = 'hiden no items'
HIDDEN_BALANCE_NO = 'hidden balance no'




places = { 'Title Screen': {
HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION: 'There is nothing but the title screen, smart guy.',
EXAMINATION2: '',
SOLVED: False,
LEFT: "To the left is a copy of the book 'True Memoirs of a Disgraced Clown', you pick it up.",
RIGHT:'To the right is a omlette gun. It brings back the many memories of being omletted. You try and approach it, but it nearly hits you. You do not dare touch it again, and you leave it there.',
OUTSIDE:'There is no outside, this is a title screen. Are you okay?',
ACTIONS: '',
NEXT: 'Gas Station',
YES2: '',
NO2: "",
NO: '',
YES: '',
NO3: '',
YES3: '',
PROMPT2: "",
PROMPT: '',
PROMPT3: '',
ADD_ITEMS: 'Easter Egg',
ADD_ITEMS2: '',
ADD_ITEMS3: '',
ITEMS:  '',
ITEMS2: '',
ITEMS3: '',
BACK: 'Title Screen',
HIDDENPROMPT: "Would you like to take 'Easter Egg'?",
HIDDENYES: 'Congrats! You now have an actual easter egg. What does it do? You may ask. Well, nothing, but it is very shiny.',
HIDDENNO: "No? Well you have it anyway, how about that?",
HIDDEN_ITEMS: 'Easter Egg',
HIDDENITEMS: '',
NEXT_PROMPT:  '',
PROMPT_AFTER:  '',
PROMPT_AFTER2:  '',
PROMPT_AFTER3:'',
ADD_ITEMS3_NO: '',
ITEMS3_NO:'',
ADD_BALANCE: 0,
SUB_BALANCE: 0,
ADD_BALANCE2: 0,
SUB_BALANCE2: 0,
HIDDEN_BALANCE: 0,
ADD_BALANCE_PROMPT: '',
SUB_BALANCE_PROMPT: '',
ADD_BALANCE_PROMPT2: '',
SUB_BALANCE_PROMPT2: '',
ADD_ITEMS_PROMPT:'',
ADD_ITEMS2_PROMPT:'',
ADD_ITEMS3_PROMPT:'',
GRENADE: "Oh look! you broke the title screen! Great job! Maybe don't go around chucking grenades.",
OMLETTE: "Oh look! You broke the title screen! Great job! Maybe don't shoot that whenever you feel like it.",
GRENADE_MONEY: 0,
OMLETTE_MONEY: 0,
OMLETTE_ITEMS: 'Commerative Button ',
GRENADE_ITEMS: 'Commerative Button',
HIDDEN_ITEMS_NO: 'Easter Egg',
HIDDEN_BALANCE_NO: '',


    },



    'Gas Station': {
HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION:'You are in a large gas station. Out of the corner of your eye you see a rat crawling on the floor. On the shelf behind you, you see a bag of potato chips that have been in the sun so long, the bag is a faded yellow, the words had ceased to exist. A small hot dog machine had what appeared to be an oblong rock being rotated. Upon further inspection, it was a quite moldy hot dog. There is a single lottery ticket left. You notice the penny dish had been befouled with a quarter.' + '\n',
EXAMINATION2: '',
SOLVED: False,
LEFT: 'To the left is a wall with streaks of what you hope to be molasses.'+'\n',
RIGHT: 'To the right is the door to the outside. The glass appears to be frosted, but it is in fact, a thin layer of dust.'+'\n',
OUTSIDE: 'The cars outside are speeding by. There is no traffic, and it is sunny outside.'+'\n',
ACTIONS: 'EVB',
NEXT: 'The Casino',
YES: 'You bought the ticket for $5. You used the quarter from the penny dish and scratched off the ticket, revealing that you had won $10.'+ '\n',
NO:'You decided not to buy the ticket, because gambling just is not your thing. You walked out the door into the sun light and was immediately flattened and killed by a stray car. You died. Please restart.' + '\n',
NO2: 'You decide not to go to vegas, maybe you are smarter than you look. "You were my only way to get to vegas!" Shoeburt said. They proceeded to force feed you a knife. You died. Please restart.' + '\n',
YES2: '"I will sponsor your trip to vegas! I have a good feeling about you! My name is Fred by the way." said the cashier. ',
NO3: 'You decide not to take the chips, passing up a possible hilarious moment later on. Oh well.',
YES3: "You feel the urge to take the chips. You don't know why, but you grab them. The cashier was about to scold you for stealing, but thought the chips were too old to be ingested.",
PROMPT:'Would you like to buy that lottery ticket?',
PROMPT2: 'A person comes in and asks you if you remember them. You answer no, and they introduce themselves as Shoeburt Papadopoulos. You tell them that you just won the lottery. They suggest you go to Las Vegas since you are so lucky. Do you want to go?',
PROMPT3: 'Do you want to take the potato chips?',
HIDDENPROMPT: 'You like hidden prompts, eh? Would you like a free pass to the end of the game?',
HIDDENYES: "Sike! That's just a slip of paper with 'eddievanbonkhertz.com, the official EVB Website' promoted on it, but by the way...you should probably check it out. (I also gave you $10 to buy the eventual T-shirts and other merchandise}",
HIDDENNO: 'Well, you got it anyway! Come again!',
ADD_ITEMS: 'Lottery Ticket',
ADD_ITEMS2: 'Lucky Quarter',
ADD_ITEMS3: 'Bag of Chips',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
BACK: 'Title Screen',
HIDDEN_ITEMS: "Slip of paper with 'eddievanbonkhertz.com' on it",
HIDDENITEMS: '',
NEXT_PROMPT: '2',
PROMPT_AFTER: '3',
PROMPT_AFTER2: '0',
PROMPT_AFTER3: '2',
ADD_ITEMS3_NO: '',
ITEMS3_NO:'',
HIDDEN_BALANCE: 10,
ADD_BALANCE: 5.25,
SUB_BALANCE: 0,
ADD_BALANCE2:0 ,
SUB_BALANCE2: 0,
ADD_BALANCE_PROMPT: '1',
SUB_BALANCE_PROMPT: '',
ADD_BALANCE_PROMPT2: '',
SUB_BALANCE_PROMPT2: '',
ADD_ITEMS_PROMPT:'1',
ADD_ITEMS2_PROMPT:'1',
ADD_ITEMS3_PROMPT:'3',
GRENADE: "You chuck a grenade at the blood-soaked wall, and it explodes, leaving a massive hole in the wall. You walk over and see the wall was insulated with single dollar bills. you take as many as you can when the cashier isn't looking",
OMLETTE: 'You omlette one of the cashiers named Greg in the face, he was knocked unconcious and was rushed to the nearest omlettepital. You swiped his outfit, you never know when it may help.',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 60,
OMLETTE_ITEMS: '6/11 Gas Station Uniform',
GRENADE_ITEMS: '',
HIDDEN_ITEMS_NO: "Slip of paper with 'eddievanbonkhertz.com' on it",
HIDDEN_BALANCE_NO: '',



},


'The Casino': {
HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION: 'You open the door and immediately go deaf from the sound of the machines blaring and chiming, it was probably for the best. The blackjack table looks easy to win, so you walk over there. You overhear them saying "hit" a bunch. You walk over and say "Deal me in." The dealer asks if you have any chips. You kick yourself (somehow in the head) for not getting those chips back at the gas station. You ask, "Where can I buy these chips?" They point you in direction of another table. You ask, "How much can I get for ten dollars?" You hand them the $10 from your lottery winnings, and they give you a single chip in return. ',
EXAMINATION2: 'You open the door and immediately go deaf from the sound of the machines blaring and chiming, it was probably for the best. The blackjack table looks easy to win, so you walk over there. You overhear them saying "hit" a bunch. You walk over and say "Deal me in." The dealer asks if you have any chips. You reach into your pocket and fish out the faded bag of chips and put them on the table. The dealer shruggs and deals you in.',
SOLVED: False ,
LEFT: 'To the left is a drunken man, who just won a jackpot and it jumpng up and down with excitement. It seems too much, because the next thing you see, is the same man barfing on his winnings.',
RIGHT: 'To the right is a muscular security guard at a desk. He glares at you, almost as if he is mad for you existing. You turn away, but you can still feel his eyes on you.',
OUTSIDE: 'The door outside is gaurded by 15 security guards. You think, "They are really serious about security here!"',
ACTIONS: 'EVB',
NEXT: 'Milk Store',
YES: 'You bet the lucky 10 dollars and ended up losing 80 dollars somehow.',
NO: 'You try to leave the casino, but when you walk up to the bouncers, they ask how much money you have. You answer a positive number, and they shake their heads and throw you back towards the machines. Unfortunately, they threw you too hard and yo konked out on one of the machines and never woke up. You died. Please restart.',
NO2: 'You stay in the casino and keep betting through the night. You fall asleep after many drinks. The guards find you, assume you are dead and put you in a body bag. They carry you to the nearest cliff, and toss you over. You died. Please restart. ',
YES2: "You walk towards the bouncer and you tell them how much money you had, and how much you have now. They think the amount lost to amount you have ratio is good enough, so they throw you out the doors, into a bus that had it's doors open. In the bus you slowly regain conciousness, and hearing, on your way to the Milk Store.",
NO3: "When you weren't looking, someone ate the entire bag before collapsing. You go spend $10 and bet with that. You somehow lose 80 dollars.",
YES3: 'You saved yourself 10 bucks by picking up that old bag of chips, congrats! You still lost 80 dollars though.',
PROMPT: 'Do you want to bet the $10 chip?',
PROMPT2: 'Do you want to leave the casino?',
PROMPT3: 'Do you want to bet the Bag Of Chips',
HIDDENPROMPT: 'Do you want to bet your lucky quarter?',
HIDDENYES: 'You bet your lucky quarter and won it back, along with another 25 cents. You kept doing this until you got 200 more dollars. When you tried to leave, the bouncers were going to stop you. With a sudden impulse you flicked them, and they all fell to the ground, allowing you to leave.',
HIDDENNO: "You didn't bet your lucky quarter, but congrats on finding the easter egg.",
HIDDENITEMS: '',
HIDDEN_ITEMS: '',
ITEMS: '',
ITEMS2: '',
ITEMS3: 'Bag of Chips',
ADD_ITEMS: '',
ADD_ITEMS2: '',
ADD_ITEMS3: '',
NEXT_PROMPT: '2',
PROMPT_AFTER: '2',
PROMPT_AFTER2: '0',
PROMPT_AFTER3: '2',
BACK: 'Gas Station',
ADD_ITEMS3_NO: '',
ITEMS3_NO:'',
HIDDEN_BALANCE: 200,
ADD_BALANCE: 0,
SUB_BALANCE: 90,
ADD_BALANCE2: 0,
SUB_BALANCE2: 80,
SUB_BALANCE_NO: 90,
ADD_BALANCE_NO: 0,
ADD_BALANCE_PROMPT: '-',
SUB_BALANCE_PROMPT: '1',
ADD_BALANCE_PROMPT2: '',
SUB_BALANCE_PROMPT2: '3',
ADD_ITEMS_PROMPT:'',
ADD_ITEMS2_PROMPT:'',
ADD_ITEMS3_PROMPT:'',
GRENADE: 'You walk to the corner of the casio and open your pack. You grab the plush grenade and squeeze it to activate it. You chuck it towards the blackjack table. It explodes, sending the machines in a 20 foot vacinity flying into the air. They start leaking money as they shoot accross the room. You scoop up 200 dollars before cashing them out and walking away from the incident. ',
OMLETTE: 'You pull the gun out of your pack and shoot a coin machine wth an omlette. It starts leaking money. You scoop up 100 dollars before cashing them and walking away from the incident. ',
GRENADE_MONEY: 200,
OMLETTE_MONEY: 100,
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: '',
OMLETTE_ITEMS: '',
GRENADE_ITEMS: '',



    },

'Milk Store': {
HIDDEN_QUEST: '',
QUEST: 'Get Milk',
QUEST_PROMPT: '1',
EXAMINATION: 'You step through the door. There is a wall of refrigerators across the aisle. Five aisles are lined up, leading to the fridge wall, with the checkout to the left.',
EXAMINATION2: '',
SOLVED: False,
LEFT: 'To the left is a man with a mask and gun in the hostage section. ',
RIGHT: 'To the right is a display of cranberry sauce that is leaking chunky blood. ',
OUTSIDE: 'Outside is are broken down cars, toxic car fumes, and everything you have come to love in the state of [REDACTED]. ',
ACTIONS: '',
NEXT: 'Picracko Gallery',
YES: '',
NO: '',
NO2: 'You gave up on trying to find your friend/crazed artist? You should be ashamed. How about you try it again after anice restart.',
YES2: 'You have just accepted a new responsibility, find Picracko, world famous crazed artist and drugged friend.',
NO3: '',
YES3: '',
PROMPT: 'Do you want to go to the dairy section, the produce section, or the hostage section?',
PROMPT2: 'You check the label on the milk and see a missing person label on the side. When you look at it closer, a memory comes flooding back of a friend called Picracko. You see that it was Picracko that was on the carton! Where could he be? You think to yourself. Suddenly you have another flashback.'+'\n Do you want to go to The Picracko Gallery?',
PROMPT3: '',
ADD_ITEMS: '',
ADD_ITEMS2: '',
ADD_ITEMS3: '',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: "Missed the chance to get Stalin's Hair? No problem. I got a snipped of his 'stache when I was in the war. Do you want it?",
HIDDENYES: '',
HIDDENNO: "What?! You don't want random hair taken from a dictator's mustache offered to you buy a voiceover that is just text? Fine. You missed out though.",
HIDDENITEMS: '',
HIDDEN_ITEMS: "Stalin's Hair",
BACK: 'The Casino',
NEXT_PROMPT: '2',
PROMPT_AFTER: '2',
PROMPT_AFTER2: '0',
PROMPT_AFTER3: '',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: '',
SUB_BALANCE: '',
HIDDEN_BALANCE: '',
SUB_BALANCE_PROMPT: '',
ADD_BALANCE_PROMPT: '',
SUB_BALANCE_PROMPT2:'',
ADD_BALANCE_PROMPT2: '',
ADD_BALANCE2: '',
SUB_BALANCE2: '',
SUB_BALANCE_NO: '',
ADD_BALANCE_NO: '',
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You chuck a grenade in the vicinity of the hostage section. You hear screams, and see a wallet launch into the air. You catch it and find 1000 dollars in it. ',
OMLETTE: 'You use your omletting gun and omlette the dairy isle which for some reason ncontained a bunch of guns. Those guns went flying into the air directly into the hand of the hostages, who were now the terrorists, holdiing the terrorist hostage. Weird.',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 1000,
OMLETTE_ITEMS: '',
GRENADE_ITEMS: '',
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: '',



},





'Picracko Gallery': {
HIDDEN_QUEST: '',
QUEST: 'Find Picracko',
QUEST_PROMPT: '1',
EXAMINATION: 'You had never been in an art gallery before. It was unsuprisingly empty. You glance around at the paintings and recoil. They were horrendous, almost purposely. You decided that you need to buy one. Coincidentally, the Picracko Original just magically appeared in the store for an absurd amount of money. You decide to serach the gallery.',
EXAMINATION2: '',
SOLVED: False,
LEFT: 'To the left is a security gaurd fast asleep, hugging his baton and snoring.',
RIGHT: 'To the right is a wall of paintings (some with music), so wretched you hurl on the floor. ',
OUTSIDE: "Outside is the sun, like always. The outside is not that interesting. It's pretty much the same all the time. Not sure why you keep using this command.",
ACTIONS: '',
NEXT: 'Ocean World',
YES2: 'Since all the visitors are barfing into the designated barf drains, you steal one easily and replace it with a splatter of pasta sauce. No one noticed for a year. Behind the painting, you found a hole in the wall. I contained 40 dollars and a Paintbrush. You throw the painting on the ground, and take the paintbrush instead.',
NO2: "You decide not to steal a painting. You turn around to leave and at that exact moment, you were hit in the back of the head by the painting that you didn't steal, apparently it was not hung very well. You died.",
NO: '',
YES: '',
YES3: 'You leave the pricracko gallery and ask a homeless man if he has a lighter. He nods and hands it to you, You realize you had one cigar left. You douse it in a puddle of gasoline and light it, before putting it in your mouth. Sadly, you put it in flame first, and it had ignited you. You died. Please restart.',
NO3: 'You stay in the gallery and fall asleep on a bench. You feel someone tap your shoulder. When you look to see who it is, you find that it is Picracko! You tell him that he should join you on your epic quest, but they should go someone fun first. He suggests Ocean World. You pull the emergency Ocean World ickets that you keep in your backpack and hand one of them to him. You both board the next bus to wherever Ocean World is. ',
PROMPT: 'Do you want to go to the left wing or the right wing?',
PROMPT2: '\n'+'Do you want to steal a painting?',
PROMPT3: 'Do you want to leave?',
ADD_ITEMS: '',
ADD_ITEMS2: 'Paintbrush',
ADD_ITEMS3: '',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: 'Do you want a FREE Picracko Original?',
HIDDENYES: 'Sucker! This will teach you not every hidden prompt is a good one! Minus 50 dollars.',
HIDDENNO: "You get it anyway, it is one of the ugliest art pieces ever produced. It's a mirror with a signature. ",
HIDDENITEMS: '',
HIDDEN_ITEMS: '',
BACK: 'Milk Store',
NEXT_PROMPT: '3',
PROMPT_AFTER: '2',
PROMPT_AFTER2: '3',
PROMPT_AFTER3: '0',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: 20,
SUB_BALANCE: '',
HIDDEN_BALANCE: '',
SUB_BALANCE_PROMPT: '',
ADD_BALANCE_PROMPT: '2',
SUB_BALANCE_PROMPT2:'',
ADD_BALANCE_PROMPT2: '',
ADD_BALANCE2: '',
SUB_BALANCE2: '',
SUB_BALANCE_NO: '',
ADD_BALANCE_NO: '',
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You chuck the granade into the right wing and hear screams. You proceed to steal a couple paintings and put them in your pack, while the gaurds were distracted. One of them spontaneously exloded in your bag, and lit it on fire. You were caught for the art destruction and was charged for the paintings. Thankfully, no one liked them, so it only cost you 5 bucks.',
OMLETTE: 'You omlette the security gaurd, ready to steal some paintings, but he appeared to be trained in omlette attacks, because he un-hinged his jaw and ate the omlette whole. Mortified, you run in the opposite direction, and konk yourself out on a metal sculpture, and wake up in the same place, with the security gaurd gone. Weird. ',
OMLETTE_MONEY: 0,
GRENADE_MONEY: -5,
OMLETTE_ITEMS: '',
GRENADE_ITEMS: '',
HIDDEN_ITEMS_NO: 'Picracko Mirror',
HIDDEN_BALANCE_NO: -50,







    },


'Ocean World': {
HIDDEN_QUEST: '',
QUEST: "Who's Leg is This?",
QUEST_PROMPT: '2',
EXAMINATION: 'You are now at the Ocean World Entrance! Ready to see the sea...of animals. People laughed when you got emergency Ocean World tickets, well where are they now? Probably not at Ocean World. You walk over to the entrance. You see a worker gathering tickets. ',
EXAMINATION2: '',
SOLVED: False,
LEFT: "To the left is a line of people angirly staring at you because you haven't moved in a while.",
RIGHT: 'To the right is the parking lot, not sure why you are outside.',
OUTSIDE: "You know that I have to write these Right? hehe...right write. If you want to know what it is like outside, go outside, but not before buying some EVB, TMDC merchandise (may or may not be) available at eddievanbonkhertz.com!",
ACTIONS: '',
NEXT: 'Payphone',
YES2: 'That was the right choice. You decide to call your old friend Shoeburt and ask who they think would be the best leg candidate.',
NO2: "You decide to rest instead of going to find a new leg, when all of a sudden, your leg starts bleeding at an incredible litre per second. You died. ",
NO: "You decide to save the tickets for a sunny day. You put them in your pocket, but get robbed and give them the tickets. Ticketless, you start living in an alleyway, you die there many years later, but that's too boring, lets restart now!",
YES: 'You hand them the tickets and you and Picracko walk into the most wonderous place on earth, Ocean World! You check the map to decide where to go first.',
NO3: '',
YES3: '',
PROMPT: 'Do you want to give hand them the emergency tickets?',
PROMPT3: 'Do you want to go to the shark section, or the harmless fish section?',
PROMPT2: 'Would you like to go on a quest to get a new leg?',
ADD_ITEMS: '',
ADD_ITEMS2: '',
ADD_ITEMS3: '',
ITEMS: '2 Emergency Tickets to Ocean World',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: "...Uh, by the way, if you want a good tip, give me 5 bucks and I'll tell you.......Do you wanna give me 5 bucks?",
HIDDENYES: "Alright, I'm not supposed to tell you this...(Disregard the fact that I was coded to tell you this)... but all of the people you can take a leg from can be summond. Here, this will help you summon one of them...",
HIDDENNO: "",
HIDDENITEMS: '',
HIDDEN_ITEMS: 'Family Photo that contains James',
BACK: 'Picracko Gallery',
NEXT_PROMPT: '2',
PROMPT_AFTER: '3',
PROMPT_AFTER2: '2',
PROMPT_AFTER3: '0',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: 0,
SUB_BALANCE: 0,
HIDDEN_BALANCE: -5,
SUB_BALANCE_PROMPT: 0,
ADD_BALANCE_PROMPT: 0,
SUB_BALANCE_PROMPT2: 0,
ADD_BALANCE_PROMPT2: 0,
ADD_BALANCE2: 0,
SUB_BALANCE2: 0,
SUB_BALANCE_NO: 0,
ADD_BALANCE_NO: 0,
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You chuck a grenade into one of the tanks and it shatters the glass, sending a big chunk into the gift shop. While they were distracted, you grabbed some merchandise. ',
OMLETTE: 'You grab the omlerting gun out of your backpack to no alarm, and load it. You choose your target, and finally shoot it into the sky. After that, you forget about it and walk around for 30 minutes. Then you see it come careening down like a meteorite, hitting the First Bank of Ocean World, sending Ocean Bucks into the air. You grab a couple.',
OMLETTE_ITEMS: '22 Ocean Bucks',
GRENADE_ITEMS: 'Ocean World T-Shirt',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 0,
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: 0,












    },

'Payphone': {


HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION: 'You look around the phone booth. It has half a phone book on a string, the phone, windows, and a mysterious keypad that said "James Bond" on it. You decide to call someone to get some consulting about where to find a leg. ',
EXAMINATION2: '',
LEFT: "To the left is the wall of the payphone, the part that isn't glass is covered in phone numbers.",
RIGHT: 'To the right is the other wall of the payphone with Picracko looking at his watch.',
OUTSIDE: "To the outside is a street and the hospital you just came from.",
ACTIONS: '',
NEXT: '',
YES2: '',
NO2: "",
NO: '',
YES: '',
NO3: "Oh, okay. It's just that why wouldn't you want a free item, seems weird.",
YES3: 'You take the rest of the Phonebook in case you need it later.',
PROMPT: 'Do you want to call Picracko, Fuick, Shoeburt, Gerbils, or Eddie?',
PROMPT2: 'Do you want to go to the bowling alley, [REDACTED] Russia, or India?',
PROMPT3: ' You were about to leave when you notice the half a phonebook still there. \n Do you want to grab the rest of the phone book?',
ADD_ITEMS: '',
ADD_ITEMS2: '',
ADD_ITEMS3: 'Half a Phonebook',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: "Do you want to type EVB into the keypad.",
HIDDENYES: "You type EVB into the keypad and it opens up a tube in the wall. Inside is 2100 Dollars, and a mint tin that says 'Cover It With Grass'.",
HIDDENNO: "You decide not to do it, what would come of it anyway, just disappointment.",
HIDDENITEMS: '',
HIDDEN_ITEMS: 'Cover It With Grass mint tin',
BACK: 'Ocean World',
NEXT_PROMPT: '',
PROMPT_AFTER: '3',
PROMPT_AFTER2: '2',
PROMPT_AFTER3: '0',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: 0,
SUB_BALANCE: 0,
HIDDEN_BALANCE: 0,
SUB_BALANCE_PROMPT: 0,
ADD_BALANCE_PROMPT: 0,
SUB_BALANCE_PROMPT2: 0,
ADD_BALANCE_PROMPT2: 0,
ADD_BALANCE2: 0,
SUB_BALANCE2: 0,
SUB_BALANCE_NO: 0,
ADD_BALANCE_NO: 0,
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You are not very smart. You chuck a grenade into the booth, remember you are supposed to call someone, and walk back in. The grenade shattered you and the booth much to the horror of Picracko who was nearby. You died.',
OMLETTE: "You pull out the gun while in the booth, and shoot the glass, it must've been bullet proof or something because the omlette ricocheted off the glass and hit you right in your chest, dislodging your spleen and sending it into your lungs. You died",
OMLETTE_ITEMS: '',
GRENADE_ITEMS: '',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 0,
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: 0,
HIDDEN_BALANCE: 2100,
















    },


'India': {
    HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION: 'You look around, you are now in a country with over a billion people, and you only know half of them personally. You talk around and try to see if anyone famous was from India. You here talk about a guy who starved himself and saved the country, Gandhi. You ask around about what he did, and apparently what he did was protest by not eating and he aslo prayed. Not eating and being on your knees are two things you are a pro at.',
EXAMINATION2: '',
SOLVED: '',
LEFT: 'To the left is whatever is left of India, Pakistan I think.',
RIGHT: "To the right is whatever is right of India, I think it's Bangladesh.",
OUTSIDE: "You are outside.",
ACTIONS: '',
NEXT: "Ghandi's House",
YES2: "You decide to take a very rocky cab to Gandhi's house. It is concrete and very unappealing. You decide to go in and find YOUR rightful leg.",
NO2: "You decide not to go to gandhi's house and try to ind a leg elsewhere, ut found no suitable donors. You collapsed on a boat which then drifted you to Greece, where you ate so much food, that your own body crushed your lungs. You died.",
NO: 'You decide not to fast, and instead grab a burger. You are then trampled by a group of vegan hippies led by a man named Pascal. You died.',
YES: "You start fasting in the middle of the sidewalk and soon gathera crowd. Some ask what you are protesting. You don't really know. After about 20 minutes you start feeling really hungry, and there hasn't been a vision about Gandhiyet. Next to you i a cart selling Chilli Dogs. I'm sure Gandhi wouldn't mind...",
NO3: 'Good choice, you stay away from the enticing food. You keep starving yourself and see a vision appear. It was Gandhi. He spoke to you, "To find what you seek, you must visit my childhood home." He then went to get a chili dog.',
YES3: "You break your starvation by eating a chili dog. It must have been tainted though because your stomach starts to feel ill. You later collapse, never onvce getting to have Gandhi's leg. You died.",
PROMPT: 'Would you like to protest by fasting?',
PROMPT2: "Do you want to go to Gandhi's home?",
PROMPT3: 'Do you want to grab a chili dog?',
ADD_ITEMS: '',
ADD_ITEMS2: '',
ADD_ITEMS3: '',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: '',
HIDDENYES: '',
HIDDENNO: "",
HIDDENITEMS: '',
HIDDEN_ITEMS: '',
BACK: 'Payphone',
NEXT_PROMPT: '2',
PROMPT_AFTER: '3',
PROMPT_AFTER2: '2',
PROMPT_AFTER3: '0',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: 0,
SUB_BALANCE: 0,
HIDDEN_BALANCE: 0,
SUB_BALANCE_PROMPT: 0,
ADD_BALANCE_PROMPT: 0,
SUB_BALANCE_PROMPT2: 0,
ADD_BALANCE_PROMPT2: 0,
ADD_BALANCE2: 0,
SUB_BALANCE2: 0,
SUB_BALANCE_NO: 0,
ADD_BALANCE_NO: 0,
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You chuck a grenade and turn the other way. You hear screams and a loud moo. You catch a piece of flaming cow, its well done. You are chased out of the continent, where you finish eating the steak. You get food poisioning and died. You died.',
OMLETTE: 'You omlette a cow, and it is knocked over cold. You are chased around the continent before being beaten by a a horde of cows. You died.',
OMLETTE_ITEMS: '',
GRENADE_ITEMS: '',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 0,
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: 0,
HIDDEN_BALANCE: 0,
















    },


'Bowling Alley': {

    HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION: 'You hear chimes and low bowling noises. You try to find a good leg candidate. You find a good leg donor and try to befriend them. You walk over and introduce yourself. You learn his name is Jeff. You decided not to come on strong, dont ask him for his leg just yet. He offers to bowl with you.',
EXAMINATION2: '',
LEFT: 'To the left is a bunch of alleys.',
RIGHT: 'To the right is more alleys.',
OUTSIDE: "Outside is a bar, you make a mental note to head there soon.",
ACTIONS: '',
NEXT: "Jeff's House",
YES2: "You decide to go to Jeff's house, after all who can refuse swimming and hockey in the air. That's a deal you don't get very often.",
NO2: "You tell Jeff that you can't go to hi house. Jeff's happy expression turns to sadness. He starts crying. He starts taking about the death of his wife, his adopted son James. You feel so bad, you decide to leave the alley. Before you leave, you spot a claw machine and try to test your luck. You try and fail for hours on end. Before you leave you pound the machine in anger. It wobbles before toppling over and crushing you. You died.",
NO: 'You decide not to bowl with Jeff, when all of a sudden a bowling ball came in fast from thhe left, hitting your face directly. It crushes your skull and squeezes your brain. You died.',
YES: 'You agree to his bowling offer, and grab a ball. You play the round of bowling and get a score of 0. You were getting really good at gutterballs, it was now your signature move. Jeff suggests that they rest for a bit and eat some food. You are given a menu, which you pocket. Jeff suggests getting the Nacho Supreme and sharing it.',
NO3: "You take one look a the plastic cheese-like substitute and decide not to ingest this poison. You tell Jeff you aren't hungry. He tells you all about his game room in his basement, which has a full pool table as well as an air hocky table.",
YES3: 'You eat the Bowling Alley Nachos and feel immediately sick. The cheese-like substance was awful. You excuse yourself to the bathroom and vomit for 15 minutes. You return to chat with Jeff. He tells you all about his game room in his basement, which has a full pool table as well as an air hocky table. Your death survivability has gone down.',
PROMPT: 'Do you want to bowl with Jeff?',
PROMPT2: "Do you want to go Jeff's house?",
PROMPT3: 'Do you want to eat some bowling alley nachos?',
ADD_ITEMS: '',
ADD_ITEMS2: '',
ADD_ITEMS3: '',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: '',
HIDDENYES: '',
HIDDENNO: "",
HIDDENITEMS: '',
HIDDEN_ITEMS: '',
BACK: 'Payphone',
NEXT_PROMPT: '2',
PROMPT_AFTER: '3',
PROMPT_AFTER2: '2',
PROMPT_AFTER3: '0',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: 0,
SUB_BALANCE: 0,
HIDDEN_BALANCE: 0,
SUB_BALANCE_PROMPT: 0,
ADD_BALANCE_PROMPT: 0,
SUB_BALANCE_PROMPT2: 0,
ADD_BALANCE_PROMPT2: 0,
ADD_BALANCE2: 0,
SUB_BALANCE2: 0,
SUB_BALANCE_NO: 0,
ADD_BALANCE_NO: 0,
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You bowl the grenade down an alley and get a perfect strike. It then explodes and sends a shock wave through the alley, getting a strike in every alley. You are awarded a Bowling Participation Trophy, which you feel is a little underwhelming.',
OMLETTE: "You take the omletting gun and shoot the claw machine glass. It must've been bulletproof or something, because the omlette ricocheted off the glass, nearly hitting some bowlers, then bowled a perfect strike. You get a participation balloon.",
OMLETTE_ITEMS: 'Bowling Participation Balloon',
GRENADE_ITEMS: 'Bowling Participation Trophy',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 0,
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: 0,
HIDDEN_BALANCE: 0,



























    },


'REDACTED, Russia': {


HIDDEN_QUEST: '',
QUEST: '',
QUEST_PROMPT: '',
EXAMINATION: "You look around in the icy snow, you see a very colorful temple that says Russia Bonkhertzyism Church. You'll have to check it out later. You ask around about if there were any famous russians. Someone mentions a guy called Stalin. Stalin, Stalin, you remember that name. From where? Now you remeber, it was from the 'How to Escape Russia' book that was written by Stalin. He must be a cool guy, you wonder if he had a leg. A Stalin impersonator is readng excerpts from the Communist Manifesto. He has a tip hat out on the ground. ",
EXAMINATION2: '',
LEFT: 'To the left is a car driving a man. Things really are weird here.',
RIGHT: 'To the right is a Stalin look-alike breakdancing.',
OUTSIDE: "You are outside and it is very cold. All the buildings are Stalin-shaped. You have found your soul-place.",
ACTIONS: '',
NEXT: 'KGB Headquarters',
YES2: "You grab lenin's jacket from the display case and pocket it. You try ti put it on, but you accidentally rip the jacket and a sheet of paper fell out. It reads, 'The Stalin you seek is at the KGB headquarters next door. -Lenin'. You go next door to the KGB Headquarters. ",
NO2: "You decide not to take the jacket, and Stalin's ghost appears before you, shakes its head and kills you. You died.",
NO3: 'You decide not to go into the Leni Mausoleum, but just then, Sputnik, the first man made satellite comes out of orbit(launched by the U.S.S.R) and hit you in the head, you died.',
YES3: "You walk over to the red building and eneter, you see a lot of artifacts and plaques. You notice Lenin's jacket in a glass case. It looks comfortable, and about your size...",
NO: 'You look at the Stalin impersonator and decide not to pay him, because his mustache was sub-par. He notices you looking and says, "You going to pay?" You shake your head a leave. He whistles and a group of KGB impersonators surround you and beat you. You died.',
YES: 'You pay the Stalin impersonator and ask him where you should go. He asks if you are a fan of communism, you say yes. He tells you to go to the Lenin Mausoleum and points to a red building next door.',
PROMPT3: 'Do you want to go to the Lenin Mausoleum?',
PROMPT2: "Do you want to steal Lenin's jacket?",
PROMPT: 'Do you want to pay the Stalin impersonator 5 dollars?',
ADD_ITEMS: '',
ADD_ITEMS2: "Lenin's Jacket",
ADD_ITEMS3: '',
ITEMS: '',
ITEMS2: '',
ITEMS3: '',
HIDDENPROMPT: 'Do you want a free T-Shirt?',
HIDDENYES: 'Stop believing all these hidden prompts. Minus 60 Dollars. Here you have learned yourself a lesson.',
HIDDENNO: "Good choice. Back to the game...",
HIDDENITEMS: 'Learned Lesson',
HIDDEN_ITEMS: '',
BACK: 'Payphone',
NEXT_PROMPT: '2',
PROMPT_AFTER: '3',
PROMPT_AFTER2: '2',
PROMPT_AFTER3: '0',
ADD_ITEMS3_NO: '',
ITEMS3_NO: '',
ADD_BALANCE: 0,
SUB_BALANCE: 5,
SUB_BALANCE_PROMPT: '1',
ADD_BALANCE_PROMPT: '',
SUB_BALANCE_PROMPT2: '',
ADD_BALANCE_PROMPT2: '',
ADD_BALANCE2: 0,
SUB_BALANCE2: 0,
SUB_BALANCE_NO: 0,
ADD_BALANCE_NO: 0,
ADD_ITEMS_PROMPT: '',
ADD_ITEMS2_PROMPT: '',
ADD_ITEMS3_PROMPT: '',
GRENADE: 'You chuck a grenade in the sky with all your strength and seconds later, you see a giant metal skyscraper explode. A piece of melted glass comes flying at you. It says "Mercury City Tow-" I wonder what it was trying to say.',
OMLETTE: "You blinly spin in circles, stopping at a location and shooting. You see a giant red memoirial that says something about Leni explode. Stalin's ghost appears before you and nods. You notice a piece of paper floating from the blast. You grab it, it is a 'Lenin Buck'. It could be worth a lot.",
OMLETTE_ITEMS: 'Piece of Molten Glass',
GRENADE_ITEMS: 'Flaming Piece of Castle',
OMLETTE_MONEY: 0,
GRENADE_MONEY: 0,
HIDDEN_ITEMS_NO: '',
HIDDEN_BALANCE_NO: 0,
HIDDEN_BALANCE: -60,
















    }





}


## DEFINITION SECTION ##


def player_balance_no():


    if places[myPlayer.location][ADD_BALANCE_NO] != 0:
        myPlayer.balance = places[myPlayer.location][ADD_BALANCE_NO] + myPlayer.balance
        print('You now have ' + str(myPlayer.balance) + 'Dollars.')
    variable_prompt = places[myPlayer.location][PROMPT_AFTER]
    if variable_prompt != '':
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()

def player_balance_sub_no():

    if places[myPlayer.location][SUB_BALANCE_NO] != 0:
        myPlayer.balance = myPlayer.balance - places[myPlayer.location][SUB_BALANCE_NO]
        print('You now have ' + str(myPlayer.balance) + ' .')
    variable_prompt = places[myPlayer.location][PROMPT_AFTER]
    if variable_prompt != '':
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()






def player_balance():
    if places[myPlayer.location][ADD_BALANCE] != 0:
        myPlayer.balance = places[myPlayer.location][ADD_BALANCE] + myPlayer.balance
        print('\n'+'You now have ' + str(myPlayer.balance) + ' Dollars.')
    variable_prompt = places[myPlayer.location][PROMPT_AFTER]
    if variable_prompt == '':
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()

def player_balance_sub():

    if places[myPlayer.location][SUB_BALANCE] != 0:
        myPlayer.balance = myPlayer.balance - places[myPlayer.location][SUB_BALANCE]
        print('\n' + 'You now have ' + str(myPlayer.balance) + ' Dollars.')
    variable_prompt = places[myPlayer.location][PROMPT_AFTER]
    if variable_prompt != '':
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()

def player_balance2():


    if places[myPlayer.location][ADD_BALANCE2] != 0:
        myPlayer.balance = places[myPlayer.location][ADD_BALANCE2] + myPlayer.balance
        print('\n'+'You now have ' + str(myPlayer.balance) + ' Dollars.')
    variable_prompt = places[myPlayer.location][PROMPT_AFTER]
    if variable_prompt != '':
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()

def player_balance_sub2():

    if places[myPlayer.location][SUB_BALANCE2] != 0:
        myPlayer.balance = myPlayer.balance - places[myPlayer.location][SUB_BALANCE2]
        print('\n'+'You now have ' + str(myPlayer.balance) + ' Dollars.')
    variable_prompt = places[myPlayer.location][PROMPT_AFTER]
    if variable_prompt != '':
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()





def boom_balance():
    grenade_money = places[myPlayer.location][GRENADE_MONEY]
    if places[myPlayer.location][GRENADE_MONEY] != 0:
        myPlayer.balance = grenade_money + myPlayer.balance
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
    else:
        print()



def omlette_balance():
    omlette_money = places[myPlayer.location][OMLETTE_MONEY]
    if places[myPlayer.location][OMLETTE_MONEY] != 0:
        myPlayer.balance = omlette_money + myPlayer.balance
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
    prompt_input()












def print_balance():
	print('\n'+ ('#' * (12 + len(str(myPlayer.balance)))))
	print('# '+ str(myPlayer.balance) +' Dollars #')
	print(('#' * (12 + len(str(myPlayer.balance)))))
	prompt_input()












def print_location():
	print('\n'+ ('#' * (4 + len(myPlayer.location))))
	print('# ' + myPlayer.location + ' #')
	print(('#' * (4 + len(myPlayer.location))))
	prompt_input()
def casino_look():
    casino_descriptions = places['The Casino'][EXAMINATION2]
    if 'Bag of Chips' in myPlayer.items:
        places[myPlayer.location][SOLVED] = True
        for character in casino_descriptions:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        prompt3()
    else:
        player_look()


def player_read():
    print("You flip through the holy pages with the spine in your hand (you don't know who's) and land on a random page...")
    EVB_generator = random.choice(EVB)
    for character in EVB_generator:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.02)
    prompt_input()


def player_look():
	place_descriptions = places[myPlayer.location][EXAMINATION]
	for character in place_descriptions:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.02)
	myPlayer.solved_places[myPlayer.location] = True
	places[myPlayer.location][SOLVED] = True
	prompt()

def player_left():
	left_descriptions = places[myPlayer.location][LEFT]
	for character in left_descriptions:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.02)
	prompt_input()
def player_right():
	right_descriptions = places[myPlayer.location][RIGHT]
	for character in right_descriptions:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.02)
	prompt_input()




def restart(restart_time):
    time.sleep(restart_time)
    myPlayer.items = ['A copy of the book True Memoirs Of a Disgraced Clown. (You are able to read it by typing "read")', 'Plush Grenade', '2 Emergency Tickets to Ocean World']
    myPlayer.location = 'Title Screen'
    myPlayer.balance = 100
    myPlayer.quests = []
    myPlayer.name = 'Eddie Van Bonkhertz'
    myPlayer.solved_places = {'Title Screen': True,'Gas Station': False, 'The Casino': False,'Milk Store': False,'Picracko Gallery': False,'Ocean World': False,'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
    myPlayer.prompt = '1'
    myPlayer.quests = []
    myPlayer.omlettes = 0
    myPlayer.taken_items = []
    myPlayer.grenades = 1
    myPlayer.completed_quests = []
    myPlayer.characters = []
    myPlayer.items_sold = []
    myPlayer.game_over = False
    myPlayer.tmdc = False
    myPlayer.omlette_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
    myPlayer.grenade_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
    myPlayer.prompt_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
    myPlayer.prompt_accomplish2 = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
    myPlayer.prompt_accomplish3 ={'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
    myPlayer.hidden_accomplish ={'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
    myPlayer.moon_cheese = False
    myPlayer.moon_cheese_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House" :False,}
    myPlayer.cold_turkey = False
    myPlayer.cold_turkey_accomplish = {'Title Screen': False,'Gas Station': False,'The Casino': False,'Milk Store': False,'Picracko Gallery': False, 'Ocean World': False, 'Payphone': False,'Bowling Alley': False,'India': False,'REDACTED, Russia':False,'KGB Headquarters': False,"Jeff's House": False,"Gandhi's House": False,}
    myPlayer.moon_cheese_cost = 0
    myPlayer.death_survivability = 0
    myPlayer.h2z456d = False
    title_screen()







def end_game():
    os.system('clear')
    print("----------------------------------------")
    print("' You have finished the EVB Text Game! '")
    print("'--------------------------------------'")
    print("'      What would you like to do?      '")
    print("'--------------------------------------'")
    print("'              - Restart -             '")
    print("'           - Keep Playing -           '")
    print("'               - Quit -               '")
    print("'     Copyright 2019 EVB Publishing    '")
    print('\n'+'You have a new objective completed: Game Finished')
    #myPlayer.quests.remove('Game Finished')





def restart_game():
    print( '\n' +'Are you sure you want to restart?')
    output = input('> ')
    if output in ['y','yes']:
        restart(0)
    else: print('The game was not restarted.')
    prompt_input()

def print_outside():
    print(places[myPlayer.location][OUTSIDE])
    prompt_input()

def player_back():
    myPlayer.location = places[myPlayer.location][BACK]
    print('You are now back at '+ myPlayer.location + ', and everyone there is very puzzled about your oddly timed return.')
    if 'Broken dune-Buggy' in myPlayer.items:
        myPlayer.items.remove('Broken Dune-Buggy')
        myPlayer.items.append('Useless Dune-Buggy')
        myPlayer.taken_items.append('Useless Dune-Buggy')
        print("Your Broken dune buggy has turned into a Useless Dune-Buggy.")
        prompt_input()
    prompt_input()


def player_next():
    myPlayer.location = places[myPlayer.location][NEXT]
    if "Emu" in myPlayer.items:
        print('You are now at '+ myPlayer.location + ', and everyone there is very puzzled about your dramatic, slo-mo entrance on an emu. ')
        if places[myPlayer.location][QUEST] not in myPlayer.completed_quests:
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
            prompt_input()
    elif "Clown Car" in myPlayer.items:
        print('You are now at '+ myPlayer.location + ', and everyone there is in fear after you dramtically crashed your Clown Car into the ' + myPlayer.location + ' . ')
        if places[myPlayer.location][QUEST] not in myPlayer.completed_quests:
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
            prompt_input()
    elif ['KGB Army','KGB Platoon', 'KGB Horde'] in myPlayer.items:
        print('You are now at '+ myPlayer.location + ', and everyone there is in awe of the group of KGB Officers dramatically carrying you and Stalin into ' + myPlayer.location + ' . ')
        if places[myPlayer.location][QUEST] not in myPlayer.completed_quests:
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
            prompt_input()
    elif "Sailboat" in myPlayer.items:
        print('You are now at '+ myPlayer.location + ', and everyone there is very suprised that you arrived at ' + myPlayer.location + ' in a sailboat with a small child at the helm, especially since you had to go over the land to get there.. ')
        if places[myPlayer.location][QUEST] not in myPlayer.completed_quests:
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
            prompt_input()
    if myPlayer.location == "Payphone":
        payphone_next = input("Would you like to go to the bowling alley, india, or REDACTED?")
        if payphone_next == "bowling alley":
            print("You are now in Bowling Alley.")
            myPlayer.location = "Bowling Alley"
            prompt_input()
        if payphone_next == "india":
            print("You are now in India.")
            myPlayer.location = "India"
            prompt_input()
        if payphone_next == "redacted":
            print("You are now in REDACTED, Russia.")
            myPlayer.location = "REDACTED, Russia"
            prompt_input()
        while payphone_next not in ["india","bowling alley","redacted"]:
            print("That is not one of the three options.")
            payphone_next = input("Would you like to go to the bowling alley, india, or REDACTED?")
            if payphone_next == "bowling alley":
                print("You are now in Bowling Alley.")
                myPlayer.location = "Bowling Alley"
                prompt_input()
            if payphone_next == "india":
                print("You are now in India.")
                myPlayer.location = "India"
                prompt_input()
            if payphone_next == "redacted":
                print("You are now in REDACTED, Russia.")
                myPlayer.location = "REDACTED, Russia"
                prompt_input()
    print("You don't have access to this command.")
    prompt_input()
















def store_input():
    action = input('\n' +'> ')
    if action.lower() == 'quit':
        prompt_input()
    elif action.lower() == 'help':
        help_store_menu()
    elif action.lower() == 'buy':
        player_buy()
    elif action.lower() == 'sell':
        player_sell()
    elif action.lower() == 'bal':
        print('\n'+ ('#' * (12 + len(str(myPlayer.balance)))))
        print('# '+ str(myPlayer.balance) +' Dollars #')
        print(('#' * (12 + len(str(myPlayer.balance)))))
        store_input()
    elif action.lower() == 'items':
        items_print()
        store_input()
    while action.lower() not in ['items','sell','bal','buy','quit','help']:
        print('Unknown command. You are still in the store, if you need a list of actions type help.')
        store_input()
    store_input()






def player_sell():
    if myPlayer.items == []:
        print('You have no items.')
        sell_input()
    else:
        print('You have ' + str(len(myPlayer.items)) + ' item(s): ' + ', '.join(myPlayer.items))
        sell_input()
    prompt_input()






def sell_input():
    action = input('What would you like to sell?' + '\n' + '> ')
    if action.lower() == 'quit':
        print('You have exited the store, back to the story')
        prompt_input()
    elif action.lower() == 'book':
        print("You can't sell this. Why would you want to? It's the ultimate advice book.")
        sell_input()
    elif action.lower == 'true memoirs of a disgraced clown':
        print("You can't sell this. Why would you want to? It's the ultimate advice book.")
        sell_input()
    elif action.lower() == 'easter egg':
        print('You want to sell your one of a kind shiny egg? Fine, here you go...')
        myPlayer.balance = myPlayer.balance + 1000
        print('Wow that egg was worth a lot!')
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
        myPlayer.items.remove('Easter Egg')
        myPlayer.items_sold.append('Easter Egg')
        sell_input()
    elif action.lower() == 'lucky quarter':
        print("That quarter is only lucky you. It's still only worth 25 cents.")
        myPlayer.balance = myPlayer.balance + .25
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
        myPlayer.items.remove('Lucky Quarter')
        myPlayer.items_sold.append('Lucky Quarter')
        sell_input()
    elif action.lower() == 'items':
        items_print()
        sell_input()
    elif action.lower() == 'bag of chips':
        print("Let's see, a 5 year old bag of potato chips should come to...about 1 cent.")
        myPlayer.balance = myPlayer.balance + .01
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
        myPlayer.items.remove('Bag of Chips')
        myPlayer.items_sold.append('Bag of Chips')
        sell_input()
    elif action.lower() == 'chips':
        print("Let's see, a 5 year old bag of potato chips should come to...about 1 cent.")
        myPlayer.balance = myPlayer.balance + .01
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
        myPlayer.items.remove('Bag of Chips')
        sell_input()
    elif action.lower() == 'slip of paper':
        print("You can't sell that, how else will you remember to visit 'eddievanbonkhertz.com, the official EVB wesite'?")
        sell_input()
    elif action.lower() == "slip of paper with 'eddievanbonkhertz.com' on it":
        print("You can't sell that, how else will you remember to visit 'eddievanbonkhertz.com, the official EVB wesite'?")
        sell_input()
    elif action.lower() == "lottery ticket":
        print("Who do you think would want this?")
        myPlayer.balance = myPlayer.balance + .10
        print('You now have ' + str(myPlayer.balance) + ' Dollars.')
        myPlayer.items_sold.append('Lottery Ticket')
        sell_input()
        myPlayer.items.remove('Lottery Ticket')
    elif action.lower == 'A copy of the book True Memoirs Of a Disgraced Clown. (You are able to read it by typing "read")':
        print("You can't sell this. Why would you want to? It's the ultimate advice book.")
        sell_input()
    elif action.lower == 'james':
        print("You are trying to sell a human being like you're Thomas Jefferson? I won't allow this, even though I sold him to you in the first place. Actually, just because you wanted to, there's negative 20 bucks.")
        myPlayer.balance = myPlayer.balance -20
        sell_input()
    elif action.lower() == 'emu':
        print("Emus are cool, why on this alternate dimension earth would you want to sell one, especially when it doubles as a transportation device! ...Although...If you DO want to sell it, ill give you 50 bucks. We got a deal?")
        emu_input = input('\n'+'> ')
        if emu_input in ['y','yes']:
            print("Finally! I have a transportation method! Now I can go to the Casino! Heheh")
            myPlayer.items.remove("Emu")
            myPlayer.items_sold.append('Emu')
            myPlayer.balance = myPlayer.balance + 50
        elif emu_input in ['n','no']:
            print("Fine. I'll just have to walk I guess. Here's some money anyway, buy your emu something nice...")
            myPlayer.balance = myPlayer.balance + 50
        sell_input()
    elif action.lower() == 'clown car':
        print("You want to sell an original model clown car? I'll take it off your hands...")
        myPlayer.balance = myPlayer.balance + 13000
        myPlayer.items.remove('Clown Car')
        myPlayer.items_sold.append('Clown Car')
        sell_input()
    elif action.lower() == 'gun':
        print("How else will you communicate to veterans? Fine, I'm sure somebody wants it...")
        myPlayer.items.remove('Gun')
        myPlayer.items_sold.append('Gun')
        myPlayer.balance = myPlayer.balance + 100
        sell_input()
    elif action.lower() == 'plush grenade':
        print("You have sold Plush Grenade")
        myPlayer.items.remove('Plush Grenade')
        myPlayer.items_sold.append('Plush Grenade')
        myPlayer.balance = myPlayer.balance + 14
        sell_input()
    elif action.lower() == 'leeeeeeeeeeeeggg':
        print("The leg has become a part of you. You cannot sell just the leg. Do you want to sell yourself?")
        leg_input = input('> ')
        if leg_input in ['y','yes']:
            print("You unfortunately sold yourself to Terrance, the local mobster. You couldn't deny the deal, it was a good price. He kills you, no details, you don't want to hear them. Please Restart. ")
            sell_input()
        else:
            print('You did not sell your yourself, good move.')
            sell_input()
    elif action.lower() == 'discontinuity':
        print("We have enough as it is, we don't want this. I'll give you pity cash, though. ")
        myPlayer.balance = myPlayer.balance + 50000
        sell_input()
    elif action.lower() == 'russia book':
        print("By selling this, you will anger Stalin, Do you want to proceed?")
        russia_input = input('\n' + '> ')
        if russia_input in ['y','yes']:
            print("You sold the book for 1,000,000 dollars, but couldn't get the money before Stalin murdered you personally. You died." )
            restart(5)
        elif russia_input in ['n','no']:
            print("You just saved yourself from a, what they call in the business, 'Death by Stalin'. For thtaa you have earned...nothing, excet that you kept your life, barely. That should be good enough for you. ")
            sell_input()
    elif action.lower() == 'kgb':
        if 'KGB' not in myPlayer.items_sold:
            print("You sell the beet for 40 dollars somehow. Ever thought of being a car salesman?")
            myPlayer.balance = myPlayer.balance + 40
            myPlayer.items.remove('KGB')
            myPlayer.items_sold.append('KGB')
            sell_input()
        else:
            print("You sell the beet for a dollar. Your luck with selling beets has ended.")
            myPlayer.balance = myPlayer.balance + 1
            myPlayer.items.remove('KGB')
            myPlayer.items_sold.append('KGB')
            sell_input()
    elif action.lower() == 'eggchair':
        print("You put out flyers for someone to buy the eggchair. You didn't have pictures though, so may were confused. You finally found a man willing to pay 100,000 dollars for it. You thought about selling it long and hard, thinking about if you could get a better offer. While you were thinking though, you ate the eggchair, and was pickpocketed. That wasn't a good day for you.")
        myPlayer.items.remove("Eggchair")
        myPlayer.balance = myPlayer.balance - 10
        myPlayer.items_sold.append('Eggchair')
        sell_input()
    elif action.lower() == 'omletting gun':
        print("You got this on a good deal, but you sold it anyway. You feel naked without it, but at least you got 200 bucks out of it.")
        myPlayer.items.remove("Omletting Gun")
        myPlayer.items_sold.append('Omletting Gun')
        myPlayer.balance = myPlayer.balance + 200
        sell_input()
    elif action.lower() == 'omlette':
        print("You want to sell a single, cold omlette? It also looks like it is covered in asphalt, has this been used? Nobody wants a used omlette, everyone knows they get more loose after use.")
        sell_input()
    elif action.lower() == 'book pages':
        print("You want to sell pages of your book? Why did you buy them in the first place? Also you can't sell these, that book is the best thing every written, according to the authors.")
        sell_input()
    elif action.lower() == 'stalin':
        print("You want to sell STALIN?! Stalin. You want to sell the man who killed millions. You want to sell Stalin. Stalin. I won't even entertain the thought. Not just because I'm communist (Never heard of an extremely political text-voice-over?), but mainly because if you go through with this, Stalin will kill you. So I'll save him some trouble...")
        restart(5)
    elif action.lower() == 'kgb officer':
        print("You want to lessen the KGB? I'll answer for you: No, you don't. ")
        sell_input()
    elif action.lower() == 'Milk':
        print("The 'milk' in the bottle you bought turned out to be horse glue, sadly you didn't find out until you had sold it. Rest in peace Charles, rest in peace.")
        print("You have aquired Guilt.")
        myPlayer.items_sold.append('Milk')
        myPlayer.items.append('Guilt')
        myPlayer.taken_items.append("Guilt")
        myPlayer.balance = myPlayer.balance + 1.00
        sell_input()
    elif action.lower() == "stalin's Hair":
        print("Some collector now has enough stalin hair to create a stalin wig. All thanks to you!")
        myPlayer.balance = myPlayer.balance + 10000
        myPlayer.items.remove("Stalin's Hair")
        myPlayer.items_sold.append("Stalin's Hair")
        sell_input()
    elif action.lower() == "stalins Hair":
        print("Some collector now has enough stalin hair to create a stalin wig. All thanks to you!")
        myPlayer.balance = myPlayer.balance + 10000
        myPlayer.items.remove("Stalin's Hair")
        myPlayer.items_sold.append("Stalin's Hair")
        sell_input()
    elif action.lower() == 'picracko mirror':
        print("Who is going to want a phony picracko piece. Someone on t-bay that's who.")
        myPlayer.balance = myPlayer.balance + 20
        myPlayer.items.remove("Picracko Mirror")
        myPlayer.items_sold.append("Picracko Mirror")
        sell_input()
    elif action.lower() == 'guilt':
        print("You cannot get rid of it, it is there forev... Oh, nevermind, you've forgotten all about it.")
        myPlayer.items.remove("Guilt")
        myPlayer.items_sold.append("Guilt")
        sell_input()
    elif action.lower() == 'tickets':
        print("These are for emergencies, you have to keep them in case you need to go to Ocean World to save the world or something.")
        sell_input()
    elif action.lower() == 'ocean world tickets':
        print("These are for emergencies, you have to keep them in case you need to go to Ocean World to save the world or something.")
        sell_input()
    elif action.lower() == 'picracko original':
        print("You put it up in a fancy auctionhouse, and when the bidders saw the painting, they burst out laughing, maybe it wasn't the best idea to do this on your birthday. Nevertheless, someone bought it for 400 grand. As a gag gift, but still, its something.")
        myPlayer.balance = myPlayer.balance + 400000
        myPlayer.items.remove('Picarcko Original')
        print("You now have "+ str(myPlayer.balance) + " Dollars.")
        myPlayer.items_sold.append("Picracko Original")
        sell_input()
    elif action.lower() == 'sailboat':
        print("You can't sell this. How else will you get around?")
        sell_input()
    elif action.lower() in ['ocean world t-shirt','ocean world t shirt']:
        print("You sold the T-shirt for 100 bucks, and I though Ocean World overpriced it...")
        myPlayer.balance = myPlayer.balance + 100
        myPlayer.items_sold.append("Ocean World T-Shirt")
        myPlayer.items.remove("Ocean World T-Shirt")
        myPlayer.items_sold.append("Ocean World T-Shirt")
    elif action.lower() in ['22 ocean bucks']:
        if myPlayer.location == 'Ocean World':
            print("You're still in Ocean world, so you think, why not spend the 22 Ocean Bucks? You go to the shop and ask what you can get for 22 Ocean Bucks. They give you three options, an Ocean World T-Shirt, a Fish Net Hat, or a Whale Keychain that says 'Eddie Van Bonkhorts'.")
            ocean_bucks_input = input("Which do you choose?")
            if ocean_bucks_input in ['t-shirt','t shirt']:
                print("You have aquired Ocean World T-Shirt")
                myPlayer.items.append("Ocean World T-Shirt")
                myPlayer.items.remove("22 Ocean Bucks")
                myPlayer.taken_items.append("Ocean World T-Shirt")
                myPlayer.items_sold.append("22 Ocean Bucks")
                sell_input()
            elif ocean_bucks_input == 'fish net hat':
                print("You have aquired Fish Net Hat. It's like a hair net, but with a fish glued to the inside.")
                myPlayer.items.append("Fish Net Hat")
                myPlayer.items.remove("22 Ocean Bucks")
                myPlayer.taken_items.append("Fish Net Hat")
                myPlayer.items_sold.append("22 Ocean Bucks")
                sell_input()
            elif ocean_buck_input == "whale keychain":
                print("You have aquired Whale Keychain that says 'Eddie Van Bonkhorts'")
                myPlayer.items.append("Whale Keychain that says 'Eddie Van Bonkhorts'")
                myPlayer.items.remove("22 Ocean Bucks")
                myPlayer.taken_items.append("Whale Keychain that says 'Eddie Van Bonkhorts'")
                myPlayer.items_sold.append("22 Ocean Bucks")
                sell_input()
            else:
                print("Not a known option, type whale keychain, fish net hat, or t-shirt.")
        else:
            print("You trade them for a lottery ticket to a stranger you meet on the street. You get 15 bucks from It! Oh, wait, they're Ocean World Bucks...")
            myPlayer.items.append("15 Ocean Bucks")
            myPlayer.items.remove("22 Ocean Bucks")
            myPlayer.taken_items.append("15 Ocean Bucks")
            myPlayer.items_sold.append("22 Ocean Bucks")
            sell_input()
    elif action.lower() == '15 ocean bucks':
        print("You trade these for another lottery ticket to a different stranger. You scratch this one and see that you have won a... a FREE Dune buggy! It is slightly broken though, and only runs on Ocean World Bucks, and it can only go in reverse. Basically, you can go back to the previous location one time.")
        myPlayer.items.append("Broken Dune Buggy")
        myPlayer.items.remove("15 Ocean Bucks")
        myPlayer.taken_items.append("Broken Dune Buggy")
        myPlayer.items_sold.append("15 Ocean Bucks")
        print("You have aqcuired Broken Dune Buggy.")
        sell_input()
    elif action.lower() == 'useless dune buggy':
        print("You sell your useless sune buggy for a pretty penny. No, literally just a pretty penny...at the scrap yard.")
        myPlayer.items.append("Pretty Penny")
        myPlayer.items.remove("Useless Dune-Buggy")
        myPlayer.taken_items.append("Pretty Penny")
        myPlayer.items_sold.append("Useless Dune Buggy")
        myPlayer.balance = myPlayer.balance + .01
        sell_input()
    elif action.lower() == 'broken dune buggy':
        print("You want to sell a basically free vehicle thta gives you the god-like power of free will? I will give you a second chance. ")
        broken_buggy_input = input("Do you want to sell the Dune Buggy?")
        if broken_buggy_input in ['y','yes']:
            print("Sweet, my first step to an unlimited transportation vehicle! Here's 500...")
            myPlayer.balance = myPlayer.balance + 500
            myPlayer.items.remove("Broken Dune Buggy")
            myPlayer.items_sold.append("Broken Dune Buggy")
        else:
            print("The smart decision, something I didn't expect from you...")
            sell_input()
    elif action.lower() == "pretty penny":
        print("You sold the penny for nothing, because you accidentally droppped it down a drain")
        myPlayer.items.remove("Pretty Penny")
        myPlayer.items_sold.append("Pretty Penny")
        sell_input()
    elif action.lower() == 'uniform':
        print("You've been lugging this piece of garbage around for too long. You give it to some random guy so he can pretend that he works there. Greg got his face broken for 100 bucks, what a waste.")
        myPlayer.items.remove("6/11 Gas Station Uniform")
        myPlayer.items_sold.append("6/11 Gas Station Uniform")
        sell_input()
    elif action.lower() == 'moon cheese':
        if myPlayer.moon_cheese == False:
            print("You sold it before you got hooked, good thinking.")
            myPlayer.items.remove("Moon Cheese")
            myPlayer.items_sold.append("Moon Cheese")
            myPlayer.balance = myPlayer.balance + 3
        elif myPlayer.moon_cheese == True:
            print("You try to sell it, but you think about eating it instead, so you keep it.")
            sell_input()
    while action not in ['moon cheese','uniform','pretty penny','useless dune buggy','broken dune buggy', '22 ocean bucks','15 ocean bucks','ocean world t shirt','ocean world t-shirt','sailboat','picracko original','tickets','ocean world tickets','lottery ticket',"slip of paper with 'eddievanbonkhertz.com' on it",'slip of paper','chips','bag of chips','lucky quarter','easter egg','true memoirs of a disgraced clown', 'book','quit','eggchair','kgb','russia book', 'discontinuity','leeeeeeeeeeeeggg','leg','plush grenade','gun','clown car','emu','james']:
        sell_help = "This is not a known item. Please try a different item. "
        for character in sell_help:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        sell_input()







def buy_input():
    action = input('\n'+'Which item would you like to buy?'+'\n')
    if action.lower() == 'quit':
        print('You have exited the store, back to the story')
        prompt_input()
    elif action.lower() == 'james':
        James_description()
        james_input = input("Would you like to buy James?" + '\n' +'> ')
        if james_input in ['y','yes']:
            if myPlayer.balance > 1500:
                if 'james' not in myPlayer.characters:
                    print("Congratulations! You now have purchased your very own human. His name is James. He doesn't really do much, but he is there, and he knows how to sail. Buying him unlocked a new item in the store, 'Sailboat'.")
                    myPlayer.characters.append('James')
                    myPlayer.balance = myPlayer.balance - 1500
                    player_buy()
            else:
                print("You do not have enough money for this item.")
                player_buy()
        else:
            print("You did not buy James.")
            player_buy()
    elif action.lower() == 'emu':
        emu_description()
        emu_input = input("Would you like to buy an Emu?"+ '\n' +'> ')
        if emu_input in ['y','yes']:
            if myPlayer.balance > 15000:
                if 'Emu' not in myPlayer.taken_items:
                    print("You have purchased an Emu! It grants you access to the 'next and 'back' commands. It is also your own emu, so that's neat, I guess.")
                    myPlayer.items.append('Emu')
                    myPlayer.taken_items.append('Emu')
                    myPlayer.balance = myPlayer.balance - 15000
                    player_buy()
            else:
                print("You do not have enough money for this item.")
                player_buy()
        else:
            print("You did not buy an Emu.")
            player_buy()
    elif action.lower() == 'clown car':
        clown_car_description()
        clown_car_input = input("Would you like to buy Clown Car?"+ '\n' +'> ')
        if clown_car_input in ['y','yes']:
            if myPlayer.balance > 15000:
                if 'Clown Car' not in myPlayer.taken_items:
                    print("You now have a clown car! It grants you access to the 'next' and 'back' commands. After you first got in, you noticed that it cannot drive, only crash into things. You nearly totalled it. You keep the keys in case it comes in handy later.")
                    myPlayer.items.append('Clown Car')
                    myPlayer.taken_items.append('Clown Car')
                    myPlayer.balance = myPlayer.balance - 15000
                    player_buy()
            else:
                print("You do not have enough money for this item.")
                player_buy()
        else:
            print("You did not buy a Clown Car.")
            player_buy()
    elif action.lower() == 'gun':
        gun_description()
        gun_input = input("Would you like to buy Gun?"+ '\n' +'> ')
        if gun_input in ['y','yes']:
            if myPlayer.balance > 200:
                if 'Gun' not in myPlayer.taken_items:
                    print("You now have a Gun! You can't shoot people with it, or do anything other than using it for military gun calls. You now have access to the 'military gun call' command. It mainly just for show, but it may be useful.")
                    myPlayer.items.append('Gun')
                    myPlayer.taken_items.append('Gun')
                    myPlayer.balance = myPlayer.balance - 200
                    player_buy()
            else:
                print("You do not have enough money for this item.")
                player_buy()
        else:
            print("You did not buy the Gun.")
            prompt_input()
    elif action.lower() == 'plush grenade':
        plush_grenade_description()
        grenade_input = input("Would you like to buy Plush Grenade?"+ '\n' +'> ')
        grenade_input = input("How many Plush Grenades do you want?"+ '\n' +'> ')
        if int(grenade_input) >0:
            if myPlayer.balance > (15*int(grenade_input)) :
                print('You now have a Plush Grenade. It is exactly like a real grenade, except soft. Use the command "boom" to set off one of these in your locaton. It may result in restart, or be nessecary to continue the game')
                myPlayer.balance = myPlayer.balance - (15*int(grenade_input))
                for i in range(int(grenade_input)):
                    myPlayer.items.append("Plush Grenade")
                player_buy()
            else:
                print("You don't have enough money.")
                player_buy()
        else:
            print("You did not buy Plush Grenade.")
            player_buy()
    elif action.lower() == "grenade":
        plush_grenade_description()
        grenade_input = input("How many Plush Grenades do you want?"+ '\n' +'> ')
        if int(grenade_input) >0:
            if myPlayer.balance > (15*int(grenade_input)) :
                print('You now have a Plush Grenade. It is exactly like a real grenade, except soft. Use the command "boom" to set off one of these in your locaton. It may result in restart, or be nessecary to continue the game')
                myPlayer.balance = myPlayer.balance - (15*int(grenade_input))
                for i in range(int(grenade_input)):
                    myPlayer.items.append("Plush Grenade")
                player_buy()
            else:
                print("You don't have enough money.")
                player_buy()
        else:
            print("You did not buy Plush Grenade.")
            player_buy()
    elif action.lower() == 'leg':
        leg_description()
        leg_input = input("Would you like to buy Leeeeeeeeeeeeggg?"+ '\n' +'> ')
        if leg_input in ['y','yes']:
            if myPlayer.balance > 500:
                if 'Leeeeeeeeeeeeggg' not in myPlayer.taken_items:
                    if 'Leeeeeeeeeeeeggg' in myPlayer.completed_quests:
                        print("You now have "+leg_var+" leeeeeeeeeeeeggg. It doesn't do much besides allow you to walk on two feet for the first time in a while.")
                        myPlayer.items.append(leg_var+'Leeeeeeeeeeeeggg')
                        myPlayer.taken_items.append('Leeeeeeeeeeeeggg')
                        myPlayer.balance = myPlayer.balance - 500
                        prompt_input()
                    else:
                        print('You have not yet completed the quest to unlock this item.')
                        player_buy()
            else:
                print("You do not have enough money for this item.")
                player_buy()
        else:
            print("You did not buy the Leeeeeeeeeeeeggg")
            player_buy()
    elif action.lower() == 'continuity':
        continuity_description()
        continuity_input = input("Would you like to buy Continuity?"+ '\n' +'> ')
        if continuity_input in ['y','yes']:
            if myPlayer.balance > 250000:
                if 'continuity' not in myPlayer.taken_items:
                    print("I cannot believe you actually not only recieved this item without cheats, but chose to get this item. Well I honestly didn't think someone was going to get this far. I mean you understand it is literally impossible to have continuity with anythng related to EVB right? I don't want to give you nothing, I mean that would be mean, the other hand, I can't give you continuity, thats phisically impossible in this game. How about this, you get 'Discontinuity'? Here, let me gather some, this place is full of it! Alright, here you go!")
                    myPlayer.items.append('Discontinuity')
                    myPlayer.taken_items.append('Discontinuity')
                    print('You have aquired Discontinuity.')
                    myPlayer.balance = myPlayer.balance - 250000
                    player_buy()
            else:
                print("You don't have enough money.")
                player_buy()
        else:
            print("You did not buy Continuity")
            player_buy()
    elif action.lower() == 'russia book':
        russia_book_description()
        russia_input = input("Would you like to buy Russia Book?"+ '\n' +'> ')
        if russia_input in ['y','yes']:
            if myPlayer.balance > 99:
                print("Congrats! You have just helped refuel the soviet union by purchasing this book. You have also unlocked the ability to purchase 'KGB', and have unlocked the 'russia' command which will read you the How To Escape Russia book.")
                myPlayer.items.append('How to Escape Russia by Stalin')
                myPlayer.taken_items.append('How to Escape Russia by Stalin')
                myPlayer.balance = myPlayer.balance - 100
                player_buy()
            else:
                print("You don't have enough money.")
                player_buy()
        else:
            print("You did not buy russia book")
            player_buy()
    elif action.lower() == 'kgb':
        if 'How to Escape Russia by Stalin' in myPlayer.taken_items:
            kgb_description()
            kgb_input = input("Would you like to buy KGB?"+ '\n' +'> ')
            if int(kgb_input) >0:
                if myPlayer.balance > ((1*int(kgb_input))-1):
                    print("You have bought KGB, a Kenny Good Beets beet. You may eat it, or admire it. The choice is yours")
                    for i in range(int(kgb_input)):
                        myPlayer.items.append('KGB')
                    myPlayer.taken_items.append('KGB')
                    myPlayer.balance = myPlayer.balance - (1*int(kgb_input))
                    player_buy()
                else:
                    print("You do not have enough money for this item.")
                    player_buy()
            else:
                print("You did not buy KGB")
                player_buy()
        else:
            print('It seems that you have not yet unlocked this item. ')
            player_buy()
    elif action.lower() == 'eggchair':
        eggchair_description()
        eggchair_input = input("How many Eggchairs would you like?"+ '\n' +'> ')
        if int(eggchair_input) >0:
            if myPlayer.balance > ((5*int(eggchair_input))-1):
                print("You now have a delicious pastry, an eggchair. You may eat it, or watch it slowly rot.")
                myPlayer.taken_items.append('Eggchair')
                for i in range(int(eggchair_input)):
                    myPlayer.items.append('Eggchair')
                myPlayer.balance = myPlayer.balance - (5*int(eggchair_input))
                player_buy()
            else:
                print("You don't have enough money.")
                player_buy()
        else:
            print("You did not buy an Eggchair")
            player_buy()
    elif action.lower() == 'omletting gun':
        omletting_gun_description()
        omletting_gun_input = input("Would you like to buy Omletting Gun?"+ '\n' +'> ')
        if omletting_gun_input in ['y','yes']:
            if myPlayer.balance > 150:
                if 'Omletting Gun' not in myPlayer.taken_items:
                    print("You now have an omletting gun! You can use it on enemies, when you encounter them. Buy omlettes as ammo from the shop. Just make sure not to point it at your face...")
                    myPlayer.items.append('Omletting Gun')
                    myPlayer.taken_items.append('Omletting Gun')
                    myPlayer.balance = myPlayer.balance - 150
                    player_buy()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print('You did not buy Omletting Gun')
            player_buy()
    elif action.lower() == 'omlette':
        if 'Omletting Gun' in myPlayer.taken_items:
            omlette_description()
            omlette_input = input("How many Omlettes would you like?"+ '\n' +'> ')
            if int(omlette_input) >0:
                if myPlayer.balance > ((10*int(omlette_input))-1):
                    print("You have acquired more ammo for your omletting gun.")
                    myPlayer.balance = myPlayer.balance - 10*int(omlette_input)
                    for i in range(int(omlette_input)):
                        myPlayer.items.append('Omlette')
                else:
                    print("You don't have enough money for this item.")
                    player_buy()
            else:
                print("You did not buy Omlette")
                player_buy()
        else:
            print("You have not unlocked this item yet.")
    elif action.lower() == 'book page':
        book_page_description()
        book_pages_input = input("How many Book Pages would you like?"+ '\n' +'> ')
        if int(book_pages_input) >0:
            if myPlayer.balance > ((1*int(book_pages_input))-1):
                print("You found a page from your book on the ground. You haphazardly staple it the book. You can view it by typing read.")
                EVB_buy_random = random.choice(EVB_buy)
                for i in range(int(book_pages_input)):
                    if EVB_buy_random not in EVB:
                        EVB.append(EVB_buy_random)
                        print(EVB_buy_random)
                        player_buy()
                    while EVB_buy_random in EVB:
                        EVB_buy_random = random.choice(EVB_buy)
                        if EVB_buy_random not in EVB:
                            EVB.append(EVB_buy_random)
                            print(EVB_buy_random)
                            player_buy()
                player_buy()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print("You did not buy a book page")
            player_buy()
    elif action.lower() == 'picracko original':
        picracko_original_description()
        picracko_input = input("Would you like to buy a Picracko Original?"+ '\n' +'> ')
        if picracko_input in ['y','yes']:
            if myPlayer.balance > 999999:
                if 'Picracko Original' not in myPlayer.taken_items:
                    if myPlayer.solved_places["Picracko Gallery"] == True:
                        print("You have your very own artpiece made by Picracko! View anytime with the command 'painting'.")
                        myPlayer.items.append("Picracko Original")
                        myPlayer.taken_items.append("Picracko Original")
                        myPlayer.balance = myPlayer.balance - 1000000
                        player_buy()
                    else:
                        print("How did you know about this? You haven't unlocked this yet.")
                        player_buy()
                else:
                    print("You already have a Picracko Original")
                    player_buy()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print("You did not buy a Picracko Original")
            player_buy()
    elif action.lower() == 'stalin':
        stalin_description()
        stalin_input = input("Would you like to buy Stalin?"+ '\n' +'> ')
        if stalin_input in ['y','yes']:
            if 'Stalin' not in myPlayer.characters:
                print("You now have your very own Stalin. He can save your life 3 times before needing a recharge. You have also unlocked 'KGB Officer' in the store, get 10 or more KGBOfficers and they will become a vehicle and unlock the 'next' and 'back' commands.")
                myPlayer.characters.append("Stalin")
                player_buy()
            else:
                print("It appears that you already have a Stalin, but onemore can't hurt. I'm going to have to charge you 15,000 dollars for this one though.")
                stalin_input2 = input("Do you want to proceed?"+'\n'+'> ')
                if stalin_input2 in ['y','yes']:
                    myPlayer.characters.append("Stalin")
                    myPlayer.balance = myPlayer.balance - 15000
                    player_buy()
        else:
            print("You didn't buy Stalin, even though he is FREE. Are you crazy?")
            player_buy()
    elif action.lower() == 'sailboat':
        sailboat_description()
        sailboat_input = input("Would you like to buy the Sailboat?"+ '\n' +'> ')
        if sailboat_input in ['y','yes']:
            if 'Sailboat' not in myPlayer.taken_items:
                if "James" in myPlayer.characters:
                    print("You now have a sailboat. 'But I don't know how to sail', you might be thinking, but James does, he will escort you from location to location through the 'next' and 'back' commands. Plus who knows, it may come in handy later.")
                    myPlayer.items.append('Sailboat')
                    myPlayer.taken_items('Sailboat')
                    myPlayer.balance = myPlayer.balance - 15000
                else:
                    print("You have not unlocked this item.")
                    player_buy()
            else:
                print("You already bought this item")
                player_buy()
        else:
            print("You did not buy the Sailboat")
            player_buy()
    elif action.lower() == 'kgb officer':
        kgb_officer_description()
        kgb_officer_input = input("Would you like to buy a KGB Officer?"+ '\n'+'> ')
        if kgb_officer_input in ['y','yes']:
            if 'Stalin' in myPlayer.characters:
                if myPlayer.balance > (300 ):
                    if 'KGB Army' not in myPlayer.characters:
                        kgb_officers_left = 10-myPlayer.characters.count("KGB Officer")
                        kgb_platoon_left = 50-((myPlayer.characters.count("KGB Platoon")*10)+ myPlayer.characters.count("KGB Officer"))
                        kgb_horde_left = 100- ((myPlayer.characters.count("KGB Horde")* 50)+ (myPlayer.characters.count("KGB Platoon")*10) +myPlayer.characters.count("KGB Officer"))
                        myPlayer.characters.append("KGB Officer")
                        myPlayer.balance = myPlayer.balance - (300)
                        if myPlayer.characters.count("KGB Officer") > 9:
                            print("Your 10 KGB Officers have turned into a KGB Platoon!")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.remove("KGB Officer")
                            myPlayer.characters.append("KGB Platoon")
                            player_buy()
                        elif myPlayer.characters.count("KGB Platoon") > 4:
                            if 'KGB Platoon' in myPlayer.characters:
                                myPlayer.characters.remove('KGB Platoon')
                                myPlayer.characters.remove('KGB Platoon')
                                myPlayer.characters.remove('KGB Platoon')
                                myPlayer.characters.remove('KGB Platoon')
                                myPlayer.characters.remove('KGB Platoon')
                                myPlayer.characters.append("KGB Horde")
                                print("Your humble KGB Platoon has turned into a KGB Horde and has unlocked the 'next' command!")
                                player_buy()
                        elif myPlayer.characters.count('KGB Horde') > 1:
                            if 'KGB Horde' in myPlayer.characters:
                                myPlayer.characters.remove('KGB Horde')
                                myPlayer.characters.remove('KGB Horde')
                                myPlayer.characters.append("KGB Army")
                                print("Your humble KGB Horde has turned into a KGB Army, and has unlocked the 'motherland' command! The 'motherland' command will allow you to rob people one time per location.")
                                player_buy()
                        elif 'KGB Platoon' in myPlayer.characters:
                            print("You now have a KGB Officer to protect you and stalin. Collect "+ str(kgb_platoon_left)+ " more Officers to create a KGB Horde.")
                            player_buy()
                        elif ['KGB Army','KGB Horde','KGB Platoon'] not in myPlayer.characters:
                            print("You now have a KGB Officer to protect you and stalin. Collect "+ str(kgb_officers_left)+ " more Officers to create a KGB Platoon.")
                            player_buy()
                        elif 'KGB Horde' in myPlayer.characters:
                            print("You now have a KGB Officer to protect you and stalin. Collect "+ str(kgb_horde_left)+ " more Officers to create a KGB Army.")
                            player_buy()
                        player_buy()
                    else:
                        print("You have a KGB Army, you have maxed out the amount of KGB Officers you can buy.")
                        player_buy()
                else:
                    print("You don't have enough money for this item.")
            else:
                print("You haven't unlocked this item yet.")
                player_buy()
    elif action.lower() in ["dune buggy","broken dune buggy"]:
        dune_buggy_description()
        dune_buggy_input = input("Would you like to buy a Broken Dune Buggy?")
        if dune_buggy_input in ['yes','y']:
            if myPlayer.balance > 999:
                myPlayer.items.append("Broken Dune-Buggy")
                myPlayer.taken_items.append("Broken Dune Buggy")
                print("You now have a dune buggy! It allows you to go back a location one time, use it wisely.")
            else:
                print("You do not have enough money for this item.")
                player_buy()
        else:
            print("You did not buy the Broken Dune Buggy")
            player_buy()
    elif action.lower() == "moon cheese":
        moon_cheese_description()
        moon_cheese_input = input("Would you like to buy Moon Cheese? \n")
        if moon_cheese_input in ['yes','y']:
            if myPlayer.balance > myPlayer.moon_cheese_cost:
                myPlayer.taken_items.append("Moon Cheese")
                myPlayer.items.append("Moon Cheese")
                myPlayer.balance = myPlayer.balance - myPlayer.moon_cheese_cost
                myPlayer.moon_cheese_cost = myPlayer.moon_cheese_cost + 5
                print("You now have a gallon of Moon Cheese! Use the command 'eat' to ingest it.")
                buy_input()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print("You did not buy Moon Cheese")
            player_buy()
    elif action.lower() == "magic 9 ball":
        magic_ball_description()
        magic_ball_input = input("Would you like to buy Magic 9 Ball? \n")
        if magic_ball_input in ['yes','y']:
            if myPlayer.balance > 19:
                myPlayer.taken_items.append("Magic 9 Ball")
                myPlayer.items.append("Magic 9 Ball")
                myPlayer.balance = myPlayer.balance - 20
                print("You now have a Magic 9 Ball, use the command 'shake' to get a tip from it.")
                buy_input()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print("You did not buy Magic 9 Ball")
            player_buy()
    elif action.lower() == "freeze dried soda":
        freeze_dried_soda_description()
        freeze_dried_soda_input = input("How many Freeze Dried Sodas would you like to buy?\n> ")
        if int(freeze_dried_soda_input) >0:
            if myPlayer.balance > ((19* int(freeze_dried_soda_input))-1):
                myPlayer.taken_items.append("Freeze Dried Soda")
                for i in range(int(freeze_dried_soda_input)):
                    myPlayer.items.append("Freeze Dried Soda")
                myPlayer.balance = myPlayer.balance - (19*int(freeze_dried_soda_input))
                print("You now have a brick of soda flavor, use 'eat' to suggest it.")
                buy_input()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print("You did not buy any Freeze Dried Soda.")
            prompt_input()
    elif action.lower() == "bonkhertz split":
        bonkhertz_split_description()
        bonkhertz_split_input = input("How many Bonkhertz Splits would you like?\n> ")
        if int(bonkhertz_split_input) >0:
            if myPlayer.balance > ((190* int(bonkhertz_split_input))-1):
                myPlayer.taken_items.append("Bonkhertz Split")
                for i in range(int(bonkhertz_split_input)):
                    myPlayer.items.append("Bonkhertz Split")
                myPlayer.balance = myPlayer.balance - (190*int(bonkhertz_split_input))
                print("You now have a Bonkhertz Split, use the command 'eat' to ingest it.")
                buy_input()
            else:
                print("You don't have enough money for this item.")
                player_buy()
        else:
            print("You did not buy any Bonkhertz Splits.")
            prompt_input()
    while action.lower() not in ['freeze dried soda','bonkhertz split','magic 9 ball','moon cheese','broken dune buggy','kgb officer','sailboat','quit','painting','picracko original','grenade','book page','omlette','omletting gun','eggchair','kgb','russia book', 'continuity','leg','plush grenade','gun','clown car', 'emu', 'james' ]:
        buy_help = 'That is not an item that is known or is available for sale. '
        for character in buy_help:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        player_buy()




def quest_print():
    if myPlayer.quests == []:
        print('You have no active quests.')
        prompt_input()
    else:
        print('You have ' + str(len(myPlayer.quests)) + ' quest(s): ' + ', '.join(myPlayer.quests))
        prompt_input()

def items_print():
    if myPlayer.items == []:
        print('You have no items.')
        prompt_input()
    else:
        print('You have ' + str(len(myPlayer.items)) + ' item(s): ' + ', '.join(myPlayer.items))
        prompt_input()


def characters_print():
    if myPlayer.characters == []:
        print('You have no characters.')
        prompt_input()
    else:
        print('You have ' + str(len(myPlayer.characters)) + ' character(s): ' + ', '.join(myPlayer.characters))
        prompt_input()



def completed_quest_print():
    if myPlayer.completed_quests == []:
        print('You have no completed quests.')
        prompt_input()
    else:
        print('You have ' + str(len(myPlayer.completed_quests)) + ' completed quest(s): ' + ', '.join(myPlayer.completed_quests))
        prompt_input()






def help_store_menu():
    print('#############################')
    print('#      Store Help Menu      #')
    print('#############################')
    print('#       Buy - To buy        #')
    print('#      Sell - To sell       #')
    print('#      Quit - To exit       #')
    print('#  Bal - Check your balance #')
    print('#############################')
    store_input()


def player_store():
    print('\n' + "You are now in the store, to go back to the story, type 'quit' " + '\n' + 'Would you like to to buy or sell?')
    store_input()















def player_buy():
    moon_len = len(str(myPlayer.moon_cheese_cost +1))
    print('\n'+'##########################################')
    print('#                                        #')
    print('#         Welcome To The Store!          #')
    print('#                                        #')
    print('##########################################')
    print('#                 ITEMS                  #')
    print('#                                        #')
    print('#             James - 1,500              #')
    if 'James' in myPlayer.characters:
        print("#            Sailboat - 15,000           #")
    print('#              Emu - 15,000              #')
    print('#           Clown Car - 15,000           #')
    print('#               Gun - 200                #')
    print('#          Plush Grenade - 15            #')
    if "Who's leg is this" in myPlayer.completed_quests:
        print('#        Leeeeeeeeeeeeggg  - 500         #')
    print('#         Continuity - 250,000           #')
    print('#  How to Escape Russia by Stalin - 100  #')
    print('#              (Russia Book)             #')
    if 'How to Escape Russia by Stalin' in myPlayer.items:
        print('#                KGB - 1                 #')
    print('#              Eggchair - 5              #')
    print("#         Bonkhertz Split - 190          #")
    print("#         Freeze Dried Soda - 19         #")
    print('#          Omletting Gun - 150           #')
    print("#           Magic 9 Ball - 20            #")
    print("#        Broken Dune Buggy - 1000        #")
    if 'Omletting Gun' in myPlayer.items:
        print('#              Omlette - 10              #')
    print('#             Book Page - 1              #')
    if myPlayer.solved_places['Picracko Gallery'] == True:
        print("#     Picracko Original - 1,000,000      #")
    if 'Summon Stalin' in myPlayer.completed_quests:
        print("#        Stalin - 0 (communism)          #")
    if moon_len < 2:
        if moon_len > 0:
            print("#            Moon Cheese - "+str(myPlayer.moon_cheese_cost +1)+"             #")
    if moon_len < 3:
        if moon_len > 1:
            print("#            Moon Cheese - "+str(myPlayer.moon_cheese_cost +1)+"            #")
    if moon_len < 4:
        if moon_len > 2:
            print("#            Moon Cheese - "+str(myPlayer.moon_cheese_cost +1)+"             #")
    if 'Stalin' in myPlayer.characters:
        print('#            KGB Officer - 150           #')
    print('##########################################')
    buy_input()












def picracko_original():
    if "Picracko Original" in myPlayer.items:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("{[{                                                     }]}")
        print("{[{                      ???????????????????????????    }]}")
        print("{[{                ????????????????????????             }]}")
        print("{[{              ?????????????             \            }]}")
        print("{[{            ?????????                    \           }]}")
        print("{[{           ?????????                      \          }]}")
        print("{[{           ????????       @0@       @0@    \         }]}")
        print("{[{           ??_?           @0@       @0@     |        }]}")
        print("{[{            /  \                            |        }]}")
        print("{[{            \                  /&&\         |        }]}")
        print("{[{             |                 &&&&         |        }]}")
        print("{[{              \        _       \&&/      _  |        }]}")
        print("{[{               |       \ \              / / |        }]}")
        print("{[{               |        \ \____________/ /  |        }]}")
        print("{[{               \         \______________/   :        }]}")
        print("{[{                \                          /         }]}")
        print("{[{                 \________________________/          }]}")
        print("{[{                      |            |                 }]}")
        print("{[{                   ___|            |___              }]}")
        print("{[{                  |   \            /   |             }]}")
        print("{[{                                                     }]}")
        print("{[{             Portrait of Eddie Van Bonkhertz         }]}")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("\n That's right, you just paid 1 million dollars for this.")
        prompt_input()
    else:
        print("You don't have the painting yet.")





















def James_description():
    print('###########################################')
    print('#                  James                  #')
    print('#              1,500 Dollars              #')
    print('#                                         #')
    print('# James is a 10 year-old that was acciden #')
    print('#  -tally kidnapped by one Eddie Van Bonk #')
    print('# -hertz. Now you can have him follow you #')
    print('# on your adventures for the low price of #')
    print('# 1,500 dollars. Is it legal? Maybe. Shou-#')
    print('# ld you? Yes.                            #')
    print('###########################################')





def emu_description():
    print('#############################################')
    print('#                    Emu                    #')
    print('#              15,000 Dollars               #')
    print('#                                           #')
    print('#   Buy an actual emu for transportation,   #')
    print('# it unlocks the "next" and "back" commands #')
    print('# that allow you to go forward and backwa-  #')
    print("# rds through the areas. Who doesn't want   #")
    print('#  1,500 dollars. Is it legal to own? Maybe.#')
    print('# Should you buy it? Yes.                   #')
    print('#############################################')






def clown_car_description():
    print('#############################################')
    print('#                 Clown Car                 #')
    print('#              15,000 Dollars               #')
    print('#                                           #')
    print('#   Buy an actual car for transportation,   #')
    print('# it unlocks the "next" and "back" commands #')
    print('# that allow you to go forward and backwa-  #')
    print("# rds through the areas. Who doesn't want   #")
    print('#  to own a clown car? Is it legal to own?  #')
    print('#  No. Should you buy it? Yes.              #')
    print('#############################################')



def gun_description():
    print('#############################################')
    print('#                    Gun                    #')
    print('#                200 Dollars                #')
    print('#                                           #')
    print("# Arm yourself with a gun that doesn't fire.#")
    print('#   You shoot it by typing "Military Gun    #')
    print('# Call". If you point it at people, the gun #')
    print("# refuses to fire. It is meant to signal to #")
    print('# other veterans, not to kill. It grants    #')
    print('#   access to the military gun call action  #')
    print('#  and description. Not worth buying, but   #')
    print("# hey, I'm just a description.              #")
    print('#############################################')



def plush_grenade_description():
    print('#############################################')
    print('#             "Plush" Grenades              #')
    print('#                15 Dollars                 #')
    print('#                                           #')
    print("# Buy a plush grenade. It's like a real one,#")
    print('#  but plush, it even explodes! Set it off  #')
    print('# by typing "boom" and get unique descript- #')
    print("# ions or use these to solve quests. Buying #")
    print('# one adds the "boom" command to your help  #')
    print('# menu and your list of actions.            #')
    print('#############################################')



def leg_description():
    print('#############################################')
    print('#              Leeeeeeeeeeeeggg             #')
    print('#                500 Dollars                #')
    print('#                                           #')
    print("# You must complete the Who's leg is this?  #")
    print('# quest to be able to buy this item. It is  #')
    print('#  a leg, it does nothing but replace your  #')
    print("# leg. That's it. it is just a leg you sto- #")
    print('# le from a political figure and put in pla-#')
    print("# ce of your leg.                           #")
    print('#############################################')




def continuity_description():
    print('#############################################')
    print('#                Continuity                 #')
    print('#              250,000 Dollars              #')
    print('#                                           #')
    print("# You are really going to buy this? No...   #")
    print("# You don't have this much money, and even  #")
    print("#  if you do, why would you buy this? It's  #")
    print("# not even possible to get. Plus, you could #")
    print('# buy 16,666 plush grenades for the same am #')
    print("# -ount. Don't buy this.                    #")
    print('#############################################')






def russia_book_description():
    print('#############################################')
    print('#       How to Escape Russia by Stalin      #')
    print('#                100 Dollars                #')
    print('#                                           #')
    print("#  This helpful guide is a nessecary item   #")
    print("# to have when travelling abroad. It helps  #")
    print("#  you get out of the most common hostage   #")
    print("#  situation in America, being in Russia.   #")
    print('# Buying this also unlocks the KGB for pur- #')
    print("# chase in the store. Buy today!            #")
    print('#############################################')








def kgb_description():
    print('###############################################')
    print('#                     KGB                     #')
    print('#                  1 Dollar                   #')
    print('#                                             #')
    print("# Buy it or we'll kill you. -Kenny Good Beats #")
    print('###############################################')





def eggchair_description():
    print('#############################################')
    print('#                 Eggchair                  #')
    print('#                10 Dollars                 #')
    print('#                                           #')
    print("#  A delicious desert. Basically a baguette #")
    print("#  filled with sugary cream and topped with #")
    print("#  chocolate cream. It unlcoks the eat fun- #")
    print("#  ction, allowing you to waste 10 dollars  #")
    print('# for no apparent reason.                   #')
    print('#############################################')





def omletting_gun_description():
    print('#############################################')
    print('#              Omletting Gun                #')
    print('#               150 Dollars                 #')
    print('#                                           #')
    print("#  The most powerful weapon on earth if us- #")
    print("#  ed correctly, the omletter, or Omletting #")
    print("#  Machine. Now available for the low, low  #")
    print("# price of 150 dollars! By it now to defeat #")
    print('# your enemies with solid egg.              #')
    print('#############################################')





def omlette_description():
    print('##############################################')
    print('#                  Omlette                   #')
    print('#                 10 Dollars                 #')
    print('#                                            #')
    print("#   A delicious solid egg. It may be eaten   #")
    print("#  or used as a weapon, so long as you have  #")
    print("#  the omlette gun. It can kill a man before #")
    print("#  the trigger is pulled, somehow. It can c- #")
    print('# reate a blast 10 times bigger than a nuke. #')
    print('##############################################')


def book_page_description():
    print('################################################')
    print('#                  Book Page                   #')
    print('#                   1 Dollar                   #')
    print('#                                              #')
    print("# You found a piece of paper on the ground,    #")
    print("# and it turned out to be one of the missing   #")
    print("# pages from your book. For some reason, the   #")
    print("# universe won't let you pick up the piece of  #")
    print('# paper until you leave a dollar on the ground #')
    print("# next to it. The universe is wierd like that, #")
    print("# dont ask questions, it's not exposition,     #")
    print('# just the way it works.                       #')
    print('################################################')




def picracko_original_description():
    print('################################################')
    print('#              Picracko Original               #')
    print('#              1,000,000 Dollars               #')
    print('#                                              #')
    print("#  This painting mysteriously appeared in the  #")
    print("# store under a vail. You have to buy it to    #")
    print("# see it, although it is a Picracko, so you    #")
    print("# know it'll be great. What are you waiting f- #")
    print('# or? Buy it with your not-earned money today! #')
    print('################################################')




def stalin_description():
    print('################################################')
    print('#                    Stalin                    #')
    print('#             0 Dollars (Communism)            #')
    print('#                                              #')
    print("#  You can buy Stalin. For free. Who wouldn't  #")
    print("#  want this deal! He comes with a new command #")
    print("#  as well, 'communism' turns the ENTIRE GAME  #")
    print("# from capitalism to communism! Plus it gives  #")
    print('# you a copy of the Communist Manifesto for f- #')
    print("# ree. It is a great deal! Stalin + Communism, #")
    print("# could there BE a better combination?         #")
    print('################################################')


def sailboat_description():
    print('#############################################')
    print('#                 Sailboat                  #')
    print('#              15,000 Dollars               #')
    print('#                                           #')
    print('# Buy an actual sailboat for transportation,#')
    print('# it unlocks the "next" and "back" commands #')
    print('# that allow you to go forward and backwa-  #')
    print("# rds through the areas. Who doesn't want   #")
    print('#   a sailboat. Is it legal to own? Sure.   #')
    print('#   Should you buy it? Of course.           #')
    print('#############################################')




def kgb_officer_description():
    print('################################################')
    print('#                  KGB Officer                 #')
    print('#                  300 Dollars                 #')
    print('#                                              #')
    print("# You can buy a KGB Officer to protect Stalin. #")
    print("# If you get 10, they turn into a KGB Platoon, #")
    print("# A KGB Platoon will unlock the 'next' command #")
    print("# And a KGB Horde will unlock the 'back' comm- #")
    print("# and, allowing you to traverse the land. It   #")
    print('#  is an amazing deal.                         #')
    print('################################################')

def dune_buggy_description():
    print('################################################')
    print('#               Broken Dune Buggy              #')
    print('#                 1000 Dollars                 #')
    print('#                                              #')
    print("# You can buy a real dune buggy! It is broken, #")
    print("#  and only has enough gas for a 30 min ride,  #")
    print("#  but it is useful nonetheless. It allows you #")
    print("#  to travel back a location ONCE. You can go  #")
    print("#  do things or events you couldn't have, get  #")
    print('# hidden items, or anything else you missed!   #')
    print('################################################')






def moon_cheese_description():
    moon_len = len(str(myPlayer.moon_cheese_cost +1))
    print('################################################')
    print("#                  Moon Cheese                 #")
    if moon_len < 2:
        if moon_len > 0:
            print("#                   "+str(myPlayer.moon_cheese_cost +1)+" Dollars                  #")
    if moon_len < 3:
        if moon_len > 1:
            print("#                  "+str(myPlayer.moon_cheese_cost +1)+" Dollars                  #")
    if moon_len < 4:
        if moon_len > 2:
            print("#                  "+str(myPlayer.moon_cheese_cost +1)+" Dollars                 #")
    print("#                                              #")
    print("# This is a gallon of liquid cheese. It isn't  #")
    print("# really cheese, more like a cheese-like subs- #")
    print("#   tance. You have heard stories that it is   #")
    print("#  'addictive' and 'bad for you', but it says  #")
    print("#   non addictive right on the box. Plus, one  #")
    print("# gallon couldn't hurt, right?                 #")
    print('################################################')





def cold_turkey_description():
    print('################################################')
    print("#                 Cold Turkey                  #")
    print("#                  2 Dollars                   #")
    print("#                                              #")
    print("# The people at the clinic said to go cold tu- #")
    print("# rky, right? There is no way that raw turkey  #")
    print("#  is bad for you or addictive like the Moon   #")
    print("# Cheese.  It even says 'For Moon Cheese addi- #")
    print("#  cts to get off the good stuff'. Two dollars #")
    print("#  to get off an addiction seems pretty good.  #")
    print('################################################')



def magic_ball_description():
    print('################################################')
    print("#                 Magic 9 Ball                 #")
    print("#                  20 Dollars                  #")
    print("#                                              #")
    print("#  This magic plastic ball with dice in it is  #")
    print("#  like a fortune cookie, but infinite and non #")
    print("# edible. It will give you valuble advice with #")
    print("#  the command 'shake'. It costs a dollar per  #")
    print("#  tip. It is important info that can change   #")
    print("# how you play the game.                       #")
    print('################################################')



def freeze_dried_soda_description():
    print('#################################################')
    print("#               Freeze-Dried Soda               #")
    print("#                  19 Dollars                   #")
    print("#                                               #")
    print("#  How do you freeze-dried soda, you may ask?   #")
    print("# You take out all the water until it's dry and #")
    print("#  frozen. Eating it also increases you death   #")
    print("# survivability.                                #")
    print('#################################################')






def bonkhertz_split_description():
    print('################################################')
    print("#                Bonkhertz Split               #")
    print("#                  190 Dollars                 #")
    print("#                                              #")
    print("#   A massive ice cream sunday that contains   #")
    print("# omlette fragments, some ashes of people who  #")
    print("# 'saved' your life over the years. It is top- #")
    print("# pped with some mints from The Mint, and cho- #")
    print("#  colate straight flush, a reference to your  #")
    print("#  amazing Blackjck skills. It adds 1 to your  #")
    print("# death survivablility rating, allowing you to #")
    print("# avoid a death in game. It also has a 1 in 10 #")
    print("# chance to cause an ice cream headache.       #")
    print('################################################')






def title_screen2():
    title_screen_bomb = places['Title Screen'][GRENADE]
    print('##############     ###')
    print('# Wel     - Q27&t -  ################           ')
    print('  C0pyri^&ht 2019 EV8*?ext Gam%! #')
    print('##############         ########')
    print(' $%         lco#$ to the *(VB Te        ')
    print('    ############   @#     - H%l! -            &^ ')
    print('*ext Gam  Publishing  ')
    print(title_screen_bomb)
    boom_balance()
    prompt_input()

def omlette():
    omlette_accomplish = myPlayer.omlette_accomplish[myPlayer.location]
    if 'Omletting Gun' in myPlayer.items:
        if 'Omlette' in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                if omlette_accomplish == False:
                    os.system('clear')
                    myPlayer.items.remove('Omlette')
                    myPlayer.omlette_accomplish[myPlayer.location] = True
                    title_screen2()
                    print(places['Title Screen'][OMLETTE])
                    if places[myPlayer.location][OMLETTE_ITEMS] != '':
                        myPlayer.items.append(places[myPlayer.location][OMLETTE_ITEMS])
                        print("You have aquired "+ places[myPlayer.location][OMLETTE_ITEMS] + ' .')
                    omlette_balance()
                else:
                    print("You have already destroyed the title screen.")
            elif myPlayer.location == "Payphone":
                if myPlayer.death_survivability >= 1:
                    print("You survived death this time, but your death survivability has decreased.")
                    myPlayer.death_survivability = myPlayer.death_survivability - 1
                    prompt_input()
                else:
                    print(places[myPlayer.location][OMLETTE])
                    restart(5)
            elif myPlayer.location == "India":
                if myPlayer.death_survivability >= 1:
                    print("You survived death this time, but your death survivability has decreased.")
                    myPlayer.death_survivability = myPlayer.death_survivability - 1
                    prompt_input()
                else:
                    print(places[myPlayer.location][OMLETTE])
                    restart(7)
            else:
                if myPlayer.omlette_accomplish[myPlayer.location] == False:
                    myPlayer.omlette_accomplish[myPlayer.location] = True
                    if places[myPlayer.location][OMLETTE_ITEMS] != '':
                        myPlayer.items.append(places[myPlayer.location][OMLETTE_ITEMS])
                        print("You have aquired "+ places[myPlayer.location][OMLETTE_ITEMS] + ' .')
                    myPlayer.items.remove('Omlette')
                    print(places[myPlayer.location][OMLETTE])
                    omlette_balance()
                else:
                    print("You have already omletted this area.")
        else:
            print("You have no ammo for your ometting gun. Buy some from the store.")
    else:
        print('It seems you have not yet unlocked this action.')
        prompt_input()



def read_russia_book():
    if 'How to Escape Russia by Joeseph Stalin' in myPlayer.items:
        stalin_read = "You grab the 'How to Escape Russia' book and it feels lighter than you expected. You open it, all the pages are blank except for one. It says: 'You can't.'"
        for character in stalin_read:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        prompt_input()
    else:
        print("CHeapskate, buy the book to read it. How would Stalin feel about this?")
        prompt_input()


def boom():
    boom_accomplish = myPlayer.grenade_accomplish[myPlayer.location]
    if 'Plush Grenade' in myPlayer.items:
        if myPlayer.location == 'Title Screen':
            if boom_accomplish != True:
                if places[myPlayer.location][GRENADE_ITEMS] != '':
                    myPlayer.items.append(places[myPlayer.location][GRENADE_ITEMS])
                    print("You have aquired "+ places[myPlayer.location][GRENADE_ITEMS] + ' .')
                myPlayer.grenade_accomplish[myPlayer.location] = True
                os.system('clear')
                myPlayer.items.remove('Plush Grenade')
                title_screen2()
                print(places[myPlayer.location][GRENADE])
                boom_balance()
                prompt_input()
            else:
                print("You have already destroyed the title screen.")
        elif myPlayer.location == "Payphone":
            if myPlayer.death_survivability >= 1:
                print("You survived death this time, but your death survivability has decreased.")
                myPlayer.death_survivability = myPlayer.death_survivability - 1
                prompt_input()
            else:
                print(places[myPlayer.location][GRENADE])
                restart(7)
        elif myPlayer.location == "India":
            if myPlayer.death_survivability >= 1:
                print("You survived death this time, but your death survivability has decreased.")
                myPlayer.death_survivability = myPlayer.death_survivability - 1
                prompt_input()
            else:
                print(places[myPlayer.location][GRENADE])
                restart(7)
        else:
            if boom_accomplish != True:
                if places[myPlayer.location][GRENADE_ITEMS] != '':
                    myPlayer.items.append(places[myPlayer.location][GRENADE_ITEMS])
                    print("You have aquired "+ places[myPlayer.location][GRENADE_ITEMS] + ' .')
                myPlayer.grenade_accomplish[myPlayer.location] = True
                myPlayer.items.remove('Plush Grenade')
                print(places[myPlayer.location][GRENADE])
                boom_balance()
                prompt_input()
            else:
                print("You have already exploded this area.")
    else:
        print('It seems you have not yet unlocked this action.')
        prompt_input()


def quest_complete():
    if "Milk" in myPlayer.taken_items:
        if myPlayer.location == 'Milk Store':
            myPlayer.completed_quests.append('Get Milk')
            print('\n'+'Objective completed: Get Milk')
            myPlayer.quests.remove('Get Milk')
            myPlayer.balance = myPlayer.balance + 30
            print('You now have ' + str(myPlayer.balance) + ' Dollars.')
            myPlayer.location == places[myPlayer.location][NEXT]
            print("You are now in the Picracko Gallery.")
    elif myPlayer.location == "Gas Station":
        if myPlayer.prompt == '3':
            myPlayer.completed_quests.append('Getting Started')
            print('\n'+'Objective completed: Getting Started')
            myPlayer.quests.remove('Getting Started')
            myPlayer.balance = myPlayer.balance + 80
            print('You now have ' + str(myPlayer.balance) + ' Dollars.')
            prompt2()
    elif myPlayer.location == "Picracko Gallery":
        if myPlayer.prompt == '3':
            myPlayer.completed_quests.append('Find Picracko')
            print('\n'+'Objective completed: Find Picracko')
            myPlayer.quests.remove('Find Picracko')
            myPlayer.balance = myPlayer.balance + 80
            print('You now have ' + str(myPlayer.balance) + ' Dollars.')
            prompt_input()




def military_gun_call():
    print('This is still being developed')
    prompt_input()



def eat_input():
    print('You have ' + str(len(myPlayer.items)) + ' item(s): ' + ', '.join(myPlayer.items))
    action = input('What would you like to eat?'+'\n> ')
    if action.lower() == 'kgb':
        if "KGB" in myPlayer.items:
            myPlayer.items.remove("KGB")
            print("You have eaten a Kenny Good Beet, a subsidiary of the KGB.")
            myPlayer.death_survivability = myPlayer.death_survivability + .01
            print("Your death survivability (how many 'deaths' you can withstand) has increased to "+str(myPlayer.death_survivability)+".")
            prompt_input()
        else:
            print("You do not have this item.")
            prompt_input()
    elif action.lower() == 'omlette':
        if "Omlette" in myPlayer.items:
            myPlayer.items.remove("Omlette")
            print("You shoot an omlette into your face, but before you pulled the trigger, you realised what a bad idea it is. You decide to take the omlette and eat it.")
            myPlayer.death_survivability = myPlayer.death_survivability + .05
            print("Your death survivability (how many 'deaths' you can withstand) has increased to "+str(myPlayer.death_survivability)+".")
            prompt_input()
        else:
            print("You do not have this item.")
            prompt_input()
    elif action.lower() == 'eggchair':
        if "Eggchair" in myPlayer.items:
            myPlayer.items.remove("Eggchair")
            print("You eat an eggchair from a local bakery, the EVB Text Game Shop. It is the best eggchair you have ever had, very sweet, very filling.")
            myPlayer.death_survivability = myPlayer.death_survivability + .08
            print("Your death survivability (how many 'deaths' you can withstand) has increased to "+str(myPlayer.death_survivability)+".")
            prompt_input()
        else:
            print("You don't have this item.")
            prompt_input()
    elif action.lower() == 'moon cheese':
        if "Moon Cheese" in myPlayer.items:
            myPlayer.items.remove("Moon Cheese")
            print("You have eaten moon cheese, fufilling your addiction.")
            myPlayer.death_survivability = myPlayer.death_survivability - .02
            myPlayer.moon_cheese_accomplish[myPlayer.location] = True
            if myPlayer.moon_cheese == False:
                myPlayer.moon_cheese = True
                print("You are now addicted to moon cheese, you must buy and eat moon cheese once per location. Be careful though, because the price will steadily rise over time.")
            print("Your death survivability (how many 'deaths' you can withstand) has decreased to "+str(myPlayer.death_survivability)+".")
            prompt_input()
        else:
            print("You do not have this item.")
            prompt_input()
    elif action.lower() == "bonkhertz split":
        if "Bonkhertz Split" in myPlayer.items:
            myPlayer.items.remove("Bonkhertz Split")
            print("You have eaten bonkhertz split, it is very fulling and raises your death survivability by 1.")
            myPlayer.death_survivability = myPlayer.death_survivability + 1.0
            myPlayer.moon_cheese_accomplish[myPlayer.location] = True
            print("Your death survivability (how many 'deaths' you can withstand) has increased to "+str(myPlayer.death_survivability)+".")
            prompt_input()
        else:
            print("You do not have this item.")
            prompt_input()
    elif action.lower() in ['freeze dried soda','soda']:
        if "Freeze Dried Soda" in myPlayer.items:
            myPlayer.items.remove("Freeze Dried Soda")
            print("You have eaten freeze dried soda.")
            myPlayer.death_survivability = myPlayer.death_survivability + 0.04
            myPlayer.moon_cheese_accomplish[myPlayer.location] = True
            print("Your death survivability (how many 'deaths' you can withstand) has increased to "+str(myPlayer.death_survivability)+".")
            prompt_input()
        else:
            print("You do not have this item.")
            prompt_input()
    elif action.lower() == "quit":
        print("Back to the story.")
        prompt_input()
    while action.lower() not in ['quit','bonkhertz split','freeze dried soda','soda','kgb','moon cheese','eggchair','chocolate cream dessert burrito','omlette']:
        print("That item does not exist or is not edible.")
        eat_input()





def player_eat():
    if 'Eggchair' in myPlayer.items:
        eat_input()
    elif 'Omlette' in myPlayer.items:
        eat_input()
    elif 'KGB' in myPlayer.items:
        eat_input()
    elif 'Moon Cheese' in myPlayer.items:
       eat_input()
    else:
        print("It appears that you haven't unlocked this action yet.")
        prompt_input()





def magic_ball():
    tips_generator = random.choice(TIPS)
    magic_ball_input = input("Do you want to get a tip? (It cost 2 dollars because I said so)\n> ")
    if "Magic 9 Ball" in myPlayer.items:
        if magic_ball_input in ['y','yes',]:
            if myPlayer.balance > 1:
                print("You shake the magic 9 ball and it speaks wisdom to you...\n")
                myPlayer.balance = myPlayer.balance - 2
                for character in tips_generator:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(.02)
                prompt_input()
            else:
                print("You don't have enough money for this tip.")
                prompt_input()
        else:
            print("You did not buy a tip from the magic 9 ball.")
            prompt_input()
    else:
        print("You have not unlocked this command yet.")
        prompt_input()

### EVBREAD ###
EVB = ['"My name is Eddie Van Bonkhertzs. I was born on April 1st, 1919." Hey this guy has your same name! And birthday. Weird.','"I went into the clown business. I had been practicing my upcoming act for a month, and when the opening night came, horror struck. I accidentally crashed the clown car into the elephant, killing 12 out of the 45 clowns on board." I was in a clown car accident just like that! I was safe in the trunk, which had padding. My friends, Jeffery, Larry and Ted, were not so lucky.',
'"When I was a child, I almost bit off my dog. " Really same! He did not taste all that great either ',
'"My father always told me “...”  this simple phrase has changed my very being since I was 3" ',
'" Sadly, although I did live, the clown makeup had seeped into my skin, which now makes me look permanently clown-ish." ',
'"I knew where I was. Russia. I am forbidden to return by order of some guy named "José-ph Stalin"',
'"It is my strong belief that people should get an omletting once in their life, it gives your life perspective for the few seconds you see the egg-based foods hurtling at your face. Your mind enters a deep place and you start asking yourself surreal questions. Like, “How did this happen?” and “What have I done with my life?”"',
'" As the pope face planted on the cobblestones, I ran away and attached the glorious leeeeeeeeeeeeggg to my stump with a half-used super glue bottle I found on the street that said “Colla fusibile Non usare.” Whatever that meant, I didn’t know or care." I have a newspaper from way back when, that has the headline, "Pope faceplants, loses leg."',
'"The SWAT team busted down the door and were oddly surprised to see an unconscious man on the table surrounded by a bunch of medical equipment. They soon questioned me about why I called the police. I said that he had an easily see-able trait, he had arms (that is why I said he was armed, duh). Plus I was told he had undergone a Cadillac arrest and I assumed that he stole the car." This book is genius!',
'" The man looked like someone I had seen before, but I couldn’t place who it was. He turned to me and we both said in unison “The Name’s McOles, Fuick McOles.” I looked at the man for a second and then it dawned on me. “My son!” I said “ I can’t believe you’ve come to visit your mother.” My son looked at me with pure confusion, and said “???”. I looked at the wall, then at the man, then back at the wall, and so on for about an hour. Then I realized that he was my Cat, Gerbils!"',
'"I needed to pay off my medical debt, I decided to start a bouncy castle company. Everybody likes bouncy castles! I thought. I tried to remember what I read in a book about how to start a successful business. “Steal From The Competition!” Was all I remembered. Yeah, I thought, STEAL FROM THE COMPETITION! It worked out nicely since I didn’t have any bouncy castles. So the next night I went to Jimmy, Bob and Ted’s Wonderous Bouncy Castle Rental Store and stole 22 bouncy castles."',
'"When I came out of the bathroom, I looked around for a phone somewhere. on my way to the phone sign I saw in the distance, I finally reached the phone and as I dialed Shoeburt Papadopoulos, I only heard the dial tone. Then I saw the sticker that said 5 cents a call. I fished into my pocket and found my trusty nickel. If only that nickel were a dime, then I could’ve used it. "',
'"I lost my thosuorus (smart word book)"',


]


EVB_buy = [
'"“I’ma fry you!!!” I yelled at the Pizza"',
'" Picracko shouted ‘A Tac’ and all the emus raced inside the house."',
'" The plane burned like a burning plane"',
"And the sun, heh, wow the sun is pretty today…(*screams*)...You better hurry, it appears...that I too, have mysteriously fallen ‘brined’",
"Picracko was smart! He’d find a way out of this mess. He, without speaking, grabbed Gerbils and whacked him on the console table repeatedly.",
"I tooka walk down the mini mall, and overheard a baker and a customer discussing eggchairs and killing a man named ‘FDR’. I walked away from that pretty fast, it sounded like they needed couples counselling. ",
"Had it not been for Sisters Mary, Theresa, and Patricia I may not be telling this story today. They gave their legs for a righteous cause. ",
"I waved to a nearby lady and said, “Good morning Delores!” To which she responded with “M..My name is Debra.”",
"Then, I remembered that the president lived around here, I could’ve gotten me into serious trouble. I got back up to leave when I saw someone in a suit, it was the president, Mr. XYZ!",
" I asked him where the mint was and he said in Washington D.C. “Then why am I going to Wisconsin?!” I asked. He then called me a bunch of mean words and kicked me out the engine room. ",
" My conclusion was that I needed money. Where does one get money? The ground!",
" I heard a sound in the background and immediately hollard OH NO, ITS DA POPO!",













    ]


TIPS = [

    "The command 'evb' can get you a lot or lose you a lot.",
    "Buy a gun and go to the hostage section in the milk store to get something special.",
    "Buying items can unlock other items in the store, so check the buy menu carefully.",
    "A broken dune buggy doesn't have to stay broken. Use the command 'fix dune buggy'.",
    "Buying and eating edible items can be a literal life saver.",
    "Buying EVB Merch, taking the EVB Quiz, and reading EVB give you something special, a great experience. Cheack them all out at eddievanbonkhertz.com. (Yes I promoted the website in a piece of advice.)",
    "The answer to a question isn't always yes.",
    "You can attempt to sell any item you get or buy.",
    "Completed quests can unlock items in the shop and give you money.",
    "If you go to REDACTED for the Who's Leg is this? quest, you will get Stalin's leg.",
    "If you go to Bowling Alley for the Who's Leg is this? quest, you will get Jeff's leg.",
    "If you go to India for the Who's Leg is this? quest, you will get Gandhi's leg.",
    "Grenades can get you more than just an explosion.",
    "Moon Cheese isn't as innocent as it seems.",
    "Omlettes are more than ammo, they are edible too.",
    "Go to eddievanbonkhertz.com/background.html for a secret game code.",













    ]



#### YES/NO ####




def player_yes():
    if myPlayer.prompt == '1':

        location_prompt = myPlayer.prompt_accomplish[myPlayer.location]
        yes_typing = places[myPlayer.location][YES]
        for character in yes_typing:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        variable_prompt = places[myPlayer.location][PROMPT_AFTER]
        add_balance_prompt = places[myPlayer.location][ADD_BALANCE_PROMPT]
        if add_balance_prompt == '1':
            if location_prompt == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance()
        sub_balance_prompt = places[myPlayer.location][SUB_BALANCE_PROMPT]
        if sub_balance_prompt == '1':
            if location_prompt == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance_sub()
        add_balance_prompt2 = places[myPlayer.location][ADD_BALANCE_PROMPT2]
        if add_balance_prompt2 == '1':
            if location_prompt == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance2()
        sub_balance_prompt2 = places[myPlayer.location][SUB_BALANCE_PROMPT2]
        if sub_balance_prompt2 == '1':
            if location_prompt == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance_sub2()
        if places[myPlayer.location][ADD_ITEMS] != '':
            variable_prompt = places[myPlayer.location][PROMPT_AFTER]
            item_prompt = places[myPlayer.location][ADD_ITEMS_PROMPT]
            if item_prompt == '1':
                add_items_prompt = places[myPlayer.location][ADD_ITEMS_PROMPT]
                if add_items_prompt == '1':
                    if location_prompt == True:
                        print('It seems like you already got this item.')
                    if location_prompt != True:
                        print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS] +'.')
                        myPlayer.items.append(places[myPlayer.location][ADD_ITEMS])

                add_items_prompt2 = places[myPlayer.location][ADD_ITEMS2_PROMPT]
                if add_items_prompt2 == '1':
                    if location_prompt == True:
                        print('It seems like you already got this item.')
                    if location_prompt != True:
                        print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS2] +'.')
                        myPlayer.items.append(places[myPlayer.location][ADD_ITEMS2])
                add_items_prompt3 = places[myPlayer.location][ADD_ITEMS3_PROMPT]
                if add_items_prompt3 == '1':
                    if location_prompt == True:
                        print('It seems like you already got this item.')
                    if location_prompt != True:
                        print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS3] +'.')
                        myPlayer.items.append(places[myPlayer.location][ADD_ITEMS3])
        if places[myPlayer.location][ITEMS] != '':
            print('\n'+'You have lost ' + places[myPlayer.location][ITEMS] +'.')
            myPlayer.items.remove(places[myPlayer.location][ITEMS])
        next_prompt = places[myPlayer.location][NEXT_PROMPT]
        if next_prompt == '1':
            if myPlayer.moon_cheese == True:
                if myPlayer.moon_cheese_accomplish[myPlayer.location] == False:
                    print('\n'+'\n'+"You did not fufill your moon cheese addiction, you died. (You must eat moon cheese once per area)")
                    restart(4)
            myPlayer.location = places[myPlayer.location][NEXT]
            print('\n'+'You are now in ' + myPlayer.location + '.')
            if places[myPlayer.location][QUEST_PROMPT] == '1':
                if places[myPlayer.location][QUEST] != '':
                    print('You have a new objective: '+ places[myPlayer.location][QUEST])
                    myPlayer.quests.append(places[myPlayer.location][QUEST])
        if places[myPlayer.location][QUEST_PROMPT] == '1':
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
        location_prompt = True
        quest_complete()
        if variable_prompt != '':
            if variable_prompt == '3':
                prompt3()
            elif variable_prompt == '2':
                prompt2()
            elif variable_prompt == '1':
                prompt()
            elif variable_prompt == '0':
                prompt_input()










    elif myPlayer.prompt == '2':
        yes_description2 = places[myPlayer.location][YES2]
        for character in yes_description2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        variable_prompt = places[myPlayer.location][PROMPT_AFTER2]
        location_prompt2 = myPlayer.prompt_accomplish2[myPlayer.location]
        add_balance_prompt = places[myPlayer.location][ADD_BALANCE_PROMPT]
        if add_balance_prompt == '2':
            if location_prompt2 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance()
        sub_balance_prompt = places[myPlayer.location][SUB_BALANCE_PROMPT]
        if sub_balance_prompt == '2':
            if location_prompt2 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance_sub()
        add_balance_prompt2 = places[myPlayer.location][ADD_BALANCE_PROMPT2]
        if add_balance_prompt2 == '2':
            if location_prompt2 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance2()
        sub_balance_prompt2 = places[myPlayer.location][SUB_BALANCE_PROMPT2]
        if sub_balance_prompt2 == '2':
            if location_prompt2 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance_sub()
        item_prompt = places[myPlayer.location][ADD_ITEMS2_PROMPT]
        if item_prompt == '2':
                add_items_prompt = places[myPlayer.location][ADD_ITEMS_PROMPT]
                if add_items_prompt == '2':
                    if location_prompt2 == True:
                        print('It seems like you already got this item.')
                    if location_prompt2 != True:
                        print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS] +'.')
                        myPlayer.items.append(places[myPlayer.location][ADD_ITEMS])
                add_items_prompt2 = places[myPlayer.location][ADD_ITEMS2_PROMPT]
                if add_items_prompt2 == '2':
                    if location_prompt2 == True:
                        print('It seems like you already got this item.')
                    if location_prompt2 != True:
                        print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS2] +'.')
                        myPlayer.items.append(places[myPlayer.location][ADD_ITEMS2])
                add_items_prompt3 = places[myPlayer.location][ADD_ITEMS3_PROMPT]
                if add_items_prompt3 == '2':
                    if location_prompt2 == True:
                        print('It seems like you already got this item.')
                    if location_prompt2 != True:
                        print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS3] +'.')
                        myPlayer.items.append(places[myPlayer.location][ADD_ITEMS3])
        if places[myPlayer.location][ITEMS2] != '':
            print('\n'+'You have lost ' + places[myPlayer.location][ITEMS2] +'.')
            myPlayer.items.remove(places[myPlayer.location][ITEMS2])
        next_prompt = places[myPlayer.location][NEXT_PROMPT]
        if next_prompt == '2':
            if myPlayer.moon_cheese == True:
                if myPlayer.moon_cheese_accomplish[myPlayer.location] == False:
                    print("\n\n"+"You did not fufill your moon cheese addiction, you died. (You must eat moon cheese once per area)")
                    restart(4)
            location_prompt2 = True
            myPlayer.location = places[myPlayer.location][NEXT]
            print('\n'+'You are now in ' + myPlayer.location + '.')
        if places[myPlayer.location][QUEST_PROMPT] == '2':
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
        quest_complete()
        location_prompt2 = True
        if variable_prompt != '':
            if variable_prompt == '3':
                prompt3()
            elif variable_prompt == '2':
                prompt2()
            elif variable_prompt == '1':
                prompt()
            elif variable_prompt == '0':
                prompt_input()





    elif myPlayer.prompt == '3':
        yes_description3 = places[myPlayer.location][YES3]
        for character in yes_description3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        if myPlayer.location == 'Picracko Gallery':
            if myPlayer.death_survivability >= 1:
                print("\nYou have avoided death this time, here is a redo.")
                myPlayer.death_survivability = myPlayer.death_survivability -1
                prompt3()
            elif myPlayer.death_survivability <1:
                restart(10)
        if myPlayer.location == 'India':
            if myPlayer.death_survivability >= 1:
                print("\nYou have avoided death this time, here is a redo.")
                myPlayer.death_survivability = myPlayer.death_survivability -1
                prompt3()
            elif myPlayer.death_survivability <1:
                restart(6)
        if myPlayer.location == "The Casino":
            myPlayer.items.remove("Bag of Chips")
        variable_prompt = places[myPlayer.location][PROMPT_AFTER3]
        location_prompt3 = myPlayer.prompt_accomplish3[myPlayer.location]
        add_balance_prompt = places[myPlayer.location][ADD_BALANCE_PROMPT]
        if add_balance_prompt == '3':
            if location_prompt3 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance()
        sub_balance_prompt = places[myPlayer.location][SUB_BALANCE_PROMPT]
        if sub_balance_prompt == '3':
            if location_prompt3 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance_sub()
        add_balance_prompt2 = places[myPlayer.location][ADD_BALANCE_PROMPT2]
        if add_balance_prompt2 == '3':
            if location_prompt3 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance2()
        sub_balance_prompt2 = places[myPlayer.location][SUB_BALANCE_PROMPT2]
        if sub_balance_prompt2 == '3':
            if location_prompt3 == True:
                print("It looks like you have already completed this prompt.")
                if variable_prompt != '':
                    if variable_prompt == '3':
                        prompt3()
                    elif variable_prompt == '2':
                        prompt2()
                    elif variable_prompt == '1':
                        prompt()
                    elif variable_prompt == '0':
                        prompt_input()
            else:
                player_balance_sub2()
        item_prompt = places[myPlayer.location][ADD_ITEMS3_PROMPT]
        if item_prompt == '3':
            add_items_prompt = places[myPlayer.location][ADD_ITEMS_PROMPT]
            if add_items_prompt == '3':
                if location_prompt3 == True:
                    print('It seems like you already got this item.')
                if location_prompt3 != True:
                    print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS] +'.')
                    myPlayer.items.append(places[myPlayer.location][ADD_ITEMS])
            add_items_prompt2 = places[myPlayer.location][ADD_ITEMS2_PROMPT]
            if add_items_prompt2 == '3':
                if location_prompt3 == True:
                    print('It seems like you already got this item.')
                if location_prompt3 != True:
                    print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS2] +'.')
                    myPlayer.items.append(places[myPlayer.location][ADD_ITEMS2])
            add_items_prompt3 = places[myPlayer.location][ADD_ITEMS3_PROMPT]
            if add_items_prompt3 == '3':
                if location_prompt3 == True:
                    print('It seems like you already got this item.')
                if location_prompt3 != True:
                    print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS3] +'.')
                    myPlayer.items.append(places[myPlayer.location][ADD_ITEMS3])
        if places[myPlayer.location][ITEMS3] != '':
            print('\n'+'You have lost ' + places[myPlayer.location][ITEMS3] +'.')
            myPlayer.items.remove(places[myPlayer.location][ITEMS3])
        next_prompt = places[myPlayer.location][NEXT_PROMPT]
        if next_prompt == '3':
            if myPlayer.moon_cheese == True:
                if myPlayer.moon_cheese_accomplish[myPlayer.location] == False:
                    print('\n'+'\n'+"You did not fufill your moon cheese addiction, you died. (You must eat moon cheese once per area)")
                    restart(4)
            location_prompt3 = True
            myPlayer.location = places[myPlayer.location][NEXT]
            print('\n' +'You are now in ' + myPlayer.location + '.')
        if places[myPlayer.location][QUEST_PROMPT] == '3':
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
        quest_complete()
        location_prompt3 = True
        if variable_prompt != '':
            if variable_prompt == '3':
                prompt3()
            elif variable_prompt == '2':
                prompt2()
            elif variable_prompt == '1':
                prompt()
            elif variable_prompt == '0':
                prompt_input()














def hidden_yes():
    hidden_item = places[myPlayer.location][HIDDEN_ITEMS]
    yes_hidden = places[myPlayer.location][HIDDENYES]
    for character in yes_hidden:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    location_prompt = myPlayer.hidden_accomplish[myPlayer.location]
    if places[myPlayer.location][HIDDEN_ITEMS] != '':
        if location_prompt == False:
            if hidden_item not in myPlayer.items:
                print('\n'+'You have acquired ' + places[myPlayer.location][HIDDEN_ITEMS] +'.')
                myPlayer.items.append(places[myPlayer.location][HIDDEN_ITEMS])
                prompt_input()
            else:
                print('\n'+"You already have this item.")
                prompt_input()
        if location_prompt == True:
            print('It seems like you already got this item.')
            prompt_input()
    if places[myPlayer.location][HIDDEN_BALANCE] != '':
        if location_prompt == False:
            myPlayer.balance = myPlayer.balance + places[myPlayer.location][HIDDEN_BALANCE]
            print('\n'+'You now have ' + str(myPlayer.balance) +'.')
            prompt_input()
        else:
            print('It seems like you already got this money.')
            prompt_input()
    if places[myPlayer.location][HIDDENITEMS] != '':
        print('\n'+'You have lost ' + places[myPlayer.location][HIDDENITEMS] +'.')
        myPlayer.items.remove(places[myPlayer.location][HIDDENITEMS])
    if places[myPlayer.location][HIDDEN_QUEST] != '':
        print('You have a new objective: '+ places[myPlayer.location][HIDDEN_QUEST])
        myPlayer.quests.append(places[myPlayer.location][HIDDEN_QUEST])
    quest_complete()
    myPlayer.hidden_accomplish[myPlayer.location] == True






def player_no():
    if myPlayer.prompt == '1':
        if myPlayer.death_survivability < 1:
            death_description = places[myPlayer.location][NO]
            for character in death_description:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.02)
            restart(5)
        elif myPlayer.death_survivability >= 1:
            print("\nYou have avoided death this time, because of your death survivablility, here is a redo.")
            myPlayer.death_survivability = myPlayer.death_survivability -1
            prompt()







    elif myPlayer.prompt == '2':
        if myPlayer.death_survivability < 1:
            death_description2 = places[myPlayer.location][NO2]
            for character in death_description2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.02)
            restart(5)
        elif myPlayer.death_survivability >= 1:
            print("\nYou have avoided death this time, here is a redo.")
            myPlayer.death_survivability = myPlayer.death_survivability -1
            prompt2()


    elif myPlayer.prompt == '3':
        death_description3 = places[myPlayer.location][NO3]
        for character in death_description3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        quest_complete()
        if places[myPlayer.location][ADD_ITEMS3_NO] != '':
            if places[myPlayer.location][ADD_ITEMS3_NO] in myPlayer.items:
                print('It seems like you already have this item.')
                prompt_input()
            if places[myPlayer.location][ADD_ITEMS3_NO] not in myPlayer.items:
                print('\n'+'You have acquired ' + places[myPlayer.location][ADD_ITEMS3_NO] +'.')
                myPlayer.items.append(places[myPlayer.location][ADD_ITEMS3_NO])
        if places[myPlayer.location][ITEMS3_NO] != '':
            print('\n'+'You have lost ' + places[myPlayer.location][ITEMS3_NO] +'.')
            myPlayer.items.remove(places[myPlayer.location][ITEMS3_NO])
        add_balance_prompt = places[myPlayer.location][ADD_BALANCE_PROMPT]
        if add_balance_prompt == '3':
            player_balance_no()
        sub_balance_prompt = places[myPlayer.location][SUB_BALANCE_PROMPT]
        if sub_balance_prompt == '3':
            player_balance_sub_no()
        if places[myPlayer.location][NEXT_PROMPT] == '3':
            myPlayer.prompt_accomplish3[myPlayer.location] = True
            myPlayer.location = places[myPlayer.location][NEXT]
            print('\n' +'You are now in ' + myPlayer.location + '.')
            if places[myPlayer.location][QUEST] != '':
                print('You have a new objective: '+ places[myPlayer.location][QUEST])
                myPlayer.quests.append(places[myPlayer.location][QUEST])
        variable_prompt = myPlayer.prompt
        myPlayer.prompt_accomplish3[myPlayer.location] == True
        if variable_prompt == '3':
            prompt3()
        elif variable_prompt == '2':
            prompt2()
        elif variable_prompt == '1':
            prompt()
        elif variable_prompt == '0':
            prompt_input()








def hidden_no():
    death_hidden = places[myPlayer.location][HIDDENNO]
    variable_prompt = places[myPlayer.location][PROMPT_AFTER3]
    for character in death_hidden:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    if places[myPlayer.location][HIDDEN_ITEMS_NO] != '':
        if location_prompt == False:
            print('\n'+'You have acquired ' + places[myPlayer.location][HIDDEN_ITEMS_NO] +'.')
            myPlayer.items.append(places[myPlayer.location][HIDDEN_ITEMS_NO])
    if places[myPlayer.location][HIDDEN_BALANCE_NO] != '':
        if location_prompt == False:
            myPlayer.balance = myPlayer.balance + places[myPlayer.location][HIDDEN_BALANCE_NO]
            print('\n'+'You now have ' + myPlayer.balance +'.')
            prompt_input()
        else:
            print('It seems like you already got this money.')
            prompt_input()
    if places[myPlayer.location][HIDDENITEMS] != '':
        print('\n'+'You have lost ' + places[myPlayer.location][HIDDENITEMS] +'.')
        myPlayer.items.remove(places[myPlayer.location][HIDDENITEMS])
    if variable_prompt == '3':
        prompt3()
    elif variable_prompt == '2':
        prompt2()
    elif variable_prompt == '1':
        prompt()
    elif variable_prompt == '0':
        prompt_input()
    elif myPlayer.location == 'Gas Station':
        restart(5)

### START GAME ###

def start_game():
    os.system('clear')
    myPlayer.location = 'Gas Station'
    question1 = 'Hello! It appears that you have amnesia. '
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)



    question2 = "Your name is Eddie Van Bonkhertz, or EVB for short. You are the world's greatest idiot. "
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    question3 = "In you pocket is a tattered copy of book called 'True Memoirs of a Disgraced Clown'. You remember seeing it fall out of a portal or something. It appears to be missing pages. "
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    question4 = "Let me walk you through the first location. Whenever you enter a new location, type 'look' to get a description and help to see further actions, such as left and right descriptions."
    for character in question4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    prompt_input()





##### PROMPT STATION #####


def prompt_input():
    swears_list = ['fuck','shit','poop','bitch',]
    action = input('\n' + '> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'help':
        instruction_menu()
    elif action.lower() in ['y','yes']:
        player_yes()
    elif action.lower() in ['n', 'no']:
        player_no()
    elif action.lower() == 'loc':
        print_location()
        prompt_input()
    elif action.lower() == 'location':
        print_location()
        prompt_input()
    elif action.lower() in ['name',"what's my name"]:
        print("Really, you've forgotten your name? Again?" + " Your name is "+ str(myPlayer.name) +".")
        prompt_input()
    elif action.lower() in ['look','look around']:
        if myPlayer.location == 'The Casino':
            casino_look()
        else:
            player_look()
    elif action.lower() in ['right',"what's to the right","what's to the right?"]:
        player_right()
    elif action.lower() in ['left', "what's to the left", "what's to the left?"]:
        player_left()
    elif action.lower() == 'restart':
        restart_game()
    elif action.lower() == 'items':
        items_print()
        prompt_input()
    elif action.lower() == 'read':
        player_read()
        prompt_input()
    elif action.lower() == 'play':
        if myPlayer.location == 'Title Screen':
            start_game()
        else:
            print("You are already in the game. Here are some symptoms of dementia: memory problems, particularly remembering recent events, increasing confusion, reduced concentration, personality or behaviour changes, apathy and withdrawal or depression, loss of ability to do everyday tasks.")
            prompt_input()
    elif action.lower() == 'evb':
        hidden_prompt()
    elif action.lower() == 'outside':
        print_outside()
    elif action.lower() == 'back':
        if 'Emu' in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                print('You cannot go back, this is the literal beginning of the game.')
                prompt_input()
            else:
                player_back()
        elif 'Clown Car' in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                print('You cannot go back, this is the literal beginning of the game.')
                prompt_input()
            else:
                player_back()
        elif 'Sailboat' in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                print('You cannot go back, this is the literal beginning of the game.')
                prompt_input()
            else:
                player_back()
        elif ['KGB Army','KGB Horde','KGB Platoon'] in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                print('You cannot go back, this is the literal beginning of the game.')
                prompt_input()
            else:
                player_back()

    elif action.lower() == 'next':
        if 'Emu' in myPlayer.items:
            if myPlayer.location == 'End Screen':
                print ('This is the end of the game, you cannot go forward more. Can you read?')
                prompt_input()
            else:
                player_next()
        elif 'Clown Car' in myPlayer.items:
            if myPlayer.location == 'End Screen':
                print ('This is the end of the game, you cannot go forward more. Can you read?')
                prompt_input()
            else:
                player_next()
        elif ['KGB Army','KGB Horde',] in myPlayer.items:
            if myPlayer.location == 'End Screen':
                print ('This is the end of the game, you cannot go forward more. Can you read?')
                prompt_input()
            else:
                player_next()
        elif 'Sailboat' in myPlayer.items:
            if myPlayer.location == 'End Screen':
                print ('This is the end of the game, you cannot go forward more. Can you read?')
                prompt_input()
            else:
                player_next()
    elif action.lower() == 'balance':
        print_balance()
    elif action.lower() == 'bal':
        print_balance()
    elif action.lower() == 'shop':
        player_store()
    elif action.lower() == 'sell':
        player_sell()
    elif action.lower() == 'store':
        player_store()
    elif action.lower() == 'buy':
        player_buy()
    elif action.lower() == 'boom':
        boom()
    elif action.lower() == 'military gun call':
        military_gun_call()
    elif action.lower() == 'mgc':
        military_gun_call()
    elif action.lower() == 'eat':
        player_eat()
    elif action.lower() == 'oml':
        omlette()
    elif action.lower() == 'russia':
        read_russia_book()
    elif action.lower() == 'dev':
        print("Nice try, Nick!")
        prompt_input()
        prompt_input()
    elif action.lower() == 'hostage':
        if myPlayer.location == 'Milk Store':
            if 'Gun' in myPlayer.items:
                print("You follow the signs to the hostage section and ask if they have any milk. One of them whispers to you, 'Go call the police.' Only half listening, you respond, 'Yeah sure, I just need to grab some milk because some text in a game told me I had to.' You try to fistbump them, but they keep their ands in the air for some reason. You were about to walk over to the produce section, when a man with a gun pointed at you told you to put your hands up. Oh, you thought, he was preparing for a military gun call. You pull out your gun and do a military gun call at him. Almost immediately, he starts putting down his weapon.'You're a veteran too?' He asked. You respond yes, and that you were trying to find the milk. He gives you a piece of Stalin's hair he got during the war, a fistbump, and points you toward the dairy isle. ")
                myPlayer.items.append("Stalin's Hair")
                myPlayer.taken_items.append("Stalin's Hair")
                print("You have aquired Stalin's Hair.")
                print("You reach the dairy isle and found the Milk fridge. You pick the cheapest milk they have, and walk back to the entrance, to the cashier and asked her to wring it up. She totals it 35 cents. You buy the milk.")
                print('You have aquired Milk.')
                myPlayer.items.append("Milk")
                myPlayer.taken_items.append("Milk")
                myPlayer.prompt_accomplish[myPlayer.location] = True
                myPlayer.balance = myPlayer.balance - .35
                prompt2()
            elif myPlayer.death_survivability >= 1:
                print("You survived death this time, but your death survivability has decreased.")
                myPlayer.death_survivability = myPlayer.death_survivability - 1
                prompt_input()
            else:
                print("You follow the sign to the hostage section and ask if they have any milk. One of them whispers to you, 'Go call the police.' Only half listening, you respond, 'Yeah sure, I just need to grab some milk because some text in a game told me I had to.' You try to fistbump them, but they keep their ands in the air for some reason. You were about to walk over to the produce section, when a man with a gun pointed at you told you to put your hands up. Oh, you thought, he was preparing for a military gun call. If only you had a gun to signal at him. You try to ask him where the milk is, but he shoots you by accident. Please restart.")
                restart(30)
        else:
            print("That command doesn't work here")
    elif action.lower() == 'produce':
        if myPlayer.location == 'Milk Store':
            if myPlayer.death_survivability >= 1:
                print("You survived death this time, but your death survivability has decreased.")
                myPlayer.death_survivability = myPlayer.death_survivability - 1
                prompt_input()
            else:
                print("You walk to the produce isle and forget what you came here for, so you walk out the store with a rotten tomato without paying. You take a bite and fall flat on the groud, not because it was rotten, but because you're allergic to tomatoes. Who knew? Not you apparently, because you just died. ")
                restart(10)
        else:
            print("That command doesn't work here")
    elif action.lower() == 'dairy':
        if myPlayer.location == 'Milk Store':
            print("You reach the dairy isle and found the Milk fridge. You pick the cheapest milk they have, and walk back to the entrance, to the cashier and asked her to wring it up. She totals it 35 cents. You buy the milk.")
            myPlayer.prompt_accomplish[myPlayer.location] = True
            myPlayer.items.append("Milk")
            myPlayer.taken_items.append("Milk")
            myPlayer.balance = myPlayer.balance - .35
            prompt2()
        else:
            print("That command doesn't work here")
    elif action.lower() == 'quests':
        quest_print()
        prompt_input()
    elif action.lower() == 'left wing':
        if myPlayer.location == 'Picracko Gallery':
            if myPlayer.death_survivability >= 1:
                print("You survived death this time, but your death survivability has decreased.")
                myPlayer.death_survivability = myPlayer.death_survivability - 1
                prompt_input()
            else:
                print("You walk into the left wing and find nothing but a computer. Intruiged, you sit in the chair and turn it on. On it is the picracko website, with awful art pieces. (Visable if you go to the EVB website and click on the story title on the story page). One about the song 'Banana Boat' is so awful, you try to leave the chair, but it straped you in and the computer shocks you. You died. Restart.")
                restart(10)
        else:
            print("That command doesn't work here")
    elif action.lower() == 'right wing':
        if myPlayer.location == 'Picracko Gallery':
            print("You walk into the right wing and see the walls covered in horrid paintings. You don't see Picracko anywhere. You decide to make the most of your time there. These paintings would be worth alot...")
            prompt2()
        else:
            print("That command doesn't work here")
    elif action.lower() in swears_list:
        print("You're so mature! You can't tell because it is a text game, but I rolled my eyes so hard, they fell out of their sockets.")
        prompt_input()
    elif action.lower() == 'kill':
        print("Stop it Graham.")
        prompt_input()
    elif action.lower() == 'loli':
        print("Pascal, I swear to god. Just for that, you have to restart.")
        restart(6)
    elif action.lower() == 'bet':
        bet_print = "Bet." * 1000
        for character in bet_print:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.001)
        prompt_input()
    elif action.lower() == 'omlette':
        print('You have '+ str(myPlayer.omlettes) + ' omlette(s).')
        prompt_input()
    elif action.lower() == 'grenade':
        print('You have '+str(myPlayer.grenades)+' grenade(s).')
        prompt_input()
    elif action.lower() == 'completed quests':
        completed_quest_print()
    elif action.lower() == 'clear':
        os.system('clear')
        prompt_input()
    elif action.lower() == 'characters':
        characters_print()
    elif action.lower() == 'tmdc':
        if myPlayer.tmdc != True:
            myPlayer.completed_quests.append("Summon Stalin")
            myPlayer.items.append('Emu')
            myPlayer.balance = myPlayer.balance + (100*10*10*10*10)
            myPlayer.tmdc = True
            myPlayer.items.append("Moon Cheese")
            prompt_input()
        else:
            print("Screw you pascal. You too Avi. And you Nick! One per customer.")
            prompt_input()
        prompt_input()
    elif action.lower() == 'shark':
        print("You wlak into the shark exhibit, but your leg scraped on some rusty metal, and you go to the hospital and are diagnosed with Tetanus, and your leg had to be amputated. Worst part is, you never got to see the sharks.")
        prompt2()
    elif action.lower() == 'harmless fish':
        print("You walk over to the oddly named Harmless Fish section. You become separated from Picracko, and go into the employee door by mistake. The door led into a slippery dock in the aquarium. You walk onto the dock, but slip and fall into the water with the fish. Your leg is brutally eaten off in 2 seconds flat. Terrified, you climb back up on the dock and slowly exit the employee area, limping through the door. After collapsing, you are rushed to the hospital, where you awake, no longer bleeding. ")
        prompt2()
    elif action.lower() == 'communism':
        myPlayer.completed_quests.append("Summon Stalin")
        prompt_input()
    elif action.lower() == "bowling alley":
        if myplayer.location == "Payphone":
            myPlayer.location = "Bowling Alley"
            myPlayer.prompt_accomplish2[myPlayer.location] = True
            print("You choose to see what kind of legs you can spot at the local bowling alley. You are now in Bowling Alley.")
            prompt_input()
        else:
            print("That command does not work here.")
            prompt_input()
    elif action.lower() == "redacted":
        if myPlayer.location == "Payphone":
            myPlayer.location = "REDACTED, Russia"
            myPlayer.prompt_accomplish2[myPlayer.location] = True
            print("You chose to hunt for a famous persons leg. What famous people came from Russia? You are now in REDACTED, Russia.")
            prompt_input()
        else:
            print("That command does not work here.")
            prompt_input()
    elif action.lower() == "india":
        if myPlayer.location == "Payphone":
            myPlayer.prompt_accomplish2[myPlayer.location] = True
            myPlayer.location = "India"
            print("You decide to try to find a famous political influencer from India to take a leg from.")
            prompt_input()
        else:
            print("That command does not work here.")
            prompt_input()
    elif action.lower() == "picracko":
        if myPlayer.location == "Payphone":
            print("You are about to call Picracko when he tells you to stop messing around. You must've forgotten he was still with you.")
            print("Do you want to call Picracko, Fuick, Shoeburt, Gerbils, or Eddie?")
            prompt_input()
        else:
            print("That command doesn't work here.")
            prompt_input()
    elif action.lower() == "gerbils":
        if myPlayer.location == "Payphone":
            print("You call Gerbils, but all you hear is a dial tone. Weeping, you hang up the phone.")
            print("Do you want to call Picracko, Fuick, Shoeburt, Gerbils, or Eddie?")
            prompt_input()
        else:
            print("That command doesn't work here.")
            prompt_input()
    elif action.lower() == "shoeburt":
        if myPlayer.location == "Payphone":
            print("You call Shoeburt and they suggest that you either go to a place like a bowling alley and steal a random persons leg, or go for someone famous from Russia or India. ")
            prompt3()
        else:
            print("That command doesn't work here.")
            prompt_input()
    elif action.lower() == "fuick":
        if myPlayer.location == "Payphone":
            print("You call your brother Fuick's phone number in australia. You hear loud Emu screeches and noises.")
            print("Do you want to call Picracko, Fuick, Shoeburt, Gerbils, or Eddie?")
            prompt_input()
        else:
            print("That command doesn't work here.")
            prompt_input()
    elif action.lower() == "eddie":
        if myPlayer.location == "Payphone":
            print("You call your old home phone. 'Hello, my name is Eddie Van Bonkhertz, what can I do for you?' It was in your exact same voice. You scream and hang up the phone. ")
            print("Do you want to call Picracko, Fuick, Shoeburt,Gerbils or Eddie?")
            prompt_input()
        else:
            print("That command doesn't work here.")
            prompt_input()
    elif action.lower() == 'shake':
        magic_ball()
    elif action.lower() == "painting":
        picracko_original()
    elif action.lower() == 'h2z456d':
        if myPlayer.h2z456d == False:
            print("Congrats on getting the code! Here is 10000 Dollars, an omletting gun and 4 omlettes.")
            myPlayer.balance = myPlayer.balance + 10000
            myPlayer.items.append("Omletting Gun")
            myPlayer.items.append("Omlette")
            myPlayer.items.append("Omlette")
            myPlayer.items.append("Omlette")
            myPlayer.items.append("Omlette")
            myPlayer.h2z456d = True
            prompt_input()
        else:
            print("You already have used this prompt.")
            prompt_input()
    acceptable_actions = ['h2z456d','painting','shake','eddie','picracko','gerbils','shoeburt','fuick','redacted','bowling alley','india','communism','shark','harmless fish','fish','characters','quests','clear','completed quests','grenade','oml','fuck','shit','poop','bitch','bet','loli','kill','info','left wing','right wing','quests','dairy','produce','hostage','dev','russia','omlette','eat','mgc','military gun call','tmdc','boom','buy','prompts','store','sell','shop','bal','balance','next','back','evb','play','read','items','look','name',"what's my name",'location','loc','where am i','quit','help','y','yes','n','no', 'right',"what's to the right","what's to the right?", 'left', "what's to the left", "what's to the left?", 'restart', places[myPlayer.location][ACTIONS]]
    while action.lower() not in acceptable_actions:
        Action_help = "You are unaware of what to do. Try a different command. (Type help for a list of actions)" + '\n'
        for character in Action_help:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        prompt_input()




















def hidden_input():
    action = input('\n' + '> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'help':
        instruction_menu()
    elif action.lower() in ['y','yes']:
        hidden_yes()
    elif action.lower() in ['n', 'no']:
        hidden_no()
    elif action.lower() == 'loc':
        print_location()
        prompt_input()
    elif action.lower() == 'location':
        print_location()
        prompt_input()
    elif action.lower() in ['name',"what's my name"]:
        print("Really, you've forgotten your name? Again?" + "Your name is "+ str(myPlayer.name) +".")
        prompt_input()
    elif action.lower() in ['look','look around']:
        if myPlayer.location == 'The Casino':
            casino_look()
        else:
            player_look()
    elif action.lower() in ['right',"what's to the right","what's to the right?"]:
        player_right()
    elif action.lower() in ['left', "what's to the left", "what's to the left?"]:
        player_left()
    elif action.lower() == 'restart':
        restart_game()
    elif action.lower() == 'items':
        items_print()
        prompt_input()
    elif action.lower() == 'read':
        player_read()
        prompt_input()
    elif action.lower() == 'play':
        if myPlayer.location == 'Title Screen':
            start_game()
        else:
            print("You are already in the game. Here are some symptoms of dementia: memory problems, particularly remembering recent events, increasing confusion, reduced concentration, personality or behaviour changes, apathy and withdrawal or depression, loss of ability to do everyday tasks.")
            prompt_input()
    elif action.lower() == 'evb':
        hidden_prompt()
    elif action.lower() == 'outside':
        print_outside()
    elif action.lower() == 'back':
        if 'Broken Dune-Buggy' in myPlayer.items:
            player_back()
        if 'Emu' in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                print('You cannot go back, this is the literal beginning of the game.')
                prompt_input()
            else:
                player_back()
        elif 'Clown Car' in myPlayer.items:
            if myPlayer.location == 'Title Screen':
                print('You cannot go back, this is the literal beginning of the game.')
                prompt_input()
            else:
                player_back()
    elif action.lower() == 'next':
        if 'Emu' in myPlayer.items:
                if myPlayer.location == 'End Screen':
                    print ('This is the end of the game, you cannot go forward more. Can you read?')
                    prompt_input()
                else:
                    player_next()
        elif 'Clown Car' in myPlayer.items:
            if myPlayer.location == 'End Screen':
                print ('This is the end of the game, you cannot go forward more. Can you read?')
                prompt_input()
            else:
                player_next()
    elif action.lower() == 'balance':
        print_balance()
    elif action.lower() == 'bal':
        print_balance()
    elif action.lower() == 'shop':
        player_store()
    elif action.lower() == 'sell':
        player_sell()
    elif action.lower() == 'store':
        player_store()
    elif action.lower() == 'buy':
        player_buy()
    elif action.lower() == 'boom':
        boom()
    elif action.lower() == 'military gun call':
        military_gun_call()
    elif action.lower() == 'mgc':
        military_gun_call()
    elif action.lower() == 'eat':
        player_eat()
    elif action.lower() == 'oml':
        omlette()
    elif action.lower() == 'russia':
        read_russia_book()
    elif action.lower() == 'dev':
        print("Nice try, Nick!")
        prompt_input()
    elif action.lower() == 'quests':
        print(myPlayer.quests)
        prompt_input()
    elif action.lower() == 'omlette':
        print('You have '+ str(myPLayer.omlettes) + ' omlettes.')
        prompt_input()
    elif action.lower() == 'grenade':
        print('You have '+str(myPlayer.grenades)+' grenades.')
        prompt_input()
    elif action.lower() == 'completed quests':
        print(myPlayer.completed_quests)
    elif action.lower() == 'h2z456d':
        if myPlayer.h2z456d == False:
            print("Congrats on getting the code! Here is 10000 Dollars, an omletting gun and 4 omlettes.")
            myPlayer.balance = myPlayer.balance + 10000
            myPlayer.items("Omletting Gun")
            myPlayer.items("Omlette")
            myPlayer.items("Omlette")
            myPlayer.items("Omlette")
            myPlayer.items("Omlette")
            myPlayer.h2z456d = True
        else:
            print("You already have used this prompt.")
            prompt_input()
    acceptable_actions = ['h2z456d','completed quests','grenade','oml','quests','dev','russia','omlette','eat','mgc','military gun call','boom','store','sell','shop','bal','balance','next','back','evb','play','read','items','look','name',"what's my name",'location','loc','where am i','quit','help','y','yes','n','no', 'right',"what's to the right","what's to the right?", 'left', "what's to the left", "what's to the left?",'tmdc', 'restart', places[myPlayer.location][ACTIONS]]
    while action.lower() not in acceptable_actions:
        Action_help = "You are unaware of what to do. Try a different command. (Type help for a list of actions)" + '\n'
        for character in Action_help:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        hidden_prompt()















def prompt():
    print('\n')
    question = places[myPlayer.location][PROMPT]
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    myPlayer.prompt = '1'
    if myPlayer.moon_cheese == True:
        print("Remember to eat a gallon of Moon Cheese before you leave this location, to fufil your Moon Cheese addiction.")
    prompt_input()

def prompt2():
    print("\n")
    question = places[myPlayer.location][PROMPT2]
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    myPlayer.prompt = '2'
    prompt_input()


def prompt3():
    print("\n")
    question = places[myPlayer.location][PROMPT3]
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    myPlayer.prompt = '3'
    prompt_input()

def hidden_prompt():
    print("\n")
    question = places[myPlayer.location][HIDDENPROMPT]
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    hidden_input()










#### TITLE SCREENS ####
def instruction_menu():
    print('#################################################')
    print('#               -   Commands   -                #')
    print('#         Quit -  Use to exit the game          #')
    print('#        Help - Use to get to this menu         #')
    print('#        Y or Yes - Use to answer Yes           #')
    print('#         N or No - Use to answer No            #')
    print('#        Loc - Use to find your location        #')
    print('#        Name - Use to find out your name       #')
    print('#        Look - Use to get descriptions         #')
    print('#    Right - Use to get descriptions (right)    #')
    print('#     Left - Use to get decriptions (left)      #')
    print('#       Restart - Use to restart the game       #')
    print('#    Items - Use to get a list of your items    #')
    print('#  Outside - Get descriptions for the outside   #')
    print('#    Bal - Use to go to check your balance      #')
    print("#    Quests - Use to check your active quests   #")
    print('#        Shop - Use to open the shop            #')
    if 'Plush Grenade' in myPlayer.items:
        print('#   Boom - Use to blow up the area you are in   #')
    if 'Omlette' in myPlayer.items:
        print('#  Oml - Use to olmette up the area you are in  #')
    print("# Grenade - Use to check the number of grenades #")
    print("#   that you have.                              #")
    print("#  Omlette -Use to check the number of omlettes #")
    print("#  that you have.                               #")
    print("# Completed Quests - Use to check the quests y- #")
    print("#  ou have completed.                           #")
    print('#     Read - Use to read excerpts from the      #')
    print('# holy book, True Memoirs Of A Disgraced Clown. #')
    print('#################################################')
    prompt_input()


def title_screen():
    os.system('clear')
    print('#################################')
    print('# Welcome to the EVB Text Game! #')
    print('#################################')
    print('            - Play -             ')
    print('            - Help -             ')
    print('            - Quit -             ')
    print('  Copyright 2019 EVB Publishing  ')
    print('\n'+'You have a new objective: Getting Started')
    myPlayer.quests.append('Getting Started')
    prompt_input()






title_screen()



























