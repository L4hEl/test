def string():
    my_string = str(input('문자열을 입력해주세요 : '))
    my_list = list(my_string)
    my_list.reverse()
    print(my_list)
if __name__ == "__main__":
    string()