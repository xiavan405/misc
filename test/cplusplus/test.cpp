/*testing user input and more complicated syntax in c++*/

#include <iostream>

using namespace std;

int main()
{
		int thisnumber;

		cout<<"Please enter a number: ";
		cin>> thisnumber;
		cin.ignore();
		cout<<"You entered: "<< thisnumber <<"\n";
		return 0;
}
