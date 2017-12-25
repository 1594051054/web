sample_string = """
name: Kalu
biography: Kalu is a wonderful employee. We love
having him on our team. He makes us great sale.
salary: $200,000


name: Eke
biography: Eke is a so-so employee. We are ambivalent about
having him on our team. He makes us amazing sales though.
salary: $240,000


name: Akin biography: Akin is the hardest worker I've ever seen. Everyone
loves to be around him. salary: $80,000

name: Uche
biography: Uche is an excellent president.
She always goes above and beyond.
salary: $450,000
"""

# How would we get the first name if we did
# not know what name it was?
# Type your code below.

# Get your start_position index
# THE LINE BELOW IS INCOMPLETE!!! PLEASE COMPLETE
start_position_index = sample_string.find("name") # <--- Add your substring argument that you want to search for

# Add count the amount of characters you searched by
# to get to the position number right after your search string above
# THE LINE BELOW IS INCOMPLETE!!! PLEASE COMPLETE
add_count = len() # <----- Pass it the substring you searched, the one you gave as an argument to the .find() above.
start_position_index += add_count

# Get your end_position index
end_position_index = sample_string.find("biography")

# grab your substring using bracket-notation
# and your two position numbers
# THE LINE BELOW IS INCOMPLETE!!! PLEASE COMPLETE
first_name = sample_string[]  # <---- Add your position numbers!

print(first_name)


# How would we get the second name?
# Type your code below.

# Get your start_position index
# THE LINE BELOW IS INCOMPLETE!!! PLEASE COMPLETE
start_position_index2 = sample_string.find("name: ", )  # <--- Add a second argument representing position number where u want to start search from. HINT: We want to start our start from the last end position of the first name.
start_position_index2 += add_count


# Get your end index position
end_position_index2 = sample_string.find("biography", start_position_index2)

# Select your substring using bracket_notation and your position numbers
second_name = sample_string[start_position_index2:end_position_index2]

# print your string
print(second_name)