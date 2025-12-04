from functions.get_file_content import get_file_content

# Test lorem.txt truncation
print("Test: get_file_content('calculator', 'lorem.txt')")
result = get_file_content("calculator", "lorem.txt")
print(f"Content length: {len(result)}")
print(f"Ends with truncation message: {result.endswith(']')}")
print(f"Last 100 chars: ...{result[-100:]}")
print()

# Test main.py
print("Test: get_file_content('calculator', 'main.py')")
result = get_file_content("calculator", "main.py")
print(f"Content length: {len(result)}")
print(result)
print()

# Test nested file
print("Test: get_file_content('calculator', 'pkg/calculator.py')")
result = get_file_content("calculator", "pkg/calculator.py")
print(f"Content length: {len(result)}")
print(result)
print()

# Test file outside working directory
print("Test: get_file_content('calculator', '/bin/cat')")
result = get_file_content("calculator", "/bin/cat")
print(result)
print()

# Test non-existent file
print("Test: get_file_content('calculator', 'pkg/does_not_exist.py')")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)
