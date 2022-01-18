def merge(priority):
    # if priority array only has one element then it is by default sorted
    if len(priority) > 1:
        left_subarray = priority[:len(priority) // 2]
        right_subarray = priority[len(priority) // 2:]

        # recursively break own the priority array
        merge(left_subarray)
        merge(right_subarray)

        # merge the final sub arrays back together in aqscending order

        left_array_index = 0
        right_array_index = 0
        merged_array_index = 0

        while left_array_index < len(left_subarray) and right_array_index < len(right_subarray):
            if left_subarray[left_array_index] < right_subarray[right_array_index]:
                priority[merged_array_index] = left_subarray[left_array_index]
                left_array_index += 1
            else:
                priority[merged_array_index] = right_subarray[right_array_index]
                right_array_index += 1
            merged_array_index += 1

        while left_array_index < len(left_subarray):
            priority[merged_array_index] = left_subarray[left_array_index]
            left_array_index += 1
            merged_array_index += 1

        while right_array_index < len(right_subarray):
            priority[merged_array_index] = right_subarray[right_array_index]
            right_array_index += 1
            merged_array_index += 1


items = []  # initialise an empty array that will be populated with list items based on user input
priority_list = []  # initialise an empty array that will be populated with priorities of items based on user input

# while True allows the user to add as many items as they would like
while True:
    item1 = (input('Add an item to the to-do list: '))
    items.append(item1)
    priority1 = (input('priority rating - literally use any number: '))
    priority_list.append(int(priority1))
    check = input('Would you like to add more items? - type *anything* for YES; No for NO : ')
    if check == 'No':
        break

# create a dictionary using the priorities as keys and the items as values
to_do_list = dict(zip(priority_list, items))

# apply the merge function created above to update the priority_list array to be sorted in ascending order
merge(priority_list)

# this line converts the to_do_list dict into an ordered dictionary based on priority from highest to lowest
ordered_todolist = {k: to_do_list[k] for k in priority_list[::-1]}

print(ordered_todolist)
