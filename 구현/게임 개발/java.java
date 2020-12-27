import java.util.*;
class Main {
  static int[][] map;
  static boolean[][] visit;
  static int playerDir;
  static int playerRowPos;
  static int playerColPos;

  //북동남서 방향 지정
  static int[] dRow = {-1,0,1,0};
  static int[] dCol = {0,1,0,-1};

  static void turnPlayer(){
    playerDir -= 1;
    if(playerDir < 0){
      playerDir = 3;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int mapRow = sc.nextInt();
    int mapCol = sc.nextInt();

    //지도 그리기
    map = new int[mapRow][mapCol];
    //방문 했던 곳 표시 default false
    visit = new boolean[mapRow][mapCol];

    playerRowPos = sc.nextInt();
    playerColPos = sc.nextInt();
    playerDir = sc.nextInt();

    visit[playerRowPos][playerColPos] = true;

    for(int i=0; i<mapRow; i++){
      for(int j=0; j<mapCol; j++){
        map[i][j] = sc.nextInt();
      }
    }

    int count = 0;
    int visitCount = 1;
    while(true){
      turnPlayer();
      if((map[playerRowPos + dRow[playerDir]][playerColPos + dCol[playerDir]] == 0) &&(visit[playerRowPos + dRow[playerDir]][playerColPos + dCol[playerDir]] == false)){
        visit[playerRowPos + dRow[playerDir]][playerColPos + dCol[playerDir]] = true;
        visitCount++;

        playerRowPos += dRow[playerDir];
        playerColPos += dCol[playerDir];
        count = 0;
      }else{
        count++;
      }
      if(count==4){
        if(map[playerRowPos - dRow[playerDir]][playerColPos - dCol[playerDir]]==1){
          break;
        }else{
          count = 0;
          playerRowPos -= dRow[playerDir];
          playerColPos -= dCol[playerDir];
        }
      }
    }

  System.out.print(visitCount);

  }
}