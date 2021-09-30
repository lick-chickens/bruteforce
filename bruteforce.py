# ----------------------
#
# >> 'AbC'
#
# << ['A', 'B', ...'AA', 'BA', ...'CCC']
#
# ----------------------

# Vars
character_set = input("Input set: ")  # The character set used to generate outputs
verbose_mode = True if input("Verbose mode? [y/n]: ") == "y" else False  # Enable printing as you go or all at once?
results = []  # Store outputs in memory

# Setup
current_iteration_index = []  # Current result

# Main loop
while not current_iteration_index == [len(character_set) - 1] * len(character_set):
    editing_index = -1  # Current index to edit
    # Index loop
    for index in range(iterated_len := len(current_iteration_index)):  # Iterate current result
        if not current_iteration_index[index] == len(character_set) - 1:  # If upto index is not finalized
            editing_index = index  # Found upto index
            break
    if editing_index == -1:  # Requires new length (total)
        current_iteration_index = [0] * (iterated_len + 1)
        print("".join([character_set[item] for item in current_iteration_index])) if verbose_mode else results.append(
            "".join([character_set[item] for item in current_iteration_index]))  # Add result
    else:
        current_iteration_index[editing_index] += 1  # Iterate current index
        for replacement_index in range(editing_index):  # Reset previous indexes
            current_iteration_index[replacement_index] = 0
        print("".join([character_set[item] for item in current_iteration_index])) if verbose_mode else results.append(
            "".join([character_set[item] for item in current_iteration_index]))  # Add result

# Show output
if not verbose_mode:
    print(results)
