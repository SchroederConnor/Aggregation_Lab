#include "restaurant.h"


int main(){
    
    // Create a MenuItem object named burger using the parameterized constructor
    // Pass "Burger" as the name and 8.5 as the price
    MenuItem burger = MenuItem("Burger", 8.5);

    // Create a MenuItem object named pizza using the parameterized constructor
    // Pass "Pizza" as the name and 18.55 as the price
    MenuItem pizza = MenuItem("Pizza", 18.5);

    // Create a MenuItem object named sandwich using the parameterized constructor
    // Pass "Sandwich" as the name and 10.5 as the price
    MenuItem sandwich = MenuItem("Sandwich", 10.5);

    // Create an array of MenuItem objects named "items" with size 3
    // Assign burger to index 0, pizza to index 1, and sandwich to index 2
    MenuItem items[3] = {burger, pizza, sandwich};

    // Create a Restaurant object named restaurant using the parameterized constructor
    // Pass "Hello World" as the name, 3 as the number of item and items as the MenuItem array
    

    //call the displayRestaurantData method for the restaurant object
    

    // Create a MenuItem object named salad using the parameterized constructor
    // Pass "Salad" as the name and 10.75 as the price
    

    //call the addItem method for the restaurant object to add item salad
    
    

    
    //To pass the test your code should have exact output as the Output.txt so do not modify it.
    //Check the item name spelling/case and the newlines are exactly same in your output
    
    return 0;
}