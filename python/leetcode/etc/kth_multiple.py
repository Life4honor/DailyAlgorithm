# 입력 A,B,K 중 K의 크기에 따라 O(K)의 동일한 시간복잡도로 수행될 것으로 기대됩니다.

# inputs = A,B,K
inputs = 6,8,8

def kth_multiple(inputs):
  multiples = []
  first, second, k = inputs
  first_count, second_count = 1, 1
  while len(multiples) < k:
    first_mul = first*first_count
    second_mul = second*second_count
    if first_mul < second_mul:
      first_count += 1
      multiples.append(first_mul)
      continue
    
    if first_mul > second_mul:
      second_count += 1
      multiples.append(second_mul)
      continue
    
    first_count += 1
    second_count += 1
    multiples.append(first_mul)

  return multiples[-1]

print(kth_multiple(inputs))
