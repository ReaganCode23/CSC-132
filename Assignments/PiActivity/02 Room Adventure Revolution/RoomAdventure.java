public class RoomAdventure{
    // game class
    /*
      block
    */
    //static means it belongs to the class
    private static Room currentRoom;
    private static String[] inventory = {null, null, null, null, null};
    private static String[] status;

    //constants - final makes it a constant
    final private static String DEFAULT_STATUS = "Sottry, I don't undestand. Try [verb] [noun]";

    public static void main(String[] args){
        setupGame();

    }

    private static void setupGame(){
        // instantiate rooms
        Room room1 = new Room("Room 1");
        Room room2 = new Room("Room2");
        Room room3 = new Room("Room3");

        //setup Room 1
        String[] room1ExitDirections = {"east", "south"}; //initializing an array
        Room[] room1ExitDestinations = {room2, room3};

        String[] room1ItemDescriptions = {
            "It is a char.",
            "It is a desk. There is a key on it"
        };

        String[] room1Grabbables = {"key"};

        room1.setExitDirections(room1ExitDirections);
        room1.setExitDestinations(room1ExitDestinations);
        room1.setItemDescriptions(room1ItemDescriptions);
        room1.grabbables = room1Grabbables;
    }



}

class Room{

    //instance variables
    private String roomName;

    // a private instance variable that is an array of Strings
    private String[] exitDirections; //west, east, north, south, up, down
    private Room[] exitDestinations; //actual rooms tied to the directions west, east, ect.

    private String[] items; //item names like "key"
    private String[] itemDescriptions; //ex: "a golden key. maybe we can take it"

    public String[] grabbables;

    // constructor
    public Room(String name){
        roomName = name;
        
    }

    //can have more than one constructor as long as the signature of the function
    //is different than all of the other contructors
    //public Room(int number){
        //roomNumber = number}

    //methods
    //setter ex:
    public void setExitDirections(String[] dirs){
        exitDirections = dirs;

    }

    // getter ex;
    public String[] getExitDirections(){
        return exitDirections;
    }

    public void setExitDestinations(Room[] exitDestinations){
        this.exitDestinations = exitDestinations;
    }

    public Room[] getExitDestinations(){
        return this.exitDestinations;

    }

    public void setItems(String[] items){
        this.items = items;

    }

    public String[] getItems(){
        return this.items;
    }

    public void setItemDescriptions(String[] itemDescriptions){
        this.itemDescriptions = itemDescriptions;
    }

    public String[] getItemDescriptions(){
        return this.itemDescriptions;
    }

    public String toString(){
        String result = "\n";
        result += "Locations: " + roomName; //concatenation and the += operator are the same

        result += "\nYou See: ";
        // for loop
        for (int i = 0; i < items.length; i++){
            result += items[i] + " "; //accessing items in a n array
        }

        //for each loops
        for (String direction : exitDirections){
            result += String.format("%s", direction);

            
        }


        return result;
    }





    // not doing getter/setter for grabbles since it is public already.

}