from person import *
from clock import *

import sys


class Player (Person):

    # static field representing the player
    me = None
    # static field recording god_mode
    god_mode = False
    # static field representing the clock
    clock = Clock(0)

    def __init__ (self,name,loc, desc, _strength):
        Person.__init__(self,name,loc, desc)
        Player.me = self
        self._max_health = 5
        self._health = self._max_health
        self._strength = _strength

    # Grab any kind of thing from player's location, 
    # given its name.  The thing may be in the possession of
    # the place, or in the possession of a person at the place.
   
    def thing_named (self,name):
        for x in self.location().contents():
            if x.name() == name:
                return x
        for x in self.peek_around():
            if x.name() == name:
                return x
        for x in self.contents():
            if x.name() == name:
                return x
        return None

    def look_around (self):
        def names (lst):
            return ', '.join([x.name() for x in lst])

        loc = self.location()
        exits = loc.exits()
        people = self.people_around()
        all_stuff = self.stuff_around()

        print '------------------------------------------------------------'
        print 'You are in', loc.name()
        print loc.describe()

        if all_stuff:
            print 'You see:', names(all_stuff)
        else: 
            print 'The room is empty'

        if people:
            print 'You see:', names(people)
        else:
            print 'You see no one around'

        if exits:
            print 'Exits:', ', '.join([x for x in exits])
        else:
            print 'There are no exits'
        
        print 
        print "Events:"
        print
    
    def is_player(self):
        return True
    
    def look (self, obj):
        def names (lst):
            return ', '.join([x.name() for x in lst])
        print obj.name()
        print obj.describe()
        if obj.is_person():
            if obj.contents() != []:
                print names(obj.contents())
        if obj.is_player():
            print "Strength: " + str(self._strength)
            print "Health: " + str(self._health) + "/" + str(self._max_health)
            
    def attack(self, acted):
        if acted.is_person():
            acted._health -= self._strength
            if acted._health <=0:
                acted.die()
                print acted._name + " has been slain..."
            
    def die (self):
        self.say('I am slain!')
        Person.die(self)
        print 'This game for you is now over...'
        sys.exit(0)
