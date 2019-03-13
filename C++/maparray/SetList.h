#include<iostream>
#include<iterator>
#include<algorithm>
#include<string>
using namespace std;
template
	<typename T>
struct ListNode
{
	T info;
	ListNode<T> * next;
	ListNode(T newinfo, ListNode<T> * newnext):info(newinfo),next(newnext){}
};

template
	<typename T>
struct SetList
{
	struct iterator
	{
		typedef std::forward_iterator_tag iterator_category;
		typedef iterator LN_it;
		typedef ListNode<T> LNvalue;
		typedef ListNode<T>& LNr;
		typedef ListNode<T>* LNptr;
		typedef ptrdiff_t difference_type;

	private:
		LNptr i;

	public:
		iterator(LNptr I):i(I){}
		LN_it operator++()
		{
			i = i->next;
			return *this;
		}
		LN_it operator++(int postfix)
		{
			LN_it cpy = *this;
			i = i->next;
			return cpy;
		}
		LNr operator*()
		{
			return *i;
		}
		LNptr operator->()
		{
			return i;
		}
		bool operator==(const LN_it&rhs) const
		{
			return rhs.i->info == i->info;
		}
		bool operator!=(const LN_it&rhs) const
		{
			return rhs.i->info != i->info;
		}
	};

public:
	SetList():head(NULL)
	{
	}

	SetList operator=(const SetList cpy)
	{
		head = cpy.head;
		return *this;
	}

	iterator begin()
	{
		return iterator(head);
	}

	iterator end()
	{
		return iterator(NULL);
	}

	iterator insert(string I)
	{
		head = new ListNode<T>(I, head);
		return iterator(head);
	}
		
	~SetList()
	{
		ListNode<T> * temp;
		while(head != NULL)
		{
			temp = head;
			head = head->next;
			delete temp;
		}
	}

private:
	ListNode<T> * head;


};





