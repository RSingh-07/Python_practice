s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?
print(len(s))  # 2 because int and float are different types, but Python automatically converts the int to float when comparing.
# So 20 (int) and 20.0 (float) are numerically equal.