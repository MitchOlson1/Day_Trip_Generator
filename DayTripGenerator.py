destinations = ['mall','park','woods','beach']
restaurants = ['Arbys','Subway','McDonalds','Chipotle']
transportation = ['car','bus','bike',]
entertainment = ['concert','movie','bar']

import random
destination = random.choice(destinations)
print(destination)

import random
restaurant = random.choice(restaurants)
print(restaurant)

import random 
transport = random.choice(transportation)
print(transport)

import random
entertain = random.choice(entertainment)
print(entertain)


user_input = input('Enter re-select')
for destination in destinations:
    if user_input == 're-select':
        import random
        destination = random.choice(destinations,1)
        print(destination)
    elif user_input != 're-select':
        break
         






    
     

