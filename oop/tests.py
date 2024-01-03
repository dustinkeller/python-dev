class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    @classmethod
    def about_species(cls):
        print(f"Cats are {Cat.species}s, which makes them similar to humans.")
    
    
    @staticmethod
    def about_species2():
        print(f"Cats are cool, aren't they?")


#1
cat1 = Cat("Whiskers", 1)
cat2 = Cat("Mittens", 3)
cat3 = Cat("Gumball", 10)

cats = [cat1, cat2, cat3]

def oldest_cat(cat_list):
    oldest = cat_list[0].age

    for cat in cat_list:
        if cat.age > oldest:
            oldest = cat.age
    
    return oldest

print(f"The oldest cat is {oldest_cat(cats)} years old.")


print(Cat.about_species())