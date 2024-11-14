//Name: Reagan Jose
//Date: 11/11/2024
//Description: Room Adventure... one last time... finally... make it stop...
//New Features:
//1. Added Extra Rooms and Grabbables
//2. Improved the inventory by making it into an ArrayList
//3. Changed Exits and Items from lists to their own Classes

import java.util.Scanner;
//Array List package
import java.util.ArrayList;

public class RoomAdventure{
    // game class
    /*
      block
    */
    //static means it belongs to the class
    private static Room currentRoom;
    private static ArrayList<String> inventory = new ArrayList<String>();   //Inventory is now an ArrayList for expandability.
    private static String status;

    //constants - final makes it a constant
    final private static String DEFAULT_STATUS = "Sorry, I don't undestand. Try [verb] [noun]";

    public static void main(String[] args){
        setupGame();
    
        //while loop (our main loop for this)
        while (true){
            System.out.println(currentRoom.toString());
            System.out.print("Inventory: ");
            
            //print out everything in the inventory
            for (int i = 0; i < inventory.size(); i++){     //.size() gives size of the ArrayList
                System.out.print(inventory.get(i) + " ");   //getting index value from ArrayList
            }
            System.out.println("\nWhat would you like to do? ");

            //taking input
            Scanner s = new Scanner(System.in);
            String input = s.nextLine();

            //processing our input
            String[] words = input.split(" ");

            if (words.length != 2){
                status = DEFAULT_STATUS;
                continue;
            }
            String verb = words[0];
            String noun = words[1];

            switch(verb){
                case "go":
                    handleGo(noun);
                    break;
                case "look":
                    handleLook(noun);
                    break;
                case "take":
                    handleTake(noun);
                    break;
                default:
                    status = DEFAULT_STATUS;
            }

            System.out.println(status);


        }

    }
    private static void handleGo(String noun){
        ArrayList<Exit> exits = currentRoom.getExits();

        status = "I don't see that room";
        //Array List For loop
        for(Exit exit : exits){
            if(noun.equals(exit.getDirection())){
                currentRoom = exit.getDestination();
                    status = "Changed Room";
                    break;  
            }
        }
    }

    private static void handleLook(String noun){
        ArrayList<Item> items = currentRoom.getItems();

        status = "I don't see that item";
        //Array List for loop
        for(Item item : items){
            if (noun.equals(item.getName())){
                status = item.getDescription();
                break;
            }
        }

    }

    private static void handleTake(String noun){
        status = "I can't grab that";
        for(int i = 0; i < currentRoom.grabbables.length; i++){
            if (noun.equals(currentRoom.grabbables[i])){
                inventory.add(noun);    //adds noun to the ArrayList which shortend up the original code a lot.
                status = String.format("Added %s to inventory", noun);
                }
            }
        }

    private static void setupGame(){
        //Items and Exits are now ArrayLists of Item objects and Exit objects.

        // Instantiate rooms
        Room room1 = new Room("Earth");
        Room room2 = new Room("Endurance Spacecraft");
        Room room3 = new Room("Miller's Planet");
        Room room4 = new Room("Mann's Planet");
        Room room5 = new Room("Tesseract");
    
        // Setup Earth
        String[] room1Grabbables = {"NASA_coordinates"};
    
        room1.addExit("north", room2);
        room1.addItem("farmhouse", "Cooper's family farmhouse, surrounded by dust storms.");
        room1.addItem("cornfield", "The vast cornfields where Cooper drives his truck.");
        room1.addItem("anomaly", "NASA_coordinates. You can probably pick them up.");
        room1.grabbables = room1Grabbables;
    
        // Setup Endurance Spacecraft
        String[] room2Grabbables = {"space_suit"};
    
        room2.addExit("south", room1);
        room2.addExit("west", room3);
        room2.addItem("control_room", "The control center of the Endurance, with various monitors and controls.");
        room2.addItem("cryo_pods", "Pods used for long-term hibernation during space travel.");
        room2.addItem("space_suit", "A space suit. You can probably pick it up.");
        room2.grabbables = room2Grabbables;
    
        // Setup Miller's Planet
        String[] room3Grabbables = {"wreckage"};
    
        room3.addExit("east", room2);
        room3.addExit("north", room4);
        room3.addItem("massive_wave", "A towering wave, the most prominent feature of Miller's Planet.");
        room3.addItem("ranger", "The small landing craft used for exploring the planet.");
        room3.addItem("wreckage", "wreckage left over from the original team. I think they died. You can probably pick it up.");
        room3.grabbables = room3Grabbables;
    
        // Setup Mann's Planet
        room4.addExit("south", room3);
        room4.addExit("north", room5);
        room4.addItem("frozen_landscape", "A barren, icy landscape stretching as far as the eye can see.");
        room4.addItem("hibernation_pod", "Dr. Mann's hibernation pod, covered in frost.");
    
        // Setup Tesseract
        String[] room5Grabbables = {"quantum_data"};
    
        room5.addExit("south", room4);
        room5.addItem("bookshelf", "A strange, infinite array of bookshelves stretching in all directions.");
        room5.addItem("time_ripple", "A visual representation of the bending of space-time.");
        room5.addItem("TARS", "You radioed tars for the quantum_data. You can probably pick it up.");

        room5.grabbables = room5Grabbables;
    
        currentRoom = room1;
        
        
    }




}

class Room{

    //instance variables
    private String roomName;

    // a private instance variable that is an array of Strings
    //private String[] exitDirections; //west, east, north, south, up, down
    //private Room[] exitDestinations; //actual rooms tied to the directions west, east, ect.

    //Array list of exits
    private ArrayList<Exit> exits = new ArrayList<Exit>();

    //Array Items
    private ArrayList<Item> items = new ArrayList<Item>();

    //List Grabbables
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

    //Exit Setter
    public void addExit(String dir, Room destination){
        exits.add(new Exit(dir, destination));
    }

    //Exit Getter
    public ArrayList<Exit> getExits(){
        return exits;
    }

    //Item Setter
    public void addItem(String name, String description){
        items.add(new Item(name, description));
    }

    //Item Getter
    public ArrayList<Item> getItems(){
        return items;
    }

    public String toString(){
        String result = "\n";
        result += "Locations: " + roomName; //concatenation and the += operator are the same

        result += "\nYou See: ";
        // for loop
        for (Item item : items){
            result += item.getName() + " "; //accessing items in a n array
        }

        //add exits to the output
        result += "\nExits: ";
        for (Exit exit : exits){
            result += String.format("%s ", exit.getDirection());   
        }


        return result;
    }
 

}

//Item class for replacing parrallel list
class Item{
    public String name;
    private String description;
    
    //contructor for item
    public Item(String name, String description){
        this.name = name;
        this.description = description;
    }

    //name getter
    public String getName(){
        return name;
    }

    //description getter
    public String getDescription(){
        return description;
    }
}

//Exit class for replacing parrallel list
class Exit{
    public String direction;
    private Room destination;
    
    //contructor for item
    public Exit(String direction, Room destination){
        this.direction = direction;
        this.destination = destination;
    }

    //direction getter
    public String getDirection(){
        return direction;
    }

    //location getter
    public Room getDestination(){
        return destination;
    }
}