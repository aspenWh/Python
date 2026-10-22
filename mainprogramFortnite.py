from FortniteBot import FortniteBot #This is when you are programming for a game when you need different outcomefor a game 

bot1 = FortniteBot("R2-D2") #creating an instance and storing it in an object called bot1
bot2 = FortniteBot("Chat")
bot3 = FortniteBot("Destroyer")

bot1.take_damage(5) #calling the take damage method on bot1 and passing in 5 as the amount of damage to take
bot2.take_damage(20)

print(bot1.name)
print(bot1.health)

print(bot2.health)
print(bot3.health)

FortniteBot.max_health = 200

print("Before")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)


print("After")
print(bot1.max_health)
print(bot2.max_health)
print(bot3.max_health)
