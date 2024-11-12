//Name: Reagan Jose
//Date: 11/11/2024
//Description: Room Adventure... one last time... finally... make it stop...

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
    private static ArrayList<String> inventory = new ArrayList<String>();
    private static String status;

    //constants - final makes it a constant
    final private static String DEFAULT_STATUS = "Sottry, I don't undestand. Try [verb] [noun]";

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
        String[] exitDirections = currentRoom.getExitDirections();
        Room[] exitDestinations = currentRoom.getExitDestinations();

        status = "I don't see that room";
        for(int i = 0; i < exitDirections.length; i++){
            if(noun.equals(exitDirections[i])){
                if(noun.equals(exitDirections[i])){
                    currentRoom = exitDestinations[i];
                    status = "Changed Room";
                    break;   
                }
            }
        }
    }

    private static void handleLook(String noun){
        String [] items = currentRoom.getItems();
        String [] itemDescriptions = currentRoom.getItemDescriptions();

        status = "I don't see that item";
        for(int i=0; i < items.length; i++){
            if (noun.equals(items[i])){
                status = itemDescriptions[i];
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
        // instantiate rooms
        Room room1 = new Room("Room 1");
        Room room2 = new Room("Room 2");
        Room room3 = new Room("Room 3");
        Room room4 = new Room("Room 4");


        //setup Room 1
        String[] room1ExitDirections = {"east", "south"}; //initializing an array
        Room[] room1ExitDestinations = {room2, room3};


        String[] room1Items ={
            "Chair",
            "Desk"
        };

        String[] room1ItemDescriptions = {
            "It is a char.",
            "It is a desk. There is a key on it"
        };

        String[] room1Grabbables = {"key"};

        room1.setExitDirections(room1ExitDirections);
        room1.setExitDestinations(room1ExitDestinations);
        room1.setItemDescriptions(room1ItemDescriptions);
        room1.setItems(room1Items);
        room1.grabbables = room1Grabbables;

        //setup Room 2
        String[] room2ExitDirections = {"west"}; //initializing an array
        Room[] room2ExitDestinations = {room1};

        String[] room2Items ={
            "rug",
            "fireplace"
        };

        String[] room2ItemDescriptions = {
            "It's like a chair but flat. There is a satsuma on it.",
            "It's hot"
        };

        String[] room2Grabbables = {"satsuma"};

        room2.setExitDirections(room2ExitDirections);
        room2.setExitDestinations(room2ExitDestinations);
        room2.setItemDescriptions(room2ItemDescriptions);
        room2.setItems(room2Items);
        room2.grabbables = room2Grabbables;
        

        //setup Room 3
        String[] room3ExitDirections = {"north", "east"}; //initializing an array
        Room[] room3ExitDestinations = {room1, room4};

        String[] room3Items ={
            "statue",
            "bookshelf"
        };

        String[] room3ItemDescriptions = {
            "It's the lady of the mist. A full sized replica.",
            "There is one book on it."
        };

        String[] room3Grabbables = {"book"};

        room3.setExitDirections(room3ExitDirections);
        room3.setExitDestinations(room3ExitDestinations);
        room3.setItemDescriptions(room3ItemDescriptions);
        room3.setItems(room3Items);
        room3.grabbables = room3Grabbables;


        //setup Room 4
        String[] room4ExitDirections = {"west"}; //initializing an array
        Room[] room4ExitDestinations = {room3};

        String[] room4Items ={
            "statue",
            "bookshelf"
        };

        String[] room4ItemDescriptions = {
            "It's the lady of the mist. A full sized replica.",
            "There is one book on it."
        };

        String[] room4Grabbables = {"book"};

        room4.setExitDirections(room4ExitDirections);
        room4.setExitDestinations(room4ExitDestinations);
        room4.setItemDescriptions(room4ItemDescriptions);
        room4.setItems(room4Items);
        room4.grabbables = room4Grabbables;

        currentRoom = room1;
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

        //add exits to the output
        result += "\nExits: ";
        for (String direction : exitDirections){
            result += String.format("%s", direction);   
        }


        return result;
    }
 

}