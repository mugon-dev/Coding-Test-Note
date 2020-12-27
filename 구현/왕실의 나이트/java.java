import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String location = sc.next();
    System.out.println(location);

    //유니코드 48 = 숫자 0
    //문자열로 변환한 숫자0을 빼줘야 유니코드에서 숫자로 변환
    int row = location.charAt(1) - '0';
    
    //a1의 첫번째 문자에서 a를 빼고 1을 더함으로써 좌표로 변환
    int col = location.charAt(0) - 'a' + 1;
    
    System.out.println(row+" , "+col);

    // 나이트가 이동가능한 8방향 정의
    int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2};
    int[] dy = {-1, -2, -2, -1, 1, 2, 2, 1};

    int count = 0;
    
    for(int i=0; i<8; i++){
      int nextRow = row + dx[i];
      int nextCol = row + dy[i];
      if((1 <= nextRow && nextRow <= 8) && (1 <= nextCol 
      && nextCol <= 8)){
        count += 1;
      }
    }
    System.out.println(count);
  }
}