#include<iostream>
using namespace std;

class String
{
public:
  explicit String(const char * s = "");
  String(const String & s );
  String operator = (const String & s );
  char & operator [] (int index );
  int size();
  String reverse();
  int indexOf(const char c );
  int indexOf(const String pattern);
  bool operator == (const String s);
  bool operator != (const String s);
  bool operator > (const String s);
  bool operator < (const String s);
  bool operator <= (const String s);
  bool operator >= (const String s);
  String operator + (const String s);
  String operator += (const String s);
  void print(ostream & out);
  void read(istream & in);
  ~String();
  static void final_report_on_allocations();

private:
  bool inBounds(int i);
  static int strlen(const char *src);
  static char* strcpy(char *dst, const char *src);
  static char * strchr(char *str, int c );
  static char * strcat(char *dest, const char *src);
  static int strcmp( const char *left, const char *right );
  static char * strrev(char *dst, char *src);
  static char* strdup(const char *src);
  static char * strstr(const char * dst,const char * src);
  char * buf;
  static int allocations;
  static char * new_char_array( int n_bytes );
  static void delete_char_array( char * p );
  static void error( const char * p );


};
ostream & operator << (ostream & out, String str );
istream & operator >> (istream & in, String & str );
