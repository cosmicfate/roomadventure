#######################################################################
# Group: Table 3
# Students: Griffin, Dylan, Cameron Storer, Joseph Henson
# Prompt: Create a text based game and add improvements to it.
#######################################################################


# This class represents a room in the House/Game
class Room:
	def __init__(self, name):
		# Every room will have a name, exits, exit locations, items, item descriptions, and grabbables
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions = []
		self.grabbables = []
	
	# accessors and mutators
	
	# name
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
	
	# exits
	@property
	def exits(self):
		return self._exits
	@exits.setter
	def exits(self, value):
		self._exits = value
	
	# exit locations
	@property
	def exitLocations(self):
		return self._exitLocations
	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value
	
	# items
	@property
	def items(self):
		return self._items
	@items.setter
	def items(self, value):
		self._items = value
	
	# item descriptions
	@property
	def itemDescriptions(self):
		return self._itemDescriptions
	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value
	
	# grabbables
	@property
	def grabbables(self):
		return self._grabbables
	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value
	
	# A function to add directions and room objects to the exits and exitLocations arrays
	def addExit(self, exit, room):
		self.exits.append(exit)
		self.exitLocations.append(room)
	
	# A function to add items and their descriptions to the items and itemDescriptions arrays
	def addItem(self, item, desc):
		self.items.append(item)
		self.itemDescriptions.append(desc)
	
	# A function to add items to a room's grabbables i.e. things that can be removed from the room
	def addGrabbable(self, item):
		self.grabbables.append(item)
	
	# A function to remove an item from a room's grabbables
	def delGrabbable(self, item):
		self.grabbables.remove(item)
	
	# A function to affect the way a room object is printed
	def __str__(self):
		# start the string with the room's name
		s = f"You are in {self.name}. \n"
		
		# what things I can see
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"
		
		# what are the exits from the room
		s += "Exits: "
		for exit in self.exits:
			s += exit + " "
		s += "\n"
		# then return the string
		return s

###################################################################################

# HELPER FUNCTIONS
def createRooms():
	global currentRoom
	
	### create 4 rooms
	r1 = Room("Room 1")
	r2 = Room("Room 2")
	r3 = Room("Room 3")
	r4 = Room("Room 4")
	
	# add exits to the room 1
	r1.addExit("east", r2)
	r1.addExit("south", r3)
	
	# add grabbables
	r1.addGrabbable("key")
	r1.addItem("desk", "it is wooden")
	r1.addItem("chair", "it is made of steel")
	
	# room 2
	r2.addExit("west", r1)
	r2.addExit("south", r4)
	r2.addItem("bed", "its twin in size")
	r2.addGrabbable("wig")
	r2.addItem("pantry", "there is bologna in it")
	
	# room 3
	r3.addExit("north", r1)
	r3.addExit("east", r4)
	r3.addItem("stove", "there are some pancakes on it")
	r3.addGrabbable("pancake")
	r3.addItem("pantry", "there is bologna in it")
	
	# room 4
	r4.addExit("north", r2)
	r4.addExit("west", r3)
	r4.addExit("south", None)
	r4.addItem("bath", "its full of milk")
	r4.addGrabbable("milk")

	
	currentRoom = r1

def death():
	print("You are dead")

################ MAIN ######################################################

inventory = []
createRooms()

while (True):
	status = f"{currentRoom}\nYou are carrying: {inventory}"
	
	if (currentRoom == None):
		death()
		break
	
	print("=" * 40)
	print(status)
	
	# prompt usser for what they want to do
	action = input("What to do? ")
	action = action.lower().strip()
	
	if (action in ["quit", "bye", "exit", "leave"]):
		break
	
	response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."
	
	# parsing whatever they typed
	words = action.split()
	
	if (len(words) == 2):
		verb = words[0]
		noun = words[1]
		
		# what should happen if they type go
		if (verb == "go"):
			response = "invalid exit"
			
			# check all the exits
			for i in range(len(currentRoom.exits)):
				# to see if the noun is in the list of exits
				if (noun == currentRoom.exits[i]):
					# if so, change the room to the associated exit location
					currentRoom = currentRoom.exitLocations[i]
					response = "Room changed"
					break
		
		# what should happen if they type look
		if (verb == "look"):
			response = "I don't see that item"
			
			# check all the items
			for i in range(len(currentRoom.items)):
				# if I find the item the player is looking for
				if (noun == currentRoom.items[i]):
					#change the response to the associated descriptions
					response = currentRoom.itemDescriptions[i]
					break
		
		# what should happen if they type take
		if (verb == "take"):
			response = "I don't see that item"
			# check all the grabbables
			for grabbables in currentRoom.grabbables:
				# if room has what you want to grab
				if (noun == grabbables):
					
					# add item to your inventory, remove the item from the room, change your response
					inventory.append(grabbables)
					currentRoom.delGrabbable(grabbables)
					response = "Item grabbed"
					break
	
	print(f"\n{response}")
