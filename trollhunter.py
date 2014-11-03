import random
from npc import *
from player import *

class TrollHunter(NPC):
    def __init__ (self,name,loc,restlessness,rage,desc):
        NPC.__init__(self,name,loc,restlessness,10, desc)
        self._rage = rage
        Player.clock.register(self.kill_trolls,1,Player.clock.time)
        
    def rage(self):
        return self._rage
        
    def set_rage(self,rage):
        self._rage = rage
        
    def is_trollhunter():
        return True
        
    def kill_trolls (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._rage) == 0:
            troll = self.trolls_around()
            if troll:
                prey = random.choice(troll)
                self.location().report(self.name() + ' hunts down ' + prey.name())
                prey.suffer(random.randint(1,5))
            else:
                self.location().report(self.name() + " is full of rage!!!")

    def die(self): 
        Player.clock.unregister(self.kill_trolls,1,Player.clock.time)
        NPC.die(self)
