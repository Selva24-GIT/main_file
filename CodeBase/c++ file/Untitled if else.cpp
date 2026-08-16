 #include<iostream>
#include<string>
 
 int main()
 {
 
   struct student
   {
   	int id;
   	std::string name;
	int age;    
   	
   };
   student s1 ={59 , "selva",18};
   student s2={666 , "sethu",19};
   int a;
   std::cin>>a;
   if (a < 18)  
   std::cout<<s1.age;
   else
   std::cout<<s2.age;
   
   
   return 0;
   }
  
   
   
