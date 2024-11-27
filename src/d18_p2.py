import day18 as d18

with open('../data/d18_input_p1.txt', 'r') as fh:
    nums = fh.readlines()
nums = [d18.read_number(n) for n in nums]

max_mag = 0
max_i, max_j = -1, -1
for i in range(len(nums) - 1):
    for j in range(1, len(nums)):
        m1 = d18.magnitude(d18.add(nums[i], nums[j]))
        m2 = d18.magnitude(d18.add(nums[j], nums[i]))
        m = max(m1, m2)
        if m > max_mag:
            max_mag = m
print(max_mag)
