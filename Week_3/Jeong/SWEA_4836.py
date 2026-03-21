t = int(input())

for i in range(t):
  
  n = int(input())
  red_grid = [[0 for i in range(10)] for _ in range(10)]
  blue_grid = [[0 for i in range(10)] for _ in range(10)]
  cnt = 0
  
  for _ in range(n):
    r1, c1, r2, c2, color = map(int, input().split())

    if color == 1:
      
      for j in range(r1, r2 + 1):
        for k in range(c1, c2 + 1):
          red_grid[j][k] = 1
          
    else:
      
      for j in range(r1, r2 + 1):
        for k in range(c1, c2 + 1):
          blue_grid[j][k] = 1
  
  
  for j in range(10):
    for k in range(10):
      if red_grid[j][k] == 1 and blue_grid[j][k] == 1:
        cnt += 1
  
  print(f"#{i + 1} {cnt}")
  
# 가?벼운 브루트포스