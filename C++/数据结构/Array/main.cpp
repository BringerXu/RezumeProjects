#include <iostream>
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
void test_int_matrix()
{
	Matrix<int> m(10,5);
    fillMatrix( m );
    cout << m;
    Matrix<int> m2(10,10);
    fillMatrix(m2);
    cout<<m2;
}
void test_double_matrix()
{
	Matrix<double> M(8,10);
    fillMatrix(M);
    cout<<M;
    Matrix<double> M2(10,8);
    fillMatrix(M2);
    cout<<M2;
}
int main()
{
   test_int_matrix();
   test_double_matrix();
   return 0;
}
