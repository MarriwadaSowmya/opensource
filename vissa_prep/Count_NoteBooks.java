import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int pages = 1000 * N;
        int notebooks = pages / 100;
        
        System.out.println(notebooks);
    }
}
