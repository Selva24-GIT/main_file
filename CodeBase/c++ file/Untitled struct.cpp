#include<iostream>
#include<string>
int main()
{

  struct company 
   {
   	int id;
   	int salary;
   	int pension;
   	int redirementamentamount;
   	
   	std::string name,job;
   
   
   };
     company c1={59 , 50000, 20000, 4000000,"selva","hr"};
     company c2={666,230000,40000,8000000,"sethu","manager"};
	 company c3={53,12000,2400,40000,"anu","mop women"};
   
   std::cout<<c3.name;
   
   
   
   
   
   
   
   
   
   return 0;
   }
