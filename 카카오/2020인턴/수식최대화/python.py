def solution(expression):
    answer = 0
    # 연산자 우선 순위 모든 경우의 수
    operators_all = [
        ('+','-','*'),('+','*','-'),
        ('-','+','*'),('-','*','+'),
        ('*','+','-'),('*','-','+')
    ]
    # 배열로 변환
    expression = expression.replace("*",',*,')
    expression = expression.replace("+",',+,')
    expression = expression.replace("-",',-,')
    expression = expression.split(",")

    # 모든 경우의 수에서 하나씩
    for operators in operators_all:
        # 입력 받은 수식 복사
        _ex = expression[:]
        # 연산자 우선순위 받아온 것 중 하나
        for operator in operators:
            # 복사한 수식 배열에 연산자가 있을 때  
            while operator in _ex:
                # 해당 연산자의 index
                i = _ex.index(operator)
                if operator == "*":
                    _ex[i-1] = int(_ex[i-1]) * int(_ex[i+1])
                    # 복사한 배열에서 계산한 수식 빼고 재배열
                    _ex = _ex[:i]+_ex[i+2:]
                if operator == "+":
                    _ex[i-1] = int(_ex[i-1]) + int(_ex[i+1])
                    _ex = _ex[:i]+_ex[i+2:]
                if operator == "-":
                    _ex[i-1] = int(_ex[i-1]) - int(_ex[i+1])
                    _ex = _ex[:i]+_ex[i+2:]
        # 절대값이 가장 큰 결과값 반환
        answer = max(answer,abs(_ex[-1]))
    return answer