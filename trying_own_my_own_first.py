# Given:
# str_x = "Emma is good developer. Emma is a writer"

# Expected Output:
# Emma appeared 2 times.

def number_of_times_substring_appeared(given):
    name = "Emma"
    for i in range(len(given)):
        if given[i] == name:
            return name
    

given_statement = "Emma is good developer. Emma is a writer"
result = number_of_times_substring_appeared(given_statement)
print("Emma appeared ", result)

# does not work kasi need pala ng count()