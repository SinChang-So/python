## 1
'''
j=0
price_list=[32100,32150,32000,32500]
for i in price_list:
    print('%d  %s'%(j,i))
    j = j+1
'''
## 2
j=100
price_list=[32100,32150,32000,32500]    
for i in price_list:
    if i == 32100:
        continue
    print('%d    %s' %(j,i))
    j = j+10

## 3
for i in range(2002,2051):
    print(i)

## 4
## range는 float 형이 안됨 
o = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in o:
    print(i)

## 5
ticker ='btc__krw'
print(ticker.upper())

## 6
file_name = "보고서.xlsx"
if file_name.endswith("xlsx") == True:
    print('파일이 끝났습니다..')

## 7
a = "hello world"
list__void  = a.split()
print(list__void)

## 8
b="2020-05-01"
list__void = b.split('-')
print(list__void)

## 9
samsaung = "5,969,782,550"
sam = samsaung.replace(",","")
print(int(sam))
print(type(int(sam)))

## 10
a = "hello world"
list__void  = a.split()
print(list__void)

## 11
price = ['20180728', 100,130,140,150,160,170]
print(price[1:])

## 12
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

##13
list = [3,100, 23, 44]
for i in list:
    if i%3 == 0:
        print(i)