#include<iostream>
#include<string>
using namespace std;
int main()
{
	int total=0;
	int number[3];
	   for(int i=0; i<3; i++ )
		{
			cin>>number[i];
			
	       total=total+number[i];
		
		}
		
		cout <<"total value"<<"\n"<<total<<" ";
		
	
	/*	switch(total%2==0,total%2==1)
		{
			case 0:
			cout <<"even";
			break;
			case 1:
			cout <<"odd";
			break;
				
		}
	*/
		
	if (total%2==0)
	cout <<"even";
	else if (total%2==1)
	cout <<"odd";	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		return 0;
		
	
}
		
