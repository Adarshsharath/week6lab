students = {
    "Adarsh": 94,
    "Arun": 100,
    "Mithun": 98,
    "sharath": 92
}
highest = 0
for key,value in students.items():
    if value > highest:
        highest = value
        name = key
print(f'The highest marks was scored by {name} and it was {highest}')



        

