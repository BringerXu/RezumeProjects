#include "String.h"

void test_constructor_and_print()
{
	cout<<"test_constructor_and_print--------"<<endl;

	String testCaP("Hello World");
	String testCaP2("C++ World");

	cout<<testCaP<<endl;
	cout<<testCaP2<<endl;
}

void test_copy_constructor()
{
	cout<<"test_copy_constructor--------"<<endl;

	String testC("Copy");
	String testC2(testC);
	cout<<testC<<':'<<testC2<<endl;

	String testCopy("Copy2");
	String testCopy2(testCopy);
	cout<<testCopy<<':'<<testCopy2<<endl;
}

void test_assignment()
{
	cout<<"test_assignment--------"<<endl;

	String testA("Assign");
	String testA2 = testA;
	cout<<testA<<':'<<testA2<<endl;

	String testA3("assignment");
	String testA4 = testA3;
	cout<<testA3<<':'<<testA4<<endl;
}

void test_bracket()
{
	cout<<"test_bracket--------"<<endl;

	String test_br("bracket");
	cout<<test_br<<"[5]:"<<test_br[5]<<endl;

	String test_br2("sdfs");
	cout<<test_br2<<"[3]:"<<test_br2[3]<<endl;

}

void test_size()
{
	cout<<"test_size--------"<<endl;

	String testS("Hello World");
	cout<<testS<<':'<<testS.size()<<endl;

	String testS2("Derive");
	cout<<testS2<<':'<<testS2.size()<<endl;
}

void test_reverse()
{
	cout<<"test_reverse--------"<<endl;

	String testRev("Hello");
	String testRev2 = testRev.reverse();
	cout<<testRev<<':'<<testRev2<<endl;

	String testRev3("World");
	String testRev4 = testRev3.reverse();
	cout<<testRev3<<':'<<testRev4<<endl;
}

void test_indexOf()
{
	cout<<"test_indexOf--------"<<endl;

	String testInd("bjherdj");
	cout<<testInd<<"  find d: "<<testInd.indexOf('d')<<endl;

	String testInd2("search");
	cout<<testInd2<<"  find e: "<<testInd2.indexOf('e')<<endl;
}

void test_relation_operators()
{
	cout<<"test_relation_operators--------"<<endl;

	String tR("Ray");
	String tR2 = tR;
	String tR3("Klefstad");
	String tR4("Klefstab");

	cout<<"=="<<endl;
	cout<<tR<<"=="<<tR2<<':'<<(tR==tR2)<<endl;

	cout<<"!="<<endl;
	cout<<tR3<<"!="<<tR4<<':'<<(tR3!=tR4)<<endl;

	cout<<">"<<endl;
	cout<<tR3<<">"<<tR4<<':'<<(tR3>tR4)<<endl;

	cout<<"<"<<endl;
	cout<<tR3<<"<"<<tR4<<':'<<(tR3<tR4)<<endl;

	cout<<">="<<endl;
	cout<<tR<<">="<<tR2<<':'<<(tR>=tR2)<<endl;

	cout<<"<="<<endl;
	cout<<tR<<"<="<<tR2<<':'<<(tR<=tR2)<<endl;
}

void test_add()
{
	cout<<"test_add--------"<<endl;

	String testAdd("U");
	String testAdd2("CI");
	cout<<(testAdd+testAdd2)<<endl;

	String testAdd3("CA");
	String testAdd4("Irvine");
	cout<<(testAdd3+testAdd4)<<endl;
}

void test_addequal()
{
	cout<<"test_addequal--------"<<endl;

	String testAdd("U");
	String testAdd2("CI");
	testAdd += testAdd2;
	cout<<testAdd<<endl;
}

void test_read()
{
	cout<<"test_read--------"<<endl;
	String testRead;
	cin>>testRead;
	cout<<testRead<<endl;
}

int main()
{
	test_constructor_and_print();
	test_copy_constructor();
	test_assignment();
	test_bracket();
	test_size();
	test_reverse();
	test_indexOf();
	test_relation_operators();
	test_add();
	test_addequal();
	test_read();
	String::final_report_on_allocations();
}
