n=input("Enter string: ")

if n.__eq__(n[::-1]):
    print(n," is palindrome")
else:
    print(n," is not palindrome")
