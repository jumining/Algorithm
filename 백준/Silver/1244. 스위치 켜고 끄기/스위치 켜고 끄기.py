num_of_switches = int(input())
arr_switch = list(map(int, input().split()))
n_students = int(input())

for _ in range(n_students):
  gender, number = map(int, input().split())

  if gender == 1:  
    for i in range(number - 1, num_of_switches, number):
      arr_switch[i] = 1 - arr_switch[i] 

  else:
    idx = number -1
    arr_switch[idx] = 1 - arr_switch[idx]
    low, high = idx-1, idx+1
    
    while low>=0 and high <num_of_switches and arr_switch[low] == arr_switch[high]:
      arr_switch[low] = 1 - arr_switch[low]
      arr_switch[high] = 1 - arr_switch[high]
      low -= 1
      high += 1

for i in range(0, num_of_switches, 20):
    print(*arr_switch[i:i+20])