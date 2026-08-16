import java.util.Scanner;
import javax.swing.text.StyledEditorKit.ForegroundAction;

class hello {
    public static void main(String[]args)
    {
                
           Scanner scan =new Scanner(System.in);
           System.out.print("ender the fist number: ");
           int a = scan.nextInt();
           System.out.print("ender the second number: ");
           int s = scan.nextInt();
           int total=0;
          
           
           for(int i=a;i<=s;i++)
           {
            if(i%2==1 )
            {
               System.out.println("add number: "+i);
               
             total =total+1;
            }
            
           }
          
           System.out.println("Total add numbers: "+ total);


    }
}
