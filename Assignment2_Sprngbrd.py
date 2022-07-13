rarebirds = {
    'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True},
'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False},
  'Four-metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False},
    'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True},
   'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False},
}

birdlocation =['In the canopy directly above our heads','Between my 6 and 9 o’clock above','Between my 9 and 12 o’clock above','Between my 12 and 3 o’clock above','Between my 3 and 6 o’clock above','In a nest on the ground','Right behind you']

codes = {
    'HHH': 'In the canopy directly above our heads',
    'HHT': 'Between my 6 and 9 o’clock above',
    'HTT': 'Between my 9 and 12 o’clock above',
    'TTT': 'Between my 12 and 3 o’clock above',
    'TTH': 'Between my 3 and 6 o’clock above',
    'THH': 'In a nest on the ground',
    'HTH': 'Right behind you'
    }

actions = ['Back Away','Cover our Heads','Take a Photograph']

#print(rarebirds["Giant Eagle"]["Aggressive"])

#string specifying the names of all the birds
print(rarebirds.keys())

#if rarebirds["Giant Eagle"]["Aggressive"] = 'True':
 #   print(actions[1])
for x in rarebirds:
    bird_name = x
    if (rarebirds[x]['Aggressive']) == True:
        print(bird_name + " is Aggressive, so " + actions[1])
    if (rarebirds[x]['Endangered']) == True:
        print(bird_name + " is endangered, so " + actions[0])
#Task 7
for code,values in codes.items():
    print(code, ":", values)
#Task 8
for x in rarebirds:
    rarebirds[x]['seen'] = 'False'
    print(rarebirds[x])
#Task 9
encounter = True
#task 10
while encounter:
    sighting = input("What do you see? ").lower()
#Task11
    rarebirdsList = list(rarebirds.keys())
    print(rarebirdsList)
#task 12
    #sighting_cap= sighting.title()
    #print("bird is: ", sighting_cap)
    print("bird is: ", sighting)
    if sighting not in list(map(lambda x: x.lower(),rarebirdsList)):
        print("that’s not one of the birds we’re looking for")
        continue
    else:
        print("this is one of the birds we’re looking for!")
#task 13
    code = input("Where do you see it? Input the correct code.")
#task 14
    location =codes[code]
    print("Location is: ",location)
#task 15
    sighting_cap= sighting.title()
    print("bird is: ", sighting_cap)
    print("So you've seen a", sighting_cap, location, ". My goodness.")
#task 16
    if rarebirds[sighting_cap]['Aggressive'] == True:
        if rarebirds[sighting_cap]['Endangered'] == True:
            print(sighting_cap + " is Aggressive and Endangered")
            print(actions[0], " and ", actions[1])
            print(actions[2] + " of " + sighting_cap + " at its " + location)
            encounter=False
        else:
            print(sighting_cap + " is Aggressive")
            print(actions[0], " and ", actions[1])
            print(actions[2] + " of " + sighting_cap + " at its " + location)
            encounter=False
    elif rarebirds[sighting_cap]['Endangered'] == True:
        print(sighting_cap + " is Endangered and we need to " + actions[0])
        print(actions[2] + " of " + sighting_cap + " at its " + location)
        encounter = False
    else:
        print(actions[2] + " of this ultra rare " + sighting_cap + " at " + location)
        encounter = False
