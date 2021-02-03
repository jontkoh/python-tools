# CLI tool for getting the sum of all input numbers 

def sum_the_array(numbers):
  new_num_array = []
  for str in numbers:
    string_to_num = float(str)
    new_num_array.append(float("{:.2f}".format(string_to_num)))

  total = 0
  for num in new_num_array:
    total += num

  return float("{:.2f}".format(total))
  

def get_numbers():
  num_array = []

  num = ""

  while True:
    num = input("Enter number(s) to add: ")
    num = num.lower()
    num = num.replace(" ", "")
    num = num.strip()
    if (num == "done" or num == "exit" or num == "-"):
      # this_is_true = False
      break
    
    if "+" in num:
      
      print("\nCurrent numbers: " + "".join(num_array) + num)
      print("Type 'done' to sum\n")
      numList = num.split("+")
      for eachNum in numList:
        num_array.append(eachNum)
    

    if (num =="restart"):
      num_array.clear()

  return num_array
  # return num_array

def main():
  print_str = """ 
      Type or paste a list of numbers separated by "+"
      (ex: 1+2+3+4.1) 
      and hit enter and then type "done" when finished \n 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
      ---Options---\n
      type: 'done' or 'exit' or '-' -> when finished\n
      type: 'restart' -> to redo the count\n
      hit:  enter key when done.\n
      hit:  control+'c' key to cancel program
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
      """
  print(print_str)
  try:
    while(True):
      num_array = get_numbers()
      total = sum_the_array(num_array)
      print("""
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
      Total: {}\n
      program restarting...
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
      """.format(str(total)))
  except:
    print("\n")


if __name__ == "__main__":
  main()
