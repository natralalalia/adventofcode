values = set()
analog_values = set()

with open('input.txt', 'r') as f:
    contents = f.read().split('\n')
    for line in contents:
        values.add(int(line))

for value in values:
    analog_values.add(2020 - value)

ans = list(set(values).intersection(analog_values))
print(ans[0] * ans[1])
