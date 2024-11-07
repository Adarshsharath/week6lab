input_list = [4, 6, 2, 6, 7, 2, 2, 4, 7, 6, 4]
freq_dict = {}
for num in input_list:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

sorted_elements = []
for num in freq_dict:
    sorted_elements.append((num, freq_dict[num]))

# Sort by frequency (highest first), and by value if frequencies are the same (lowest first)
sorted_elements.sort(key=lambda x: (-x[1], x[0]))  # Sort by -frequency (descending) and value (ascending)

sorted_list = []
for num, freq in sorted_elements:
    sorted_list.extend([num] * freq)


print(sorted_list)
