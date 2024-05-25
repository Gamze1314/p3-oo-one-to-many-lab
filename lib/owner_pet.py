# Owner feeds pet, pets pleases owner => Association.

class Pet:

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner if isinstance(owner, Owner) else None
        Pet.all.append(self)  # append new instances to all list.

        # validate that the pet_type is one of those types in the __init__ method.
        # raise Exception if this check fails.
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise ValueError(f"{pet_type} is not a valid pet type.")


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # return a full list of owner's pets
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # validate and add pet.
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError(f"{pet} is not a valid pet type.")

    def get_sorted_pets(self):
        # returns a sorted list of pets by their names.
        sorted_pets = self.pets()
        # lambda function returns pet names , and sort() returns sorted list of pets
        sorted_pets.sort(key=lambda pet: pet.name)
        return sorted_pets


# my_pet = Pet("chula", "pitbull", "myself")
# print(my_pet.pet_type)

# owner_obj = Owner("myself")
# print(owner_obj.name)

# pet1 = Pet("Max", "dog")
# pet2 = Pet("Whiskers", "cat")
# pet3 = Pet("Nibbles", "rodent")
# pet4 = Pet("Tweety", "bird")

# # Try to assign an invalid pet type
# try:
#     pet5 = Pet("Spike", "turtle")
# except Exception as e:
#     print(e)
