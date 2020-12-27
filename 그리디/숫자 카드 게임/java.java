import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int result = 0;
    int[] value = new int[m];
    int[] min_value = new int[n];
    System.out.println("n: "+n+" m: "+m);
    for(int i=0;i<n;i++){
      for(int j=0;j<m;j++){
        value[j] = sc.nextInt();
      }
      Arrays.sort(value);
      min_value[i] = value[0];
    }
    Arrays.sort(min_value);
    System.out.println(min_value[n-1]);
  }
}