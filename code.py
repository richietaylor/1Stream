# Code for Interview
import typing

# This function reverses the input string
def reverseString(input: str) -> str:
    output =""  
    for i in range(len(input)-1, -1, -1):
        output += input[i]
    return output

# This function returns true if the input string is a palindrome, false otherwise
def isPalindrome(input: str) -> bool:
    return False

# This function sorts the input list in ascending order
def sortArray(input: typing.List[int]) -> typing.List[int]:
    return input

if __name__ == "__main__":

    print(reverseString("Hello World"))