#include<iostream>
#include "stack.h"
using std::string;
using std::cin;
using std::cout;
using std::endl;
int main(){
	string str;
	Stack testStack;
	while(getline(cin,str))
	{
		for(int i = 0;i < str.length();i++)
		{
			testStack.push(str[i]);
		}
	
		while(!testStack.isEmpty())
		{
			cout<<testStack.pop()<<endl;
		}
	}
	return 0;
}
