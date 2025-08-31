def find_missing_number(numbers):
  numbers.sort()
  expected_number = numbers[0]
  for i in range(len(numbers)):
    if numbers[i] != expected_number:
      return expected_number
    expected_number += 1
  return None 


def remove_duplicates(numbers):
  unique_numbers = []
  for number in numbers:
    if number not in unique_numbers:
      unique_numbers.append(number)
  return unique_numbers


def intersection(list1, list2):
  intersection_list = []
  for element in list1:
    if element in list2 and element not in intersection_list:
      intersection_list.append(element)
  return intersection_list


def union(list1, list2):
  union_list = list1.copy()
  for element in list2:
    if element not in union_list:
      union_list.append(element)
  return union_list


def difference(list1, list2):
  difference_list = []
  for element in list1:
    if element not in list2:
      difference_list.append(element)
  return difference_list




def find_first_duplicate(numbers):
  seen = set()
  for number in numbers:
    if number in seen:
      return number
    seen.add(number)
  return None


def second_largest(numbers):
  if len(numbers) < 2:
    return None
  largest = max(numbers)
  second_largest = float('-inf')  
  for number in numbers:
    if number != largest and number > second_largest:
      second_largest = number
  return second_largest



def common_elements(list1, list2, list3):
  common_elements_list = []
  for element in list1:
    if element in list2 and element in list3 and element not in common_elements_list:
      common_elements_list.append(element)
  return common_elements_list



def sum_of_sublists(list_of_lists):
  total_sum = 0
  for sublist in list_of_lists:
    for element in sublist:
      total_sum += element
  return total_sum