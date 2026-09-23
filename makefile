restaurant: main.o restaurant.o menuItem.o
	g++ -o restaurant main.o restaurant.o menuItem.o
main.o: main.cpp restaurant.h
	g++ -c main.cpp
restaurant.o: restaurant.cpp restaurant.h menuItem.h
	g++ -c restaurant.cpp
menuItem.o: menuItem.cpp menuItem.h
	g++ -c menuItem.cpp
clean:
	rm *.o restaurant