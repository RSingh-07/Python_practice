class Vector:
    def __init__(self, l):
        self.l = l


    def __len__(self):   #Overriding built-in length behavior
        return len(self.l)
    
# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))
