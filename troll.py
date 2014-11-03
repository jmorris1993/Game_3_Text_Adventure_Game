import random
from npc import *
from player import *

class Troll (NPC):

    def __init__ (self,name,loc,restlessness,hunger, desc):
        NPC.__init__(self,name,loc,restlessness,10, desc)
        self._hunger = hunger
        Player.clock.register(self.eat_people,2,Player.clock.time)

    def eat_people (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._hunger) == 0:
            people = self.people_around()
            if people:
                victim = random.choice(people)
                self.location().report(self.name() + ' takes a bite out of ' + victim.name())
                victim.suffer(random.randint(1,3))
            else:
                self.location().report(self.name() + "'s belly rumbles")
    
    def is_troll(self):
        return True

    def die(self):
        Player.clock.unregister(self.eat_people,2,Player.clock.time)
        NPC.die(self)