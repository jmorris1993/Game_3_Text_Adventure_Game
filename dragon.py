from player import *
from npc import *
from weaponandarmor import *


class Dragon(NPC):
    def __init__ (self,name,loc,restlessness,rage, desc):
        NPC.__init__(self,name,loc,restlessness,1, desc)
        self._max_health = 50
        self._health = self._max_health
        self._rage = rage
        Player.clock.register(self.burn_everything,1,Player.clock.time)
        

    def burn_everything (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._rage) == 0:
            people = self.people_around()
            for people in self.people_around():
                self.location().report(self.name() + ' burns ' + people.name())
                people.suffer(10)
            else:
                self.location().report(self.name() + " is ready to burn things.")
    
    def move_somewhere (self):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)
    
    def is_dragon(self):
        return True

    def die (self):
        self.say('How dare you slay me!! AAAAAHHHHHHHHHHHHHH!!!!!!')
        Player.clock.unregister(self.burn_everything,1,Player.clock.time)
        Player.clock.unregister(self.move_somewhere,1,Player.clock.time)
        NPC.die(self)
        print "You have slain the dragon. You gain the dragon sword and the dragon shield."
        Player.me.add_thing(WeaponAndArmor("Dragon Sword",Player.me.location(),"The most powerful sword in the game. Burns everyone. +100 Str",100,0))
        Player.me.add_thing(WeaponAndArmor("Dragon Shield", Player.me.location(), "The most powerful shield in the game. You are invincible. +200 Def",0,200 ))
