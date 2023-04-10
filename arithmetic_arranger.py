def empty_spaces(
    numbers):  # Will eliminate all spaces from the numbers inside a list
  new_num = []
  for number in numbers:
    new_num.append(number.replace(' ', ''))
  return new_num


def only_digits(numbers):  # Verify if the list has just numbers
  for number in numbers:
    if not number.isnumeric():
      return False
  return True


def more_than_four(
    numbers):  # Verify if the list has numbers with more than 4 digits
  for number in numbers:
    if len(number) > 4:
      return False
  return True


def arithmetic_arranger(problems, display=False):
  numbers = []
  operators = []
  """
  Hendling errors
  """

  # More than five operation Error handling
  if len(problems) > 5:
    return "Error: Too many problems."

  for operation in problems:

    # Another operator than + or - Error handling
    if '+' not in operation and '-' not in operation:
      return "Error: Operator must be '+' or '-'."
    elif '+' in operation:
      numbers.extend(operation.split('+'))
      operators.append('+')
      numbers = empty_spaces(numbers)
    elif '-' in operation:
      numbers.extend(operation.split('-'))
      operators.append('-')
      numbers = empty_spaces(numbers)

    # Only digit Error handling
    if not only_digits(numbers):
      return 'Error: Numbers must only contain digits.'

    #More than 4 digits Error handling
    if not more_than_four(numbers):
      return 'Error: Numbers cannot be more than four digits.'
  """
  Solving the problem
  """
  # Separate the numbers into 2 list, first row and second row
  first_row = []
  second_row = []
  third_row = []
  fourth_row = []
  for i in range(0, len(numbers), 2):
    first_row.append(numbers[i])
    second_row.append(numbers[i + 1])

  # Add whitespaces and operators so that the numbers have the same lenghts
  # Create the fourth row without white spaces
  for i in range(0, len(first_row)):

    # Verify if the biggest number is in the first row
    if len(first_row[i]) > len(second_row[i]):

      # Create the fourth row before modifing the others row
      if operators[i] == '+':
        fourth_row.append(str(int(first_row[i]) + int(second_row[i])))
      else:
        fourth_row.append(str(int(first_row[i]) - int(second_row[i])))
      second_row[i] = operators[i] + ' ' + ' ' * (
        len(first_row[i]) - len(second_row[i])) + second_row[i]
      first_row[i] = ' ' * 2 + first_row[i]

    # Verify if the biggest number is in the second row
    elif len(first_row[i]) < len(second_row[i]):

      # Create the fourth row before modifing the others row
      if operators[i] == '+':
        fourth_row.append(str(int(first_row[i]) + int(second_row[i])))
      else:
        fourth_row.append(str(int(first_row[i]) - int(second_row[i])))
      first_row[i] = ' ' * (len(second_row[i]) - len(first_row[i]) +
                            2) + first_row[i]
      second_row[i] = operators[i] + ' ' + second_row[i]

    # Verify if the numbers are equal in size
    else:

      # Create the fourth row before modifing the others row
      if operators[i] == '+':
        fourth_row.append(str(int(first_row[i]) + int(second_row[i])))
      else:
        fourth_row.append(str(int(first_row[i]) - int(second_row[i])))
      first_row[i] = ' ' * +2 + first_row[i]
      second_row[i] = operators[i] + ' ' + second_row[i]

    # Create the third row composed by '-'
    third_row.append('-' * len(second_row[i]))

  # Adjust the length of the fourth row to be equal with the others
  for i in range(0, len(third_row)):
    fourth_row[i] = ' ' * (len(third_row[i]) -
                           len(fourth_row[i])) + fourth_row[i]

  arranged_problems = '    '.join(first_row) + '\n' + '    '.join(
    second_row) + '\n' + '    '.join(third_row)

  if display:
    arranged_problems = arranged_problems + '\n' + '    '.join(fourth_row)

  return arranged_problems