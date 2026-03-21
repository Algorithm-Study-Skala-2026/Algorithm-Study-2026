import java.util.Scanner;
import java.util.*;

public class Main {
    public static long D[];
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //값 채워넣는 배열 생성
        D= new long[10];

        D[1] = 9;
        for(int i=2;i<D.length;i++){
            long square = powLong(10, i-1);
            long max = square*10-1;
            D[i] = D[i - 1] + i * ((max / square - 1) * square + max % square + 1);
        }

        //값 구하기
        String stringInput = input.nextLine();
        int length = stringInput.length();
        int num = Integer.parseInt(stringInput);

        System.out.println(digit(length,num));
    }

    static long powLong(long a, long e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res *= a;
            a *= a;
            e >>= 1;
        }
        return res;
    }

    public static long digit(int length,int num){
        long square = powLong(10, length - 1);
        return D[length - 1] + length * ((num / square - 1) * square + num % square + 1);
    }

}
