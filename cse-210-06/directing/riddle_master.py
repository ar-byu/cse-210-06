import random

class RiddleMaster:
    def __init__(self):
        #Initializes the riddles, hints, and answer options
        self._riddle_list = [
        ["""The room is dark and humid. The floor is covered in a carpet of moss, 
        and small mushrooms grow at the edges of the room. Across the room is a door with a sign hanging on it. 
        The large letters painted on the sign read 
        'You cannot enter this room. What room is it?' 
        Underneath the question is a space to write something down. What will you write?""", "Look around the edges of the room.", "mushroom", "a mushroom"],
        ["""The walls of this room glitter with flecks of gold. Large statues flank the door, and two sets of armor stand 
        on either side of the door across the room. The other door has a sign hanging on it. You draw close enough to read the sign. 
        It says, 
        'I have a golden tail and a golden head, but no body. What am I?' 
        Underneath the question is a space to write something.""", "You might have one in your pocket.", "coin", "gold coin"],
        ["""The room you enter is dazzlingly bright in comparison to the rest of the tower. You pause for a moment to let your eyes adjust. 
        The walls are not made of stone like the rest of the tower's walls; instead they are made out of large windows. 
        Across the room from you is a door with a sign on it. The sign reads, 
        'I am an eye set in a blue face. My gaze feeds the world. 
        If I go blind so does the world.' 
        Under the questions is a space to write something.""", "Look outside.", "sun", "the sun"],
        ["""The room before you doesn't smell very good. Hay and straw is scattered on the floor. There are saddles hanging along one wall, 
        and suits of armor lining the other. On the opposite end of the room, there is a door with a sign. The sign reads 
        'What has six legs, but only walks on four?' 
        Under the questions is a space to write something.""", "Look at the walls.", "a person riding a horse", "a person on a horse"],
        ["""The room you enter is covered in sand. It crunches under your feet as you walk, leaving prints of your boots. 
        The only other thing in the room, besides all the sand, is a door with a sign. You draw close to the sign to read it. 
        The sign reads, 
        'The more you leave it behind, the more you take. What am I?' 
        Under the question is a space to write something.""", "Look at the floor behind you.", "footprints", "footsteps"],
        ["""The dark room is larger than it should be, and has a domed ceiling, upon which is a detailed astronomical map.
        The sun and moon are depicted at opposite sides of the room. On the other side of the room is a door with a sign.
        The sign reads, 
        'They arrive every night whether invited or not. They can be seen, but not heard or touched. 
        If one falls the rest keep moving. What am I?'
        Under the question is a space to write something.""", "Look at the ceiling.", "stars", "the stars"],
        ["""The room you enter is uncomfortably warm. Two large fireplaces sit at either side of the room, both with roaring fires within them.
        There is a door on the other side of the room, with a sign on it. The sign reads,
        'What breathes, consumes, and grows, but was and never will be alive?'""",
        "Look at the sides of the room", "fire", "a fire"],
        ["""The room you enter is fairly plain, except for the tapestries on the walls. Each tapestry has an intricate family tree embroidered on it.
        The main line of each family tree marks people sharing the same first name. There is a door on the other side of the room. It bears a sign, which reads,
        'Passed from parent to child, and shared between siblings, though it is used more by others. What am I?'""",
        "Look closely at the family trees.", "names", "a name"
        ]]

    def get_riddle(self):
        #Chooses a random riddle and its associated hint and answers
        riddle = random.choice(self._riddle_list)
        return riddle