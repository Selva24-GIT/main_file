import java.util.Scanner;
public class student
 {
  int mark;
  String name;
  int value;
  student(int a,String b,int c)
  {
     mark =a;
    name =b;
     value =c; 
  
  }  
  
  public static void main(String[]args)
  {
    
    student obj = new student( 20,"selva",50);
  
    student obj2= new student(100,"dev",69);
    System.out.println(obj.mark);
    System.out.print(obj2.name);
  } 
}
