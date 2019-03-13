#include<iostream>
#include "SetList.h"
#include<string>
#include<fstream>
#include<iterator>
#include<algorithm>
int main()
{
	SetList<string> sl;

	ifstream stop("stopwords.txt");
	istream_iterator<string> it_stop(stop);
	for_each(it_stop, istream_iterator<string>(), [&](string I)
	{
		sl.insert(I);
	});
	return 0;
}

