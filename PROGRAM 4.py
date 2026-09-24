string = input("Enter a string: ")


if string == string[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")


mid = len(string) // 2

if len(string) % 2 == 0:
    if string[:mid] == string[mid:]:
        print("The string is Symmetrical.")
    else:
        print("The string is not Symmetrical.")
else:
    if string[:mid] == string[mid+1:]:
        print("The string is Symmetrical.")
    else:
        print("The string is not Symmetrical.")
