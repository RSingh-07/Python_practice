letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''

# Chaining in strings - calling multiple string methods one after another, in a single expression.
print(letter.replace("<|Name|>","Riya").replace("<|Date|>","7 September 2025"))