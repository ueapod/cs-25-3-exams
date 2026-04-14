def check_polindrome 
  left,right = 0,len(s) - 1

  while left < right:
     if s[left] == ' ':
    left += 1
   elif s[right] ==' ':
     right -= 1 
    elif s[left].lower() l= s[right].lower()
       return "Нет"
     else:
      left += 1 
      right -= 1 
    return "Да"

   text = input("Введите строку: ")
   print(check_palindrome(text))