import java.util.Arrays;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    // 배열크기 n , 더해지는 횟수 m , 최대 연속 횟수 k
    //수를 입력받아 배열에 저장
    //배열을 정렬하여 가장 큰수와 두번째로 큰수 찾기
    //제일 큰수를 k번 더하고 두번째 큰수를 한번 더하기
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int k = sc.nextInt();
    System.out.println("n: "+n+" m: "+m+" k: "+k);
     
    int[] arr = new int[n];
    for(int i = 0; i < n; i++){
      arr[i] = sc.nextInt();
    }
    Arrays.sort(arr);
    int first = arr[arr.length-1];
    int second = arr[arr.length-2];
    System.out.println("first: "+first+" second: "+second);
    //k+1만큼 큰수 k번 작은수 1번의 합이 반복됨
    //더해지는 횟수가 m번
    // m / (k+1)이 반복되는 횟수
    int count = m/(k+1);
    //반복되는 합
    int repeatSum = ((first*k)+second)*count;
    System.out.println("repeatSum: "+repeatSum);
    //나버지
    int remainder = m % (k+1);
    //나머지 합
    int remainderSum = 0;
    if(remainder!=0){
      remainderSum = remainder*first;
    }
    System.out.println("remainderSum: "+remainderSum);
    int result = repeatSum + remainderSum;
    System.out.println("result : "+result);

  }
}