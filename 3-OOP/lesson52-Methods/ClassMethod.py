#3. Class Methods (The "Blueprint Manager")
# These methods are for things that change the entire blueprint for every house ever made. They use cls because they talk to the Class itself, not a specific object.

# Example: Changing the "Type of Wood" used for all houses in the neighborhood.

class House:
    material = "Oak" # Shared by all houses

    @classmethod
    # CLASS METHOD: Uses 'cls' to change the shared material
    def change_material(cls, new_material):
        cls.material = new_material

House.change_material("Maple") # Now all future houses use Maple