from queue import Queue
n = int(input())

q = Queue()
q.put(1)

count = 0
while not q.empty():
    num = q.get()
    if(num <= n):
        count += 1
    else:
        continue
    q.put(num * 10 + 1)
    q.put(num * 10)

print(count)