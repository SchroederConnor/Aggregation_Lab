import subprocess
import sys
import re
import os
import difflib

# -----------------------------
# Remove comments + clean code
# -----------------------------
def remove_comments(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text


def print_result(test_name, passed):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")


# -----------------------
# File Checks
# -----------------------

REQUIRED_FILES = [
        "restaurant.h",
        "restaurant.cpp",
        "menuItem.h",
        "menuItem.cpp",
        "main.cpp",
        "Output.txt"
    ]
EXEC = "./restaurant"
# -----------------------------
# Check required files
# -----------------------------
def check_files():
    print("Checking required files...")
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:", ", ".join(missing))
        return False
    return True


# -----------------------------
# Check header file
# -----------------------------
def check_header():
    print("Checking restaurant.h...")
    with open("restaurant.h") as f:
        header = remove_comments(f.read())

    checks = [
        (r"string\s+name\s*;", "string name"),
        (r"#define\s+SIZE\s+3", "#define SIZE 3"),
        (r"class\s+Restaurant", "class Restaurant"),
        (r"int\s+numItem\s*;", "int numItem"),
        (r"Restaurant\s*\(\s*\)", "default constructor"),
        (r"Restaurant\s*\(", "parameterized constructor"),
        (r"Restaurant\s*\(\s*const\s+Restaurant\s*&", "copy constructor Restaurant(const Restaurant&)"),
        (r"MenuItem\s+items\s*\[\s*SIZE\s*\]", "MenuItem items[SIZE]"),
        (r"setName", "setName"),
        (r"getName", "getName"),
    
        (r"getNumItem", "getNumItem"),
        (r"addItem", "addItem"),
        (r"getItems", "getItems"),
        (r"displayRestaurantData", "displayRestaurantData"),


    ]

    checks2 = [
        
        (r"setNumItem", "setNumItem"),
    
    ]

    for regex, label in checks:
        if not re.search(regex, header):
            print("Missing:", label)
            return False
    
    for regex, label in checks2:
        
        if  re.search(regex, header):
            print("There should not be any setNumItem method declaration")
            return False
    
    return True



    # print("restaurant.h check passed")


# -----------------------------
# Check cpp file
# -----------------------------
def check_cpp():
    print("Checking restaurant.cpp...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments(f.read())

    checks = [
        (r"Restaurant::Restaurant\s*\(\s*\)", "default constructor"),
        (r"Restaurant::Restaurant\s*\(", "parameterized constructor"),
        (r"Restaurant\s*\(\s*const\s+Restaurant\s*&", "copy constructor Restaurant(const Restaurant&)")

    ]
    for regex, label in checks:
        if not re.search(regex, cpp):
            print("Missing:", label)
            return False
    
    checks2 = [
        
        (r"setNumItem", "setNumItem"),
    
    ]

    for regex, label in checks2:
        if  re.search(regex, cpp):
            print("There should not be any setNumItem method implementation")
            return False

    required = [
    
        r"Restaurant::setName",
        r"Restaurant::getName",
        r"Restaurant::getNumItem",
        r"Restaurant::addItem",
        r"Restaurant::getItems",
        r"Restaurant::displayRestaurantData"
    ]

    for item in required:
        if not re.search(item, cpp):
            print(f"restaurant.cpp missing implementation: {item}")
            return False 
    return True

    # print("restaurant.cpp check passed")


# -----------------------
# addItem capacity check
# -----------------------
def addItem_check():
    print("Checking addItem method...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments(f.read())
    if "Limit exceeded!" not in cpp:
        print("Missing overflow error message in addItem()")
        return False
    return True

# -----------------------------
# Check main file
# -----------------------------
def check_main():
    print("Checking main.cpp...")

    with open("main.cpp", "r") as f:
        content = remove_comments(f.read())

    required = [
        "MenuItem",
        "Restaurant",
        "displayRestaurantData",
        "addItem",
        "[",
        "]"
    ]

    missing = [r for r in required if r not in content]

    if missing:
        print(" main.cpp issues:")
        for m in missing:
            print(" -", m)
        return False
    return True
    


# -----------------------------
# Build project
# -----------------------------
def build():
    print("Building project...")

    result = subprocess.run(["make"], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Build failed:\n")
        print(result.stderr)
        return False 
    return True


# -----------------------------
# Run program
# -----------------------------
def run_program():
    print("Running program...")

    if not os.path.exists(EXEC):
        print(" Executable not found")
        sys.exit(1)

    result = subprocess.run([EXEC], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Program crashed")
        print(result.stderr)
        sys.exit(1)

    print("Program output captured.")
    return result.stdout.strip()


# ---------------------------
# Run make clean
# ---------------------------
def check_make_clean():
    try:
        subprocess.run(
            ["make", "clean"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        obj_files = [f for f in os.listdir(".") if f.endswith(".o")]
        exe_files = os.path.exists(EXEC)
        # if not os.path.exists(EXEC):
            
        #     sys.exit(1)
        print ("Checking make clean...")

        if exe_files:
            print("Executable restaurant is not removed.")
            return False 

        if obj_files:
            print("Not all the .o files are removed.")
            return False

        return True

    except Exception:
        return False


# -----------------------------
# Load expected output
# -----------------------------
def load_expected():
    with open("Output.txt", "r") as f:
        return f.read().strip()


# -----------------------------
# Compare outputs
# -----------------------------
def compare_output():
    print("Comparing output with Output.txt...")

    actual = run_program()
    expected = load_expected()

    if actual == expected:
        print("Output matches exactly!")
        return True
    print("Output does NOT match!\nCheck output.txt")
    
# print(" Output does NOT match!\n")

    diff = difflib.unified_diff(
    expected.splitlines(),
    actual.splitlines(),
    fromfile="Expected (Output.txt)",
    tofile="Actual (Program Output)",
    lineterm=""
    )

    print("Difference Report:")
    print("  --- : Expected output")
    print("  +++ : Your program output")
    print("  -   : Line missing or incorrect in your output")
    print("  +   : Line produced by your program that differs from expected")
    print("      : Lines without a symbol match in both outputs")
    print()

    for line in diff:
        if line.startswith("@@"):
            continue
        print(line)
    return False

# -----------------------------
# Main
# -----------------------------
def main():
    total = 0
    passed = 0

    

    tests = [
        ("Required Files Exist", check_files),
        ("Header Declarations", check_header),
        ("CPP Implementations", check_cpp),
        ("addItem Check",addItem_check),
        ("main.cpp Structure", check_main),
        ("Makefile Builds", build),
        ("Executable Created and Output Matching", compare_output),
        ("Make Clean Works", check_make_clean),
        
        
    ]

    for name, func in tests:
        total += 1
        result = func()
        print_result(name, result)

        if result:
            passed += 1

    if passed == total:
        print("\n======================")
        print("Project Passed")
        print("======================")
        sys.exit(0)
    else:
        print("\n======================")
        print("Project Failed")
        print("======================")
        sys.exit(1)
   


if __name__ == "__main__":
    main()