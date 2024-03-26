//9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[]args)throws IOException{
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
        
        int max=0;
        int num=0;
        
        for(int i=0;i<9;i++){
            int a=Integer.parseInt(bf.readLine());
            if(a>max){
                max=a;
                num=i+1;
            }
        }

        
        System.out.println(max);
        System.out.println(num);
        
    }
}