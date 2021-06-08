def solution(numbers, hand):
    answer = ''
    # 키패드를 배열(좌표)로 표현
    keypad = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        "*":(3,0),0:(3,1),"#":(3,2)
    }
    # 왼쪽 오른쪽을 집합으로 정의
    left, right = set([1,4,7]), set([3,6,9])
    # 왼손, 오른손 위치 초기화
    hand_L, hand_R = "*", "#"
    for num in numbers:
        # 값을 넣을때 마다 왼손, 오른손 위치 지정
        if num in left:
            answer += "L"
            hand_L = num
        elif num in right:
            answer += "R"
            hand_R = num
        else:
            # 현재 손의 좌표에서 누를 번호의 좌표까지의 x,y 거리의 합
            dist_L = abs(keypad[hand_L][0]-keypad[num][0])+abs(keypad[hand_L][1]-keypad[num][1])
            dist_R = abs(keypad[hand_R][0]-keypad[num][0])+abs(keypad[hand_R][1]-keypad[num][1])
            if dist_L == dist_R:
                if hand == "left":
                    answer += "L"
                    hand_L = num
                else:
                    answer += "R"
                    hand_R = num
            elif dist_L < dist_R:
                answer += "L"
                hand_L = num
            else:
                answer += "R"
                hand_R = num
    return answer