import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int count = 0;
    int target = 0;
    while(n != 1){
      target = (n/k)*k;
      count += n - target;
      n = target;
      count += 1;
      n /= k;
    }
    System.out.println(count);
  }
}