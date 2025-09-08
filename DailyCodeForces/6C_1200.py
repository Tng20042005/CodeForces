n = int(input())
array = list(map(int, input().split()))

alice = 0
bob = 0
alice_time = 0
bob_time = 0
l = 0
r = n - 1
while l <= r:
    while alice_time <= bob_time and l <= r:
        alice_time += array[l]
        l += 1
        alice += 1
    while bob_time < alice_time and l <= r:
        bob_time += array[r]
        r -= 1
        bob += 1

print(alice , bob)