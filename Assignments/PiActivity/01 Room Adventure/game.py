from tkinter import (
    # Widgets
    Frame, Label, Text, PhotoImage, Entry,

    # Constants
    X, Y, BOTH,
    BOTTOM, RIGHT, LEFT,
    DISABLED, NORMAL, END,


    #Additional Stuff for Typehints
    Tk
)

from room import Room
import os

class Game(Frame):

    #Some constants for the game
    EXIT_ACTIONS = ["exit", "quit", "q", "bye"]

    #Some statuses
    STATUS_DEFAULT = "I don't understand. Try verb noun. Valid verbs are go, look, take, use(noun does not matter, uses item equiped)"
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid exit."
    STATUS_ROOM_CHANGE = "Room Changed"
    STATUS_GRABBED = "Item Grabbed"
    STATUS_BAD_GRABBABLE = "I can't grab that"
    STATUS_BAD_ITEM = "I don't see that"

    #option: have a status class within the Game Class
    #Game Dimensions
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent:Tk):
        """
        The Game Class.

        parent: Tk - a Tk object representing the window the game runs in
        """

        self.inventory = []
        #Sets default for equipped item to None
        self.equipped_item = None
        Frame.__init__(self, parent)
        self.pack(fill=BOTH)

    def setup_game(self):
        #create rooms
        r1 = Room("Room1", os.path.join("images", "room1.gif" ))       
        r2 = Room("Room2", os.path.join("images", "room2.gif" ))        
        r3 = Room("Room3", os.path.join("images", "room3.gif" ))        
        r4 = Room("Room4", os.path.join("images", "room4.gif" ))        

        #add exits to rooms
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("north", r1)
        r3.add_exit("east", r4)

        r4.add_exit("west", r3)
        r4.add_exit("north", r2)
        r4.add_exit("south", None, "key") #locked room

        #add itmes to rooms
        r1.add_item("chair", "Its made of beans in a bag.")
        r1.add_item("tv", "Its playing Spongebob.")
        r1.add_item("note", "I can't find my key and I'm made because it leads to an awesome place...")
        
        r2.add_item("patrick", "He's playing the mayonaises. He's also in the mood for music. Perhaps play some for him?")
        r2.add_item("tv", "It's also playing spongebob")

        r3.add_item("sponge", "It's just a sponge")
        r3.add_item("bob", "It's a guy named bob")

        r4.add_item("squidward", "His clarinet is laying unguarded. You could probably take it")
        r4.add_item("Locked Door", "The south exit door is locked for some reason. Must be something amazing on th eother side.")

        #add grabbables 
        r4.add_grabbable("key")
        r2.add_grabbable("knife")
        r3.add_grabbable("sponge")
        r4.add_grabbable("clarinet")

        #set the starting room for the game
        self.current_room = r1   
    def setup_gui(self):

        #the input element
        self.player_input = Entry(self, bg = "white", fg = "black")
        self.player_input.bind("<Return>", self.process_input)
        self.player_input.pack(side = BOTTOM, fill = X)
        self.player_input.focus()

        #the image element
        img = None
        img_width = Game.WIDTH // 2
        self.image_container = Label(
            self,
            width = img_width,
            image = img
        )

        self.image_container.image = img
        self.image_container.pack(side = LEFT, fill=Y)
        self.image_container.pack_propagate(False)
        #the info area
        text_container_width = 600
        text_container = Frame(self, width=text_container_width)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)

        self.text = Text(
            text_container,
            bg ="lightgrey",
            fg="black",
            state=DISABLED
        )

        self.text.pack(fill=Y, expand=1)

        # Inventory label
        self.inventory_label = Label(self, text="Inventory", bg="lightgrey", fg="black", font=("Helvetica", 14))
        self.inventory_label.pack(side=BOTTOM, fill=X)

        # Inventory display container 
        self.inventory_frame = Frame(text_container, width=Game.WIDTH // 2, height=100, bg="lightgrey") 
        self.inventory_frame.pack(side=BOTTOM, fill=X)
        self.inventory_images = []
        self.inventory_labels = []


    #Displays images of items in inventory
    def update_inv_display(self):
        for i, item in enumerate(self.inventory):
            img = PhotoImage(file=f"images/{item.lower()}.gif")  # Assumes each item has a corresponding image file
            if item == self.equipped_item:  #check if item is equiped and highlights blue
                label = Label(self.inventory_frame, image=img, bg="blue")
                print("highlighted blue")
            else:
                label = Label(self.inventory_frame, image=img, bg="white")
            label.grid(row=0, column=i, padx=5)
            self.inventory_images.append(img)
            self.inventory_labels.append(label)
        

    def set_image(self):
        if self.current_room == None:
            img = PhotoImage(file="Images/skull.gif")

        else:
            img = PhotoImage(file=self.current_room.image)

        self.image_container.config(image=img)
        self.image_container.image = img

    def set_status(self, status:str):
        self.text.config(state=NORMAL) #make the text editable
        self.text.delete(1.0, END)

        if self.current_room == None:
            self.text.insert(END, Game.STATUS_DEAD)
        
        else:
            content = f"{self.current_room}\n"
            content += f"Your are Carrying {self.inventory}\n\n"
            content += status
            self.text.insert(END, content)
            self.text.config(state = DISABLED)
    def clear_entry(self):
        self.player_input.delete(0, END)

    def handle_go(self, destination):
        status = Game.STATUS_BAD_EXIT
        if destination in self.current_room.exits:   #exits are in dictionary
            if destination in self.current_room.locked_exits:
                status = f"The {destination} door is locked. Must need a Key"
            else:
                self.current_room = self.current_room.exits[destination]
                status = Game.STATUS_ROOM_CHANGE


        self.set_status(status)
        self.set_image()

    #New method for using items
    def handle_use(self, item: str):
        status = Game.STATUS_BAD_GRABBABLE
        if item == "key":
            #item is not used yet
            used = False
            #iterate through locked door exits
            for exit in self.current_room.locked_exits:
                #check if item is required for an exit
                if self.current_room.unlock_exit(exit, item) == True:
                    status = f"You used the {item} to unlock the {exit} door"
                    print(f"{self.current_room.locked_exits}")
                    #item has now been used
                    used = True
                    break
            if not used:
                status = f"You used the {item}, but nothing happened"

        elif item == "clarinet":
            #check if in room with patrick
            if self.current_room.name == "Room2":
                status = "Patrick loved the music and he dropped a knife out of his mayonaise. You can probably pick it up"
            else:
                status = "You played the music gracefully although no one seemed to here"

        elif item == "knife":
            #check if in room with squidward
            if self.current_room.name == "Room4":
                status = "Squidward screamed SPongebobbb!! as he fell to the ground in death. Turns out you were spongebob the whole time. He droped a key. You can probably pick it up"
            else:
                status = "You might need to find someone to use that on lol"
        elif item == "sponge":
            status = "the sponge looked at you with deep concering eyes"
        else:
            status = "You must equip an item before using it"
        self.set_status(status)

    
    #Handles when an item is equipped 
    def handle_equip(self, item_name):
        if item_name in self.inventory:
            self.equipped_item = item_name
            #highlight equiped item
            self.update_inv_display()
            self.set_status(f"Sucessfully Equipped {self.equipped_item}")
        else:
            self.set_status(f"You don't have {item_name} in your inventory.")
          

    def handle_look(self, item):
        status = Game.STATUS_BAD_ITEM
        if item in self.current_room.items:
            status = self.current_room.items[item]

        self.set_status(status)

        pass
    def handle_take(self, grabbable):
        status = Game.STATUS_BAD_GRABBABLE
        if grabbable in self.current_room.grabbables:  #this is just a list
            self.inventory.append(grabbable)
            self.current_room.delete_grabbable(grabbable)
            #Calls update inv display to put the grabbed items image on screen
            self.update_inv_display()
            status = Game.STATUS_GRABBED
        self.set_status(status)

    def handle_default(self):
        self.set_status(Game.STATUS_DEFAULT)
        self.clear_entry

    def play(self):
        self.setup_game()
        self.setup_gui()
        self.set_image()
        self.set_status("")



    def process_input(self, event):
        action = self.player_input.get()
        action = action.lower()

        if action in Game.EXIT_ACTIONS:
            exit()

        if self.current_room == None:
            self.clear_entry()
            return
        
        words = action.split()  # splits at spaces and creates a list

        if len(words) != 2:
            self.handle_default()
            return
        
        verb = words[0]
        noun = words[1]

        match verb:
            case "go": self.handle_go(noun)
            case "look": self.handle_look(noun)
            case "take": self.handle_take(noun)
            #New verb for using an item that is equiped
            case "use": self.handle_use(self.equipped_item)
            #New verb for when you want to equip an item
            case "equip": self.handle_equip(noun)

        self.clear_entry()
        

    