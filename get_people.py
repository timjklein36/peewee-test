from person import Person
from dimensions import Dimensions


def is_taller_than(dimensions, test_height):
    return dimensions.height > test_height


min_height = 3.0

tall_people = Person.select().join(Dimensions).where(
                is_taller_than(Person.dimensions, min_height)
            )

print('Tall people:')
for person in tall_people:
    print('Id:', person.id, ', Height:', person.dimensions.height)
