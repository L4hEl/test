#각도기
# 0 < angle < 90 : 1
# angle = 90 : 2
# 90< angle < 180 : 3
# angle = 180 : 4
# 0 < angle <= 180 / int angle 

def angle():
    input_angle = int(input('각도를 입력해주세요. : '))
    if (0 < input_angle < 90):
        print('1')
    elif (input_angle == 90):
        print('2')
    elif (90 < input_angle < 180):
        print('3')
    elif (input_angle == 180):
        print('4')
    elif (input_angle > 180):
        print('제한된 각도보다 큽니다')
    elif (input_angle < 0):
        print('제한된 각도보다 작습니다')    
    return input_angle      
if __name__ == "__main__":
    angle()