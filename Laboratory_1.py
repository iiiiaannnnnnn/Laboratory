#Laboratory Activity 1
#1
def count_vowels(user, vowels = ["a","e","i","o","u"],count = 0):
    for char in user.lower():
        if char in vowels:
            count += 1
    print(f"The number of vowels user use: {count}")
user = str(input("Enter a string: "))
count_vowels(user)

#2
# def make_shirt(size="Large", message="I love python"):
#     print(f"Making a {size} shirt with the message: '{message}'")
# make_shirt()

#3
# def merge_strings(*args):
#     return " ".join(args)
# print(merge_strings("Python", "is", "fun"))

#4
# def setup_applications(app_name,version,**kwargs):
#     config = {"app_name": app_name, 
#               "version": version}
#     config.update(kwargs)
#     return config
# print(setup_applications("MyApp", "1.0", debug=True, port=300,environment="production"))

