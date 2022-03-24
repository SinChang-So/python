## 1
letters = 'python'
print(letters[0],letters[2])

## 2
string = "PYTHON"
reversed_str = string[::-1]
print(reversed_str)

## 3

url = "http://sharebook.kr"
a = input("\n")
print(url.rfind(a))
index = url.index(a)
# print(type(k))
print(url[index:len(url)+2])




'''
## 4
file_name = "보고서.xlsx"
x = file_name.endswith("xlsx")
print(x)

## 5
file1_name = "2020_보고서.xlsx"
y = file1_name.startswith("2020")
print(y)

## 6
score = int(input("점수를 입력하세요."))
if(score >80):
    print("A학점")
elif(score > 60):
    print("B학점")
elif(score > 41):
    print("C학점")
elif(score >21):
    print("D학점")
elif(score >0):
    print("E학점")
## 7
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소세지", "라면", "팥빙수", "김치전"]
print(len(cook))

## 8
warn_list = input("투자 종목 선택")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
if warn_list in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 목록이 아닙니다.")
## 9
리스트 = [100, 200, 300]

for i in 리스트:
    print(i+10)

리스트1 = ["SK하이닉스", "삼성전자", "LG전자"]
## 10
for i in 리스트1:
    print(len(i))'''


