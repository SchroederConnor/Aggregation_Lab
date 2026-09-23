#ifndef RESTAURANT_H
#define RESTAURANT_H
#define SIZE 3
#include "menuItem.h"

class Restaurant
{
    string name;
    MenuItem items[SIZE];
    int numItem;

    public:
        Restaurant();
        Restaurant(string, MenuItem*, int);
        Restaurant(const Restaurant&);

        void setName(string);

        string getName();
        int getNumItems();
        MenuItem* getItems();
        
        void addItem(MenuItem);

        void displayRestaurantData();
};

#endif