class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def get_pets(self):
        """Return all related pets of the owner."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner's list of pets."""
        if not isinstance(pet, Pet):
            raise Exception("The argument must be an instance of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return the list of related pets sorted by name."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Must be one of {}".format(self.PET_TYPES))
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all_pets.append(self)
