import java.util.*;

public class SeriesSum 
{
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int sum = 0;
    for(int i =1;i<n+1;i++)
    {
        for(int j=1; j<i+1;j++)
        {
            sum+=(j*j);
        }
    }
System.out.println(sum);
    
  }
}