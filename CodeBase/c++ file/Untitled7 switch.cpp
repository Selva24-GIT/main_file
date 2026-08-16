#include<iostream>
#include<string>
#include"max.h"
using namespace std;

int main()
{
	float a,b;
	char oppracation;
cout<<"num1 :";
cin>>a;
cout<<"oppracation :";
cin>>oppracation;
cout <<"num2 :";
cin>>b;

switch(oppracation)

{
case '+':
cout<<add(b,a)<<"\n";
break;
case '-':
cout<<sub(b,a)<<"\n";
break;
case '*':
cout<<mul(b,a)<<"\n";
break;
case '/':
cout<<div(a,b)<<"\n";
break;	
default :cout<<"you ender the wrong answer";
}




}
