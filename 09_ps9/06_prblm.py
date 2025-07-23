with open("log.txt") as f:
   content =  f.read()

if("python" in content):
   print("Yes present")
else:
   print("No not present")