class SuperList(list):
    def __len__(self):
        return 100
    
test = SuperList()

print(issubclass(SuperList, list))

print(isinstance(test, list))
