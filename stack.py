opens = ('[', '{', '(')
close_to_open = {']': '[', '}': '{', ')': '('}  
  
def check(text):
    stack = []
  
    for char in text:       
        if char in opens:
            stack.append(char)
        elif char in close_to_open:
            opening = close_to_open[char]  # simpler retrieval
  
            if stack and (opening == stack[-1]):  # lists are true if not empty, -1 is the last item in a list
                stack.pop()
            else:
                print(len(stack))
                return 'Unbalanced'
  
    if not stack:           # lists are False if empty
        return 'Balanced'
  
string = '{[()]}'

  
print(string, check(string))