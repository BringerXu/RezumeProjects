#include<iostream>
using namespace std;
#define MAXLEN 128
  class String
  {
  public:
    explicit String( const char * s = "")
    {
    	strcpy(buf,s);
    }

    String( const String & s )
    {
    	strcpy(buf,s.buf);
    }

    String operator = ( const String & s )
    {
    	strcpy(buf,s.buf);
    	return *this;
    }

    char & operator [] ( int index )
    {
    	if(!inBounds(index))
    	{
    		index = 0;
    	}
    	return buf[index];
    }

    int size()
    {
    	return strlen(buf);
    }

    String reverse()
    {
    	String ret;
    	strrev(ret.buf,buf);
    	return ret;
    }

    int indexOf( const char c )
    {
    	return strchr(buf, c) - buf;
    }

    int indexOf( const String pattern )
    {
    	return strstr(buf,pattern.buf) - buf;
    }
    bool operator == ( const String s )
    {
    	return strcmp(buf,s.buf) == 0;
    }

    bool operator != ( const String s )
    {
    	return strcmp(buf,s.buf) != 0;
    }

    bool operator > ( const String s )
    {
    	return strcmp(buf,s.buf) > 0;
    }

    bool operator < ( const String s )
    {
    	return strcmp(buf,s.buf) < 0;
    }

    bool operator <= ( const String s )
    {
    	return (strcmp(buf,s.buf) < 0 || strcmp(buf,s.buf) == 0);
    }

    bool operator >= ( const String s )
    {
    	return (strcmp(buf,s.buf) > 0 || strcmp(buf,s.buf) == 0);
    }

    String operator + ( const String s )
    {
    	return String(strcat(buf,s.buf));
    }

    String operator += ( const String s )
    {
    	strcat(buf,s.buf);
    	return *this;
    }

    void print( ostream & out )
    {
    	out<<buf;
    }

    void read( istream & in )
    {
    	in.getline(buf,MAXLEN);
    }

    ~String(){}

  private:
    bool inBounds( int i )
    {
      return i >= 0 && i < strlen(buf);
    }

    static int strlen( const char *s ){
    	return !*s ? 0:1 + strlen(++s);
    }

    static char * strcpy( char *dest, const char *src )
    {
    	char * ret = dest;
    	while(*dest++ = *src++)
    	{
    		;
    	}
    	return ret;
    }

    static char * strcat(char *dest, const char *src)
    {
    	strcpy(dest+strlen(dest),src);
    	return dest;
    }

    static int strcmp( const char *left, const char *right )
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

    static int strncmp( const char *left, const char *right, int n )
    {
    	for(;n--;++left,++right)
    	{
    		if(*left != *right)
    		{
    			return *left - *right;
    		}
    	}
    	return 0;
    }

    static char * strchr(char *str, int c )
    {
    	return !*str ? 0 : *str == c ? str : strchr(str+1,c);
    }

    static const char * strstr( const char *haystack, const char *needle )
    {
    	int len = strlen(needle);
    	while(*needle)
    	{
    		if(*needle == *haystack++ && haystack != '\0' && needle != '\0')
    		{
    			int cmp = strncmp(haystack,needle,len);
    			if(cmp == 0)
    			{
    				return haystack;
    			}
    		}
    	}
    	return NULL;
    }

    static char * strstr( char *haystack, const char *needle )
    {
    	int len = strlen(needle);
    	while(*needle)
    	{
    		if(*needle == *haystack++ && haystack != '\0' && needle != '\0')
    		{
    			int cmp = strncmp(haystack,needle,len);
    			if(cmp == 0)
    			{
    				return haystack;
    			}
    		}
    	}
    	return NULL;
    }

    static char * strrev(char *dst, char *src)
    {
    	int len = strlen(src);
    	for(int i=0;i<len;i++)
    	{
    		dst[i] = src[len-i-1];
    	}
    	dst[len] = '\0';
    	return dst;
    }

    char buf[MAXLEN];
  };


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
