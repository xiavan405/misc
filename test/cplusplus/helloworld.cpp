// testing c++ syntax

#include <iostream> //this line tells the program to make operations from the iostream head//header available

int main() { /*this line initiates the "main" part of the program that executes when the program is run. it also defines the "success state" as "int" meaning the program expects an integer to be returned before it can end. */
	std::cout << "Hello world!\n"; //std::cout is analagous to std.cout() python syntax//cout is essentially the print function of c++. << "pipes" the string into cout. 
	return 0; //we return an int so the program will know to end here.
}
