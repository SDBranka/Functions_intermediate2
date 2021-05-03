#1. Update Values in Dictionaries and Lists
print("---Update Values in Dictionaries and Lists---")

def update_values(x_list, stud_list, sport_dict, z_list):
    for i in range(len(x_list)):            # -Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
        # print(x_list[i])
        for j in range(len(x_list[i])):
            # print(x_list[i][j])
            if(x_list[i][j] == 10):
                x_list[i][j] = 15
    stud_list[0]["last_name"] = "Bryant"             # -Change the last_name of the first student from 'Jordan' to 'Bryant'
    for val in sport_dict:              # -In the sports_directory, change 'Messi' to 'Andres'
        # print(sport_dict[val])
        for player in range(len(sport_dict[val])):
            if(sport_dict[val][player] == 'Messi'):
                sport_dict[val][player] = 'Andres'
    for dict in range(len(z_list)):                # -Change the value 20 in z to 30
        # print(z_list[dict])
        for val in z_list[dict]:
            if(z_list[dict][val] == 20):
                z_list[dict][val] = 30
            
    return x_list, stud_list, sport_dict, z_list


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x_after, students_after, sports_dir_after, z_after = update_values(x, students, sports_directory, z)
print(f"x now = {x_after}. students now = {students_after}.\nsports_directory now = {sports_dir_after}. z now = {z_after}")


#2. Iterate Through a List of Dictionaries
# -Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
# 
# # iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
print("\n\n---Iterate Through a List of Dictionaries---")

# def iterateDictionary(stud_list):             #works, but trying for bonus below
#     for dict in range(len(stud_list)):
#         # print(i)
#         # print(stud_list[dict])
#         for key, val in stud_list[dict].items():
#             print(key, " - ", val)

def iterateDictionary(stud_list):
    for dict in range(len(stud_list)):
        st_list = []
        for key, val in stud_list[dict].items():
            st_list.append(key)
            st_list.append(val)
        print(f"{st_list[0]} - {st_list[1]}, {st_list[2]} - {st_list[3]}")


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


iterateDictionary(students)



#3. Get Values From a List of Dictionaries
# -Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel
print("\n\n---Get Values From a List of Dictionarie---")

def iterateDictionary2(name, studs):
    for dict in range(len(studs)):
        for key in studs[dict]:
            if(key == name):
                print(studs[dict][key])


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


# iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


# 4. Iterate Through a Dictionary with List Values - Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
#
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
#
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
print("\n\n---Iterate Through a Dictionary with List Values---")

def printInfo(a_dict):
    for val in a_dict:
        # print(a_dict[val])
        print(f"{len(a_dict[val])} {val.upper()}")
        for i in range(len(a_dict[val])):
            print(a_dict[val][i])
        print("\n")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

