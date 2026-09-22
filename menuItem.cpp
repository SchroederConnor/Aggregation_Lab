#include "menuItem.h"

MenuItem ::MenuItem(){
    name = "N/A";
    price = 0.0;
}
MenuItem ::MenuItem  (string n,double p){
    name = n;
    price = p;
}
MenuItem::MenuItem  (const MenuItem& rhs){
    name = rhs.name;
    price = rhs.price;
}   

void MenuItem::setName(string n){
    name = n;
}
void MenuItem::setPrice(double p){
    price = p;
}

string MenuItem::getName(){
    return name;
}
double MenuItem::getPrice(){
    return price;
}

void MenuItem::displayMenuItemDataa(){
    cout  << name << ": " << price << endl;
    
}