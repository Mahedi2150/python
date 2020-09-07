from collections import deque
bank = deque(['anis','karim','bijoy'])
print(bank)
bank.popleft()
print(bank)

if not bank:
    print("Not person left")