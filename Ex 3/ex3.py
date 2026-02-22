# Importing regular expression module
import re


# ---------------------------------------------------------
# Question 1 : Strong Password Validation
# ---------------------------------------------------------
def validate_password(password):
    """
    This function validates a password based on the following rules:
    1. Length must be 8 to 15 characters
    2. Must contain at least one uppercase letter
    3. Must contain at least one lowercase letter
    4. Must contain at least one digit
    5. Must contain at least one special character (@ # $ % & !)
    6. Must NOT start with a digit
    7. Must NOT contain spaces
    8. Must NOT contain same character repeated consecutively
    """

    # Regular Expression Explanation:
    # ^(?!\d)              -> Password must NOT start with a digit
    # (?!.*\s)             -> Password must NOT contain spaces
    # (?!.*(.)\1)          -> No consecutive repeated characters
    # (?=.*[A-Z])          -> At least one uppercase letter
    # (?=.*[a-z])          -> At least one lowercase letter
    # (?=.*\d)             -> At least one digit
    # (?=.*[@#$%&!])       -> At least one special character
    # [A-Za-z\d@#$%&!]{8,15} -> Allowed characters and length 8–15
    # $                    -> End of string

    pattern = r'^(?!\d)(?!.*\s)(?!.*(.)\1)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!])[A-Za-z\d@#$%&!]{8,15}$'

    if re.match(pattern, password):
        print("Valid Password")
    else:
        print("Invalid Password")


# ---------------------------------------------------------
# Question 2 : PAN Number Validation
# ---------------------------------------------------------
def validate_pan(pan):
    """
    This function validates Indian PAN number format:
    1. Exactly 10 characters
    2. First 5 must be uppercase letters
    3. Next 4 must be digits
    4. Last 1 must be uppercase letter
    """

    # ^[A-Z]{5}  -> First 5 uppercase letters
    # [0-9]{4}   -> Next 4 digits
    # [A-Z]      -> Last 1 uppercase letter
    # $          -> End of string

    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

    if re.match(pattern, pan):
        print("Valid PAN Number")
    else:
        print("Invalid PAN Number")


# ---------------------------------------------------------
# Question 3 : Aadhaar Number Validation
# ---------------------------------------------------------
def validate_aadhaar(aadhaar):
    """
    This function validates Aadhaar number:
    1. Exactly 12 digits
    2. Must not start with 0 or 1
    3. Spaces every 4 digits are optional
    """

    # ^[2-9]      -> First digit must be 2–9
    # \d{3}       -> Next 3 digits
    # \s?         -> Optional space
    # \d{4}       -> Next 4 digits
    # \s?         -> Optional space
    # \d{4}       -> Last 4 digits
    # $           -> End of string

    pattern = r'^[2-9]\d{3}\s?\d{4}\s?\d{4}$'

    if re.match(pattern, aadhaar):
        print("Valid Aadhaar Number")
    else:
        print("Invalid Aadhaar Number")


# ---------------------------------------------------------
# Question 4 : Log File ERROR Analyzer
# ---------------------------------------------------------
def extract_error_logs(log_data):
    """
    This function extracts only ERROR level logs.
    It displays date and message in format:
    YYYY-MM-DD : Message
    """

    # \[ERROR\]            -> Match only ERROR level logs
    # (\d{4}-\d{2}-\d{2})   -> Capture date (YYYY-MM-DD)
    # \s\d{2}:\d{2}:\d{2}   -> Match time (HH:MM:SS)
    # \s-\s                 -> Match separator " - "
    # (.+)                  -> Capture the message

    pattern = r'\[ERROR\]\s(\d{4}-\d{2}-\d{2})\s\d{2}:\d{2}:\d{2}\s-\s(.+)'

    matches = re.findall(pattern, log_data)

    for date, message in matches:
        print(date + " : " + message)


# ---------------------------------------------------------
# Main Program Execution
# ---------------------------------------------------------

print("----- Strong Password Validation -----")
validate_password("Ai@2026Pass")

print("\n----- PAN Number Validation -----")
validate_pan("ABCDE1234F")

print("\n----- Aadhaar Number Validation -----")
validate_aadhaar("2345 6789 1234")

print("\n----- ERROR Log Extraction -----")

log_input = """
[INFO] 2026-01-12 10:15:30 - System started
[ERROR] 2026-01-12 10:16:10 - Database connection failed
[WARNING] 2026-01-12 10:17:45 - Memory usage high
[ERROR] 2026-01-13 09:05:00 - Disk not found
"""

extract_error_logs(log_input)