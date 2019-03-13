#include<iostream>
#include<fstream>
#include<string>
#include<utility>
#include<iterator>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
int main()
{
	string line;
	set<string> st;
	map<string,int> stl;
	ifstream file("sample_doc.txt");
	istream_iterator<string> it_file(file);
	ifstream stop("stopwords.txt");
	istream_iterator<string> it_stop(stop);
	ofstream fre("frequency.txt");
	if(file.is_open() && stop.is_open())
	{
		copy(it_stop,istream_iterator<string>(),inserter(st,st.begin()));
		for_each(st.begin(), st.end(), [&](string s){transform(s.begin(), s.end(), s.begin(), ::tolower);});
		for_each(it_file, istream_iterator<string>(), [&](string s)
		{
			transform(s.begin(),s.end(),s.begin(),::tolower);
			if(st.find(s)==st.end())
			{
				stl[s]++;
			}
		});
		for_each(begin(stl), end(stl), [&fre](const pair<const string, int>& p)
		{
			fre<<p.first<<":"<<p.second<<endl;
		});
	}
	file.close();
	stop.close();
	fre.close();	
	return 0;
};
