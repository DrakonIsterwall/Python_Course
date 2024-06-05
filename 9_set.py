empty_set=set()
print(empty_set)

string_set= {"Red","Yellow","Blue"}
print(string_set)

number_set={5,0,-2,9.01}
print(number_set)

mixed_set={"Hi!",2,4.5,4-3.2J}
print(mixed_set)

print("With .add  .remove  .clear  you can add,remove an element and with clear you can remove all value in a set")

mixed_set.add(1000)
print(mixed_set)
mixed_set.remove(2)
print(mixed_set)
mixed_set.clear()
print(mixed_set)

print ("With frozenset({}) you can make a set that is unchangeable")

frozen_set=frozenset({1,2,3,4})
print(frozen_set)

frozen_set.add(5)

