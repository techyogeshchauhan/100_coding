import math

def solve():
    n, m, k = map(int, input().split())  # Use input() instead of raw_input()

    rooms_boys = math.ceil(n / k)  # No need for float conversion in Python 3
    rooms_girls = math.ceil(m / k)

    total_rooms = rooms_boys + rooms_girls
    print(total_rooms)  # Use print() function

t = int(input())  # Use input() instead of raw_input()
for _ in range(t):
    solve()
