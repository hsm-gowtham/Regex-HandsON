import re

from numpy import mat

some_random_sentence = '''
I'm beginnin' to feel like a Rap God, Rap God
All my people from the front to the back nod, back nod
Now, who thinks their arms are long enough to slap box, slap box?
They said I rap like a robot, so call me Rap-bot
But for me to rap like a computer, it must be in my genes
I got a laptop in my back pocket
My pen'll go off when I half-cock it
Got a fat knot from that rap profit
Made a livin' and a killin' off it
Ever since Bill Clinton was still in office
With Monica Lewinsky feelin' on his nutsack
I'm an MC still as honest
But as rude and as indecent as all hell
Syllables, skill-a-holic (kill 'em all with)
'''

pattern = re.compile(r"I'm")

matches = pattern.finditer(some_random_sentence)

for match in matches:
    print(match)

# span is useful for indexing
print(some_random_sentence[30:37])