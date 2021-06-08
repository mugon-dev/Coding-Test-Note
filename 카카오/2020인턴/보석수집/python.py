def solution(gems):
    answer = []
    # 보석 종류
    gem_count = len(set(gems))
    # 구매한 보석 담을 곳
    contain = {}
    start, end = 0,0
    # 구매하는 구간
    length = len(gems)+1

    # 구매하는 구간의 끝이 진열대 안넘도록
    while end < len(gems):
        # 현재 구매할려는 보석이 구매 리스트에 없다면
        if gems[end] not in contain:
            # 구매 리스트에 등록 후 하나 샀다고 표시
            contain[gems[end]] = 1
        else:
            # 이미 등록되어 있으면 
            contain[gems[end]] += 1
        # 다음 보석으로
        end += 1
        
        # 모든 종류의 보석을 샀다면
        if len(contain) == gem_count:
            # 시작 위치를 하나씩 올라가면서
            while start < end:
                # 시작위치의 보석이 1개 초과라면
                if contain[gems[start]] > 1:
                    # 해당 위치 보석을 빼고
                    contain[gems[start]] -= 1
                    # 시작위치를 하나 증가
                    start += 1
                # 구매하는 구간이 이전보다 짧다면
                elif length > end - start:
                    # 현재 구간을 저장
                    length = end - start
                    # 반환
                    answer = [start+1,end]
                    # if 문을 빠져나감
                    break
                else:
                    break
    return answer