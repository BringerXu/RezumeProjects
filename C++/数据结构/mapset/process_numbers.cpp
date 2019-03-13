#include<iostream>
#include<vector>
#include<string>
#include<iterator>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	vector<int> v;
	ifstream rn("rand_numbers.txt");
	istream_iterator<int> it_rn(rn);

	ofstream odd("odd.txt");
	ofstream even("even.txt");

	copy(it_rn,istream_iterator<int>(), back_inserter(v));
	sort(begin(v),end(v));
	for_each(begin(v), end(v), [&even,&odd](int i)
	{
		if(i%2==0)
		{
			even<<i<<endl;
		}
		else
		{
			odd<<i<<endl;
		}
	});
	rn.close();
	odd.close();
	even.close();
	return 0;
}
