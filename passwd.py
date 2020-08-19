password ='a123456'
x = 3
while True:
    pwd = input ('請輸入密碼: ')
    if pwd == password:
        print ('登入成功!')
        break
    else:
        x = x - 1
        print ('登入失敗，您剩', x, '次機會。')
        if x == 0:
            print('錯誤三次，帳號已鎖定')
            break
