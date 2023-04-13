import io
data = {}
with open('input.txt', "r+b") as file:
    data['magic'] = file.read(1).hex()
print(data)