import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        
        double a = x-(x*0.1);
        double b = x-100;
        double res = Math.min(a,b);
        System.out.println((int)res);
    }
}
