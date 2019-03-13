#include<iostream>
#include "Matrix.h"

template
  <typename T>

void fillMatrix( Matrix <T> & m )
{
  int i, j;
  for ( i = 0; i < m.numRows(); i++ )
    m[i][0] = T();
  for ( j = 0; j < m.numCols(); j++ )
    m[0][j] = T();
  for ( i = 1; i < m.numRows(); i++ )
    for ( j = 1; j < m.numCols(); j++ )
    {
      m[i][j] = T(i * j);
    }
}

void generate_exception( Matrix <double>& m )
{
	for(int row=0;row<=m.numRows();++row)
	{
		for(int col=0;col<=m.numCols();++col)
		{
			m[row][col];
		}
	}
}

void test_double_matrix_exceptions()
throw()
{
	try
	{
		cout << "Starting...\n";
		Matrix < double > M(8,10);
		fillMatrix( M );
		cout << M;
		generate_exception( M );
	}
	catch(const IndexOutOfBoundsException &e)
	{
		cout << "Index out of bounds"<<endl;
	}
	cout << "Done\n";
}

int main()
{
   for (int i=0; i<3; ++i)
   {
       test_double_matrix_exceptions();
   }
   return 0;
}
