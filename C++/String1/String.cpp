#include "String.h"
int String::allocations = 0;
String::String(const char * s)
{
	buf = strdup(s);
}

String::String(const String & s )
{
	buf = strdup(s.buf);
}

String String::operator = (const String & s )
{
	delete_char_array(buf);
	buf = strdup(s.buf);
	return *this;
}

char & String::operator [] (int index )
{
	if(inBounds(index))
	{
		return buf[index];
	}
	return buf[0];
}

int String::size()
{
	return strlen(buf);
}

String String::reverse()
{
	String cpy;
	delete_char_array(cpy.buf);
	cpy.buf = new_char_array(strlen(buf)+1);
	strrev(cpy.buf, buf);
	return cpy;
}

int String::indexOf(const char c)
{
	return strchr(buf,c)-buf;
}

int String::indexOf(const String pattern)
{
	if(strstr(buf,pattern.buf) != 0)
	{
		return strstr(buf,pattern.buf) - buf;
	}
	return 0;
}

bool String::operator == (const String s)
{
	return strcmp(buf,s.buf) == 0;
}

bool String::operator != (const String s)
{
	return strcmp(buf,s.buf) != 0;
}

bool String::operator > (const String s)
{
	return strcmp(buf,s.buf) > 0;
}

bool String::operator < (const String s)
{
	return strcmp(buf,s.buf) < 0;
}

bool String::operator <= (const String s)
{
	return (strcmp(buf,s.buf) < 0 || strcmp(buf,s.buf) == 0);
}

bool String::operator >= (const String s)
{
	return (strcmp(buf,s.buf) > 0 || strcmp(buf,s.buf) == 0);
}

String String::operator + (const String s)
{
	String cpy;
	delete_char_array(cpy.buf);
	cpy.buf = new_char_array(strlen(buf)+strlen(s.buf)+1);
	strcpy(cpy.buf,buf);
	strcat(cpy.buf,s.buf);
	return cpy;
}

String String::operator += (const String s)
{
	String cpy;
	delete_char_array(cpy.buf);
	cpy.buf = new_char_array(strlen(buf)+strlen(s.buf)+1);
	strcpy(cpy.buf,buf);
	strcat(cpy.buf,s.buf);
	delete_char_array(buf);
	buf = strdup(cpy.buf);
	return *this;
}

void String::print(ostream & out)
{
	out<<buf;
}

void String::read(istream & in)
{
	delete_char_array(buf);
	char arr[256];
	in.getline(arr,256);
	buf = strdup(arr);
}

String::~String()
{
	delete_char_array(buf);
}

char* String::strdup(const char *src)
{
	int len = strlen(src);
	char* ret = new_char_array(len+1);
	for(int i=0;i<len;++i)
	{
		ret[i] = src[i];
	}
	ret[len] = '\0';
	return ret;
}

char * String::strrev(char *dst, char *src)
{
	int len = strlen(src);
	for(int i=0;i<len;i++)
	{
	  dst[i] = src[len-i-1];
	}
	dst[len] = '\0';
	return dst;
}

int String::strcmp( const char *left, const char *right )
{
	while(*left != '\0' && *right != '\0')
	{
		if(*left++!=*right++)
		{
			return int(left-right);
		}
	}
	return 0;
}

char * String::strcat(char *dest, const char *src)
{
	strcpy(dest+strlen(dest),src);
	return dest;
}

char *String::strchr(char *str, int c )
{
	return !*str ? 0 : *str == c ? str : strchr(str+1,c);
}

char* String::strcpy(char *dst, const char *src)
{
	char * ret = dst;
	while(*dst++ = *src++)
	{
		;
	}
	return ret;
}

bool String::inBounds(int i)
{
	return i >= 0 && i < strlen(buf);
}

int String::strlen(const char *src)
{
	return !*src ? 0:1 + strlen(++src);
}

ostream & operator << (ostream & out, String str )
{
	str.print(out);
	return out;
}

istream & operator >> (istream & in, String & str )
{
	str.read(in);
	return in;
}

char * String::new_char_array( int n_bytes )
{
	++allocations;
	return new char[n_bytes];
}

void String::delete_char_array( char * p )
{
	--allocations;
	if (allocations < 0) error("more delete[] than new[]");
	delete [] p;
}

void String::error( const char * p )
{
	cerr << "Error (class String): " << p << endl;
}

void String::final_report_on_allocations()
{
	if (allocations > 0)
	{
		error("Memory Leak in class String");
	}
	if (allocations < 0)
	{
		error("Too many delete[]s in class String");
	}
	if (allocations == 0)
	{
		cout << "Allocations & deallocations match\n";
	}
}

char * String::strstr(const char * dst,const char * src)
{
	char * pivot = 0;
	if(*dst && *src)
	{
		for(int i = 0; i < strlen(dst) - strlen(src);++i)
		{
			if(dst[i] == *src)
			{
				pivot = (char *)(dst+=i);
				for(;*src;src++,dst++)
				{
					if(*src != *dst)
					{
						pivot = 0;
						break;
					}
				}
			}
		}
	}
	return pivot;
}










