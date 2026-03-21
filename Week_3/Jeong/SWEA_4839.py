t = int(input())

for i in range(t):
  page, a_target, b_target = map(int, input().split())
  
  left = 1
  right = page
  
  now_a = 0
  now_b = 0
  cnt_a = 0
  cnt_b = 0
  
  while True:
    now_a = (left + right) // 2
    cnt_a += 1
    
    if now_a == a_target:
      break
    elif now_a > a_target:
      right = now_a
    else:
      left = now_a
  
  left = 1
  right = page
  
  while True:
    now_b = (left + right) // 2
    cnt_b += 1
    
    if now_b == b_target:
      break
    elif now_b > b_target:
      right = now_b
    else:
      left = now_b
  
  
  if cnt_a < cnt_b:
    print(f'#{i + 1} A')
    
  elif cnt_a > cnt_b:
    print(f'#{i + 1} B')
    
  else:
    print(f'#{i + 1} 0')