# Input strings
s = "egg"
t = "add"

# Step 1: Check if the lengths of the strings are different
if len(s) != len(t):
    print(False)
else:
    # Create two dictionaries for the mappings
    map_s_to_t = {}
    map_t_to_s = {}
    is_isomorphic = True
    
    # Step 2: Iterate through both strings
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if current char in s is already mapped to a different char in t
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                is_isomorphic = False
                break
        else:
            map_s_to_t[char_s] = char_t
        
        # Check if current char in t is already mapped to a different char in s
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                is_isomorphic = False
                break
        else:
            map_t_to_s[char_t] = char_s
    
    # Step 3: Output the result
    print(is_isomorphic)
