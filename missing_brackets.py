# ReadMe.md 
# To find a missing bracket and check for duplicate method names in Java code using Python. 
# command to run the script  "Python3 test.py"

# In sample java code, we can remove any closing bracket and test, it will indicate the missing bracket with Index position:

# Sample output
"""Missing bracket at index 19: {
Duplicate method found: void printMessage"""



import re

# Example usage:
java_code = """
public class Main {
    public void printMessage() {
        System.out.println("Hello, World!");
    }
    
    public void printMessage() {
        System.out.println("Duplicate method!");
    }
    
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                System.out.println(i);
            }
        }
    }
}
"""


# Method for finding missing brackets
def find_missing_bracket(java_code):
    stack = []
    pattern = r'[{}]'

    for match in re.finditer(pattern, java_code):
        char = match.group()
        if char == '{':
            stack.append(match.start())
        elif char == '}':
            if not stack:
                return match.start()
            stack.pop()

    if stack:
        return stack[-1]
    else:
        return None

# Method for checking duplicate method names
def find_duplicate_method_names(java_code):
    method_names = set()
    pattern = r'(\w+)\s+(\w+)\s*\([^)]*\)\s*\{'

    for match in re.finditer(pattern, java_code):
        access_modifier, return_type = match.group(1, 2)
        method_signature = f"{access_modifier} {return_type}"
        if method_signature in method_names:
            return method_signature
        method_names.add(method_signature)

    return None



missing_bracket_index = find_missing_bracket(java_code)
if missing_bracket_index is not None:
    print(f"Missing bracket at index {missing_bracket_index}: {java_code[missing_bracket_index]}")
else:
    print("No missing brackets found.")

duplicate_method = find_duplicate_method_names(java_code)
if duplicate_method is not None:
    print(f"Duplicate method found: {duplicate_method}")
else:
    print("No duplicate methods found.")

