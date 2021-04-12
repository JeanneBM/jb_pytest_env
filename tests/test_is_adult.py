import pytest
from src.is_adult import is_adult

def test_is_adult():
  
  #given
  age = 18
  
  #when
  result = is_adult(age)
  
  #then
  assert result
  assert is_adult(20)
  
