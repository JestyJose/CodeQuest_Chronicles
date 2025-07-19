import random
def generate_story(challenge_tye):
    intro=[
        "Welcome, brave coder! Your next question awaits:",
        "Greetings, Code Warrior. Prepare for battle:",
        "The realm of bugs is restless.Time to act:"
        ]
    scenarios={
        "loops":[
            "The Looping Forest has trapped many in infinite cycles. Cany you find a way out?",
            "A magic scroll repeats itself endlessly. Break the spell of repetition"
        ],
        "recursion":[
            "You fall into the Cave of Recursion, where every exit leads back in. Escape it!",
            "Whispers echo endlessly in the Tower of Recursion. Solve its mystery."
        ],
        "sorting":[
            "The King's archives are in chaos. Sort the scrolls in the right order!",
            "A puzzle of order has appeared. Arrange the gems by their true rank."
        ]
    }
    intro=random.choice(intro)
    scenarios=random.choice(scenarios.get(challenge_tye,["A mysterious bug has appeared. Fix it!"]))
    return f"\n{intro}\n\n{scenarios}\n"