def convert_base(number, from_base, to_base):
  base_10_number = int(str(number), from_base)
  target_base_number = ""
  while base_10_number > 0:
    remainder = base_10_number % to_base
    target_base_number = str(remainder) + target_base_number
    base_10_number //= to_base
  return target_base_number
number_to_convert = input("Enter the number to convert: ")
source_base = int(input("Enter the source base: "))
target_base = int(input("Enter the target base: "))
result = convert_base(number_to_convert, source_base, target_base)
print(f"The result in base {target_base}: {result}")