# Test cases
import pytest
from owner_pet import Owner
from owner_pet import Pet

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

    owner = Owner("Jim")
    pet = Pet("Clifford", "dog", owner)
    assert pet.owner == owner

    Pet.all_pets = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    Pet.all_pets = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all_pets = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")

    assert pet1 in Pet.all_pets
    assert pet2 in Pet.all_pets
    assert len(Pet.all_pets) == 2

    Pet.all_pets = []

def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    # Add pets to the owner
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    assert owner.get_pets() == [pet1, pet2]

    Pet.all_pets = []

def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)

    assert pet
