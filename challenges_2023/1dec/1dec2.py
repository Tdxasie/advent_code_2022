import re 

def extract_digits(line):
    # Extracts digits (both numerical and spelled out) from the line
    digits = re.findall(r'\d+|[a-zA-Z]+', line)
    # Converts spelled-out digits to numerical digits
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    # Get indices of digit mapping keys in the line
    indices = [line.find(key) for key in digit_mapping.keys() if key in line]
    
    # Extract the corresponding literal digits
    literal_digits = [line[index] for index in indices]
    
    # Combine numerical and literal digits
    digits = [digit_mapping.get(d.lower(), d) if d.isalpha() else d for d in digits + literal_digits]
    
    # Extract the first and last digits
    first_digit = digits[0]
    last_digit = digits[-1]
    
    return int(first_digit + last_digit)

def sum_calibration_values(lines):
    # Calculates the calibration values for each line
    calibration_values = [extract_digits(line) for line in lines if line]
    
    # Returns the sum of all calibration values
    return sum(calibration_values)


with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

print(sum_calibration_values(lines))