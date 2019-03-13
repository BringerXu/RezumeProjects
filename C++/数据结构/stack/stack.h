#include<iostream>
#define STACK_CAPACITY 1000 
using std::cout;
using std::endl;
class Stack{
public:
	Stack(){
		count = -1;
	}

	void push(char c){
		if(isFull()){
			error("Stack is full");
			return;
		}
		s[++count] = c;		
	}

	char pop(){
		if(! isEmpty()){
			return s[count--];
		}else{
		error("Stack is empty->nothing to pop");
		return '\0';
		}
	}

	char top(){
		if(! isEmpty()){
			return s[count];
		}else{
			error("Stack is empty->nothing on the top");
			return '\0';
		}
	}

	bool isEmpty(){
		if(count == -1){
			return true;
		}
		return false;
	}

	bool isFull(){
		if(count >= STACK_CAPACITY-1){
			return true;
		}
		return false;
	}
	

private:
	int count;
	char s[STACK_CAPACITY];
	void error(const char* msg){
		cout<<"Error:"<<msg<<endl;
	}
};
