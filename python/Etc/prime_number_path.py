shortest_prime_number_path = []
inputs = "6899 4463"
prime_numbers = [2]


def find_path(inputs):
  current_position, destination = inputs.split()
  
  if current_position == destination:
    return
  
  if current_position not in shortest_prime_number_path:
    shortest_prime_number_path.append(current_position)

  for idx, char in enumerate(destination):
    next_position = current_position[:idx] + destination[idx] + current_position[idx +1:]

    if in_prime_numbers(convert_to_int(next_position)):
      find_path(f"{next_position} {destination}")


def initialize_prime_numbers(inputs):
  left, right = inputs.split()
  maximum_prime_number = max(convert_to_int(left), convert_to_int(right))
  number = 1
  while prime_numbers[-1] < maximum_prime_number:
    number += 1
    if is_prime(number):
      prime_numbers.append(number)

  
def convert_to_int(string_input):
  return int(string_input)


def is_prime(number):
  for prime in prime_numbers:
    if number % prime == 0:
      return False
  return True


def in_prime_numbers(number):
  return number in prime_numbers


initialize_prime_numbers(inputs)
find_path(inputs)

for path in shortest_prime_number_path:
  print(path)
