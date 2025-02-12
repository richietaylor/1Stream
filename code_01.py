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
# I just did it for integers for the sake of this problem
def sortArray(input: typing.List[int]) -> typing.List[int]:
    # I am using the Bubble Sort algorithm for this problem
    
    # Iterate over the list and compare each element with the next one  
    for i in range(len(input)):
        for j in range(len(input)-1):
            # If the current element is greater than the next one, swap them
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
    return input

if __name__ == "__main__":

    string:str = input("Enter a string: ")
    print("Reversed String" , reverseString(string))
    print("Is Palindrome?: ", isPalindrome(string))

    # Get the array of integers from the user
    array_input = input("Enter a list of integers separated by spaces: ")
    try:
        array = list(map(int, array_input.split()))
        print("Sorted Array:", sortArray(array))
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by spaces.")

    # print(reverseString("Hello World"))
    # print(isPalindrome("baaaab"))
    # print(sortArray([1, 5, 2, 4, 5, 0, -1]))