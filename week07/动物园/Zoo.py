from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,mold,shape,character):
        super().__init__()
        # 类型
        self.mold = mold
        # 体型
        self.shape = shape
        # 性格
        self.character = character
        # 是否凶猛
        self.is_ferocious = self.ferocious()
    
    def ferocious(self):
        if (self.shape =="中" or self.shape =="大") and self.mold =="食肉" and self.character =="凶猛":
            return  True
        else:
            return False

class Cat(Animal):
    voice = ""
    def __init__(self, animal_name, mold, shape, character):
        super().__init__(mold, shape, character)
        self.animal_name = animal_name
        self.is_pet = True

class Zoo(object):
    def __init__(self,zoo_name):
        self.zoo_name = zoo_name
        self.animals = {}
    
    def add_animal(self,animal):
        if animal not in self.animals:
            self.animals[animal] = animal
            return True
        return False

    def __getattr__(self,animal):
        print(self.animals.keys)
        for key in self.animals.keys():
            if animal in str(key):
                print(f'{animal}在动物园中了')
                return True
        return False


if __name__ == "__main__":
    z = Zoo("时间动物园")
    cat1 = Cat("大花猫1","食肉","小","温顺")
    add1 = z.add_animal(cat1)
    add2 = z.add_animal(cat1)
    print(add1)
    print(add2)
    have_cat = getattr(z, 'Cat')
    print(have_cat)