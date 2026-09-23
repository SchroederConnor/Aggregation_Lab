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
    if(numItem < SIZE)
    {
        for(int i = 0; i < numItem; i++)
        {
            if(items[i].getName() == "N/A")
            {
                items[i] = m;
                numItem++;
                break;
            }
            break;
        }
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

    for(int i = 0; i < numItem; i++)
    {
        items[i].displayMenuItemDataa();
    }
}
