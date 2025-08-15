a, b = map(int, input().split())
ship_counter = 0

while b:
    ship_counter += a // b 
    a, b = b, a%b

print(ship_counter)