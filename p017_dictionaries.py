# Dictionary is a python data type that is used to store key value pairs. 

# Dictionaries are created using pair of curly braces .
# Below shows an example of a dictionary "mobile_directory" which has
# key as name of the person and value as mobile number.

mobile_directory = {
    'binoy' : '9895-055-906',
    'rajesh' : '9775-328-101'
}

# To add an item to the dictionary
mobile_directory['vinod'] = "9895-225-125"

# add another item to the dictionary
mobile_directory['aravind'] = "9895-000-125"

# To retrive an item of dictionary use the syntax dictionary_name['key']
print( "Mobile number of aravind is ", mobile_directory['aravind'] )

# Another method to retrive an item of dictionary 
# Benefit of get method: Returns value of key, if key is not found it returns None, 
# instead on throwing KeyError exception
print( "Mobile number of aravind is (using get method)", mobile_directory.get('aravind') )

# To print the dictionary
print( "Printing entire dictionary", mobile_directory )

# To delete items from dictionary
del mobile_directory['aravind']

# printing mobile_directory after deletion
print( "Printing dictionary after deleting aravind", mobile_directory )

# To loop items in a dictionary
# below example prints the mobile numbers available in the dictionary
print("Looping")
for key in mobile_directory:
    print( mobile_directory[key] )

# Find the length (number of elements) of the dictionary
print( "Number of elements in dictionary = ", len( mobile_directory ) )

# return all keys in a dictionary
print( "Keys in the dictionary:", mobile_directory.keys() )

# to store keys of a dictionary as a list
list_keys = list( mobile_directory.keys() )
print( "List of keys: ",list_keys )

# to store values of a dictionary as a list
list_values = list( mobile_directory.values() )
print( "List of values:", list_values )

# to delete a random item from the dictionary.
# it returns the deleted item as a tuple so that you can use it later if required
deleted_item = mobile_directory.popitem()
print( "Deleted item =", deleted_item )



#### Output of the program #####
# Mobile number of aravind is  9895-000-125
# Mobile number of aravind is (using get method) 9895-000-125
# Printing entire dictionary {'binoy': '9895-055-906', 'rajesh': '9775-328-101', 'vinod': '9895-225-125', 'aravind': '9895-000-125'}
# Printing dictionary after deleting aravind {'binoy': '9895-055-906', 'rajesh': '9775-328-101', 'vinod': '9895-225-125'}
# Looping
# 9895-055-906
# 9775-328-101
# 9895-225-125
# Number of elements in dictionary =  3
# Keys in the dictionary: dict_keys(['binoy', 'rajesh', 'vinod'])
# List of keys:  ['binoy', 'rajesh', 'vinod']
# List of values: ['9895-055-906', '9775-328-101', '9895-225-125']
# Deleted item = ('vinod', '9895-225-125')
