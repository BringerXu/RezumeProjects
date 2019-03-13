#include "String.h"
//ListNode
String::ListNode * String::ListNode::stringToList(const char *s)
{
	return !*s ? 0 : new ListNode(*s, stringToList(s+1));
}

String::ListNode * String::ListNode::copy(ListNode * L)
{
	return L == NULL ? NULL : new ListNode(L->info,copy(L->next));
}

String::ListNode * String::ListNode::append(ListNode * L1, ListNode * L2)
{
	return L1 == NULL ? copy(L2) : new ListNode(L1->info, append(L1->next, L2));
}

int String::ListNode::length(ListNode * L)
{
	return L == NULL ? 0 : 1 + length(L->next);
}

String::ListNode * String::ListNode::reverse(ListNode * L)
{
	ListNode * head = L;
	ListNode * temp = NULL;
	while(head!=NULL)
	{
		temp = new ListNode(head->info,temp);
		head = head->next;
	}
	return temp;
}

int String::ListNode::compare(ListNode * L1, ListNode * L2)
{
	if(L1 != NULL && L2 != NULL)
	{
		return (L1->info-L2->info)!=0 ? (L1->info-L2->info):compare(L1->next,L2->next);
	}
	if(L1 != NULL)
	{
		return L1->info - 0;
	}
	if(L2 != NULL)
	{
		return L2->info - 0;
	}
}

void String::ListNode::deleteList(ListNode * L)
{
	if(L != NULL)
	{
		deleteList(L->next);
		delete L;
	}
}



//String
String::String( const char * s):head(ListNode::stringToList(s))
{
}

String::String( const String & s )
{
	head = ListNode::copy(s.head);
}

String String::operator = ( const String & s )
{
	ListNode::deleteList(head);
	head = ListNode::copy(s.head);
	return *this;
}

char & String::operator [] ( const int index )
{
	ListNode * temp = head;
	if(inBounds(index))
	{
		for(int i = index;i>0;--i)
		{
			temp = temp->next;
		}
		return temp->info;
	}
	cerr<<"OUT OF RANGE"<<endl;
	return temp->info;
}

int String::size() const
{
	return ListNode::length(head);
}

int String::indexOf(char c) const
{
	ListNode * temp = head;
	int index = 0;
	while(temp != NULL)
	{
		if(temp->info == c)
		{
			break;
		}
		++index;
		temp = temp->next;
	}

	return index;
}

bool String::operator == ( const String & s ) const
{
	return ListNode::compare(head,s.head) == 0 ? 1 : 0;
}

bool String::operator < ( const String & s ) const
{
	return ListNode::compare(head,s.head) < 0 ? 1 : 0;
}

String String::operator + ( const String & s ) const
{
	String ret;
	ListNode::deleteList(ret.head);
	ret.head = ListNode::append(head,s.head);
	return ret;
}

String String::operator += ( const String & s )
{
	ListNode * temp = ListNode::append(head,s.head);
	ListNode::deleteList(head);
	head = temp;
	return *this;
}

String String::reverse() const
{
	String ret;
	ListNode::deleteList(ret.head);
	ret.head = ListNode::reverse(head);
	return ret;
}

void String::print( ostream & out ) const
{
	for(ListNode * temp = head;temp != NULL;temp = temp->next)
	{
		out<<temp->info;
	}
	out<<'\0';
}

void String::read( istream & in )
{
	ListNode::deleteList(head);
	char arr[256];
	in.getline(arr,256);
	head = ListNode::stringToList(arr);
}

String::~String()
{
	ListNode::deleteList(head);
}

//input output
ostream & operator << ( ostream & out, String str )
{
	str.print(out);
	return out;
}

istream & operator >> ( istream & in, String & str )
{
	str.read(in);
	return in;
}
