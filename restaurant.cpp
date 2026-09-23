#include "restaurant.h"

//constructors
Restaurant::Restaurant()
{
    name = "N/A";
    numItem = 0;
}
Restaurant::Restaurant(string n, MenuItem* m, int num)
{
    name = n;
    for(int i = 0; i < num; i++)
    {
        items[i] = m[i];
    }
}
Restaurant::Restaurant(const Restaurant& rhs)
{
    name = rhs.name;
    numItem = rhs.numItem;
    for(int i; i < numItem; i++)
    {
        items[i] = rhs.items[i];
    }
}

//setters
void Restaurant::setName(string n){
    name = n;
}

//getters
string Restaurant::getName(){
    return name;
}
int Restaurant::getNumItems(){
    return numItem;
}
MenuItem* Restaurant::getItems(){
    return items;
}

//adders
void Restaurant::addItem(MenuItem m)
{
    if(numItem < 3)
    {
        items[numItem] = m;
        numItem++;
    }
    else
    {
        cout << "Can not add new menu item. Limit exceeded!" << endl;
    }
}

void Restaurant::displayRestaurantData()
{
    cout << "Welcome to " << name << endl;
    cout << "===================" << endl;
    cout << "Menu" << endl;

    for(int i = 0; i < 3; i++)
    {
        items[i].displayMenuItemDataa();
    }
}
