#object oriented programming
class FortniteBot:  #class

    def __init__(self, bot_name):#constructor -- Runs once when created

        self.name = bot_name #attribute
        self.health = 100 #attribute

    def take_damage(self, amount): #method
        self.health -= amount

    