#include<iostream>
#include<string>
int main()
{
	std::string name,age;
	std::cout<<"what is your name?";
	std::cin>>name;
	std::cout<<"what is your age?";
	std::cin>>age;
	int tamil2,english3,maths4;
	std::cout<<"tamil mark";
	std::cin>>tamil2;
	std::cout<<"english mark";
	std::cin>>english3;
	std::cout<<"maths mark";
	std::cin>>maths4;
	std::cout<<"name:"<<name<<"\n"<<"age:"<<age<<"\n"<<"tamil:"<<tamil2<<"\n"<<"english:"<<english3<<"\n";
	std::cout<<"maths:"<<maths4<<"\n";
	std::cout<<"total:"<<tamil2+english3+maths4<<"\n";
	std::cout<<"avrage:"<<(tamil2+english3+maths4)*3<<"%";
	return 0;	
	
}
