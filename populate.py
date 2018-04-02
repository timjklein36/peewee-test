from person import Person
from dimensions import Dimensions


def main():
    # create two people
    dim_one = Dimensions.create(height=6.2, weight=250.0)
    dim_two = Dimensions.create(height=5.9, weight=180.0)
    person_one = Person.create(dimensions=dim_one)
    person_two = Person.create(dimensions=dim_two)


if __name__ == "__main__":
    main()
