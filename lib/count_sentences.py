#!/usr/bin/env python3

class MyString:
  '''blueprints string'''
  def __init__(self, value=""):
    '''initialize attribute'''
    self.value = value

  @property
  def value(self):
    '''value property'''
    return self._value
  
  @value.setter
  def value(self, value):
    '''set value'''
    if type(value) in (str,):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    '''checks if sentence ends with period'''
    if list(self.value)[len(list(self.value)) -1] == ".":
      return True
    else:
      return False
  
  def is_exclamation(self):
    '''checks if sentence ends with exclamation'''
    if list(self.value)[len(list(self.value))-1] == "!":
      return True
    else:
      return False
  
  def is_question(self):
    '''checks if last value is question mark'''
    if list(self.value)[len(list(self.value))-1] == "?":
      return True
    else:
      return False
    
  def count_sentences(self):
    '''counts'''
    string = self.value.replace("!", ".").replace("?", ".").replace("...", ".")
    sentences = string.split(".")
    non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(non_empty_sentences)

your_string = MyString("howdy.")

print(your_string.is_sentence(), your_string.is_exclamation())