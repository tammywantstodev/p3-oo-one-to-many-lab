class Pet:
    all=[]
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name, pet_type, owner="John"):
        self.name=name
        self.owner=owner
        if self.check_pet_type(pet_type):
            self.pet_type=pet_type
        else:
            raise Exception('Pet_type is not valid')
        Pet.all.append(self)
    @classmethod
    def check_pet_type(cls, pet_type):
        return pet_type in cls.PET_TYPES
   
class Owner:
    def __init__(self,name):
        self.name=name
        self._owner=None
    
    def pets(self):
       return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self
    def get_sorted_pets(self):
        pet_list = self.pets()
        pet_list.sort(key=lambda pet: pet.name)  
        return pet_list