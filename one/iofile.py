high_score = [0,2,9]
with open('test.txt', 'a') as f:
    for i in high_score:
        f.write(','+str(i))
with open ('test.txt','r') as f:
    a = []
    a = f.read()
    b = list(map(int,a.split(',')))

print(b)