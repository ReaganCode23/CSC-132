
class Room:

    def __init__(self, name: str, image_filepath: str):
        """
        A Room in Room Adventure game.

        name: str- a name for the room
        image_filepath: str - the relative filepath to the image
        :name: 
        """

        self.name = name
        self.image = image_filepath
        self.exits: dict[str, 'Room'] = {}
        #locked exits
        self.locked_exits: dict[str, str] = {}
        self.items: dict[str, str] = {}
        self.grabbables = []


    def add_exit(self, location: str, room: 'Room | None', locked_with: str = None) -> None:  #There is now a locked with parameter
        """
        Adds an exit to the room.
        location: str - a direction such as "north", "south", "east", "west", "up", "down", ect..
        room: Room | None - a room that the `location` leads to.
        """

        self.exits[location] = room
        #configure locked exit with required item to unlock
        if locked_with:
            self.locked_exits[location] = locked_with
        

    def add_item(self, label:str, desc: str,) -> None:
        self.items[label] = desc
        
    def add_grabbable(self, item: str) -> None:
        self.grabbables.append(item)

    def delete_grabbable(self, item: str) -> None:
        self.grabbables.remove(item)
    
    #New Method for unlocking an exit
    def unlock_exit(self, location: str, item: str) -> bool:
        #checks if room is locked and if item matches
        if self.locked_exits[location] == item: 
            #removes exit from locked_exits
            print(f"{self.locked_exits[location]} = {item}")
            del self.locked_exits[location]
            return True
        else:
            return False

    def __str__(self) -> None:
        result = f"You are in {self.name}\n"
        result += f"You see: "
        for item in self.items.keys():
            result += item + " "
        result += "\n"

        result += "Exits: "
        for exit in self.exits.keys():
            result += exit + " "
        
        result += "\n"
        return result