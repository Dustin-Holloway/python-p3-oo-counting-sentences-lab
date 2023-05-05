# #!/usr/bin/env python3

# class MyString:
#       def __init__(self, value=''):
#            self.value = value
            

#       def set_value(self, variable):
#           if isinstance(variable, str):
#                self._value = variable
#           else: 
#               print("The value must be a string.")
          
#       def get_value(self):
#            return self._value


#       def is_sentence(self):
#            if self._value.endswith("."):
#             return True
#            else:
#             return False
           
#       def is_question(self):
#           if self._value.endswith("?"):
#               return True
#           else:
#               return False
          
#       def is_exclamation(self):
#           if self._value.endswith("!"):
#               return True
#           else:
#               return False
          
#       def count_sentences(self):
#           delimiters = ".?!"
#           count = 0
#           for char in self._value:
#               if char in delimiters:
#                   count += 1
#           return count


#       value = property(get_value, set_value)



class MyString:
    def __init__(self, value=''):
        self._value = value

    def set_value(self, variable):
        if isinstance(variable, str):
            self._value = variable
        else: 
            print("The value must be a string.")

    def get_value(self):
        return self._value
    

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    
    def count_sentences(self):
      delimiters = [".", "?", "!"]
      count = 0
      for char in self._value:
        if char in delimiters:
            count += 1 
      return count
        
    def count_sentences(self):
      delimiters = [".", "?", "!"]
      count = 0
      previous_char = None
      for char in self._value:
        if char in delimiters and (previous_char is None or previous_char not in delimiters):
            count += 1
        previous_char = char
      return count
    