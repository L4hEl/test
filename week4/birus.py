def birus():
    birus_n, hour = map (int, input('세균의 수와 시간을 입력해주세요. : ').split(' '))
    print (f'처음엔 {birus_n}마리')
    for i in range(1,hour+1):
        birus_n *= 2
        print (f'{i}시간후엔 {birus_n}마리')
    return birus_n, hour
if __name__ == "__main__":
    birus()