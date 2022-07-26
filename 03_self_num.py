num = set(range(1, 101)) # num 변수에 1부터 10000까지의 숫자를 저장
gen_num = set() # gen_num 변수에 생성된 숫자를 저장

for i in range(1,101): # 1부터 10000까지 반복
    for j in str(i): # i의 숫자를 스트링으로 변환 후 각 자리수를 반복
        i += int(j) # i에 j를 정수로 변환하여 더함 (i = i + int(j))
    gen_num.add(i) # gen_num에 i를 추가 (gen_num.add(i))
    print(i)

self_num = sorted(num - gen_num) # num - gen_num의 결과를 정렬하여 self_num에 저장 (정렬하지 않으면 순서가 바뀌어서 정렬되지 않음)
for i in self_num:
    print(i)
