import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int x = sc.nextInt();
        
        if (a+b >= x || a+c >= x || b+c >= x){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
    }
}
