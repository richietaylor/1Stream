# Code for Interview
import typing

# This function reverses the input string
def reverseString(input: str) -> str:
    # Define output
    output =""  
    # Iterate over the input string in reverse order
    for i in range(len(input)-1, -1, -1):
        output += input[i]
    # Reutrn the reversed string
    return output

# This function returns true if the input string is a palindrome, false otherwise
def isPalindrome(input: str) -> bool:
    # I am using basic Recursion for this problem because I miss Uni :(
    # This assumes that an original String of length 0 is a palindrome,
    # but this makes sense to me (You can read an empty string both ways)

    # Check for base cases
    if len(input) == 0 or len(input) == 1:
        return True
    # Check if the first and last characters are the same
    elif input[0] != input[-1]:
        return False
    # Recursively check the rest of the string
    else:
        return isPalindrome(input[1:-1])


# This function sorts the input list in ascending order
def sortArray(input: typing.List[int]) -> typing.List[int]:
    return input

if __name__ == "__main__":
    print(reverseString("Hello World"))
    print(isPalindrome("baaaab"))