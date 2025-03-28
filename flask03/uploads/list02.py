#예제 - 아래는 5명의 학생들의 성적을 입력 받아서 최고값, 최소값, 평균값, 특정 점수 이상의 count 프로그램

STUDENTS = 5
lst = []
count = 0

for i in range(STUDENTS):
    value = int(input(f"{i+1}번째 학생의 성적을 입력하세요."))
    lst.append(value)

print(f"최대 점수 : {max(lst)}")
print(f"최소 점수 : {min(lst)}")
print(f"평균 점수 : {sum(lst)/len(lst)}")

for score in lst:
    if score >= 80:
        count += 1  #count = count +1

print(f"80점 이상 학생 수 : {count}")