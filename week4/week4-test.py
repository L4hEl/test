#문제-1
"""
#나이 출력
#매개변수를 선언하고 문제해결
#정답률 91%
def solution(age):
    answer = 2022 - int(age)+1  
    print(f'2022년 기준 {age}살이므로 {answer}입니다.')
    return answer
solution(40)
"""
"""
#키보드 입력 받아 문제해결
def solution():
    age = int(input('나이를 입력해주세요 : '))
    answer = 2022 - int(age)+1
    print(f'2022년 기준 {age}살이므로 {answer}입니다.')
    return answer
solution()
"""
#문제-2
"""
#문자열안에 문자열
#매개변수를 선언하고 문제해결
#정답률 89%
def solution(str1, str2):
    if str2 in str1:
        answer = 1
        print(f'{str1}에 {str2}가 존재하므로 {answer}를 return합니다.')
    else:
        answer = 2
        print(f'{str1}에 {str2}가 존재하지 않으므로 {answer}를 return합니다.')
    return answer
solution("ab6CDE44efgh22iJKlmno","6CD")
"""
"""
#키보드 입력 받아 문제해결
def solution():
    str1 = str(input('문자열을 입력해주세요 : '))
    str2 = str(input('포함될 문자열을 입력해주세요 : '))
    if str2 in str1:
        answer = 1
        print(f'{str1}에 {str2}가 존재하므로 {answer}를 return합니다.')
    else:
        answer = 2
        print(f'{str1}에 {str2}가 존재하지 않으므로 {answer}를 return합니다.')
    return answer
solution()
"""
#문제=3
"""
#정답률 89%
#매개변수 선언 후 코드 작성
def ice_americano (money):
    coffe = 5500
    answer = print(f'가진 돈은 {money}이며 아메리카노는 {money//coffe}잔 살 수 있고 잔돈은 {money%coffe}입니다')
    return answer
ice_americano(15000)
"""
"""
#키보드 입력을 받고 divmod()함수 사용
#divmod(a,b)는 b를 a로 나눈 값과 나머지를 출력함 
def ice_americano ():
    coffe = int(input('커피 값을 입력해주세요 : '))
    money = int(input('가진 돈을 입력해주세요 : '))
    print(f'가진돈은 {money}이며 커피값은 {coffe}이기 때문에 잔과 잔돈은 각각 {divmod(money,coffe)}입니다.')
ice_americano()
"""
#문제-4
"""
#피자를 모두 동일하게 나눠 먹기
def pizza_event():
    answer = 0
    pizaa_pieces = 7
    n = int(input('사람의 수를 적어주세요 : '))
    if(n % pizaa_pieces !=0):
        print (f'피자 판수는 {n - (n%pizaa_pieces)}입니다.')
    else:
        print (f'피자 판수는 {n//pizaa_pieces}입니다.')
    return answer
pizza_event()
"""
#문제-5
"""
def solution(num_list):
    answer = num_list
    answer.reverse()
    print(answer)
    return answer
solution([1, 2, 3, 4, 5])
"""