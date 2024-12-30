#queue
from collections import deque

bank =deque(["A","B","C"])
print(bank)

bank.popleft()
print(bank)
bank.popleft()
print(bank)