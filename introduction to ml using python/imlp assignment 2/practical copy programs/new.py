set_1={24,25,72,84}
set_2={25,72,57,89}
print(set_1[1])
print(f"The intersection of both The sets is below: \n{set_1.intersection(set_2)}")
print(f"Union of both The sets is below:\n{set_1.union(set_2)}")
print(f"The difference of The sets is below:\n{set_1.difference(set_2)}")
print(f"The symmetric difference of The sets is below:\n{set_1.symmetric_difference(set_2)}")
print(f"The cleared set is below:\n{set_1.clear(),"\n",set_2.clear()}")