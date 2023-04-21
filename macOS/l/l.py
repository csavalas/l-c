import glob
from colorama import Fore, Back, Style
from math import floor
import json
import os, sys
import pyperclip

# Store amount of columns in terminal
width = os.get_terminal_size()[0]
# TO disable abbreviation of long names, simply set this value to width
width_max = int(min(width, 60))
# Fetch directory listing from current dir or CLA passed in
path = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]


def quit(error="No results found."):
    print(error)
    exit()

# Utility function to return the prefix/suffix of a given entry
def get_prefix(i):
    return f'{i}. '
def get_suffix():
    return ' '
# Placed in the middle of abbreviated filenames
dots = '...'


# If a wildcard is in the path, then use glob for directory listing
if '*' in path:
    items = sorted(glob.glob(path))
    if not items:
        quit()
# Otherwise, use listdir
else:
    try:
        items = sorted(os.listdir(path))
    except (FileNotFoundError, PermissionError) as error:
        quit(error=error)

print(f"\n{Back.WHITE}{Fore.BLUE}Directory listing for: {os.path.abspath(path)}{Style.RESET_ALL}\n")


# Separate into lists depending on dir, file, special (for sorting)
types = {
    'dirs': [],
    'files': [],    
    'special': [],
}

for item in items:    
    # If wildcard is not in the path, append the path for directory checking
    if '*' not in path:
        check = os.path.join(path, item)
    else:
        check = item
    if os.path.isdir(check):
        types['dirs'].append(item)
    elif os.path.isfile(check):
        types['files'].append(item)
    else:
        types['special'].append(item)
# Place into a list with dirs 1st, files, then special / respectively alpha sorted
files = types['dirs'] + types['files'] + types['special']

# Make a copy of files to retain all unabbreviated names
files_backend = files.copy()

# For better UI, the path needs to be removed when using glob, doesn't affect backend
if '*' in path:
    for i, file in enumerate(files):
        filename = os.path.basename(file)
        files[i] = filename if filename else os.path.basename(os.path.normpath(file))


# Determine if a file + pre/suffix is > width_max, if so, abbreviate it
for i, file in enumerate(files):
    prefix, suffix = get_prefix(i), get_suffix()
    overage = len(f'{prefix}{file}{suffix}') - width_max
    if overage > 0:
        # Abbreviate filename and place dots in the middle to convey so
        overage += len(dots)
        del_index = int(len(file) / 2 - overage / 2)
        files[i] = files[i][:del_index] + dots + files[i][del_index + overage:]


lines = [[]]
cols = [0]

while True:
    line = 0
    for i, file in enumerate(files):
        prefix, suffix = get_prefix(i), get_suffix()
        file_formatted = f'{prefix}{file}{suffix}'.ljust(cols[-1], ' ')
        lines[line].append(file_formatted)
        if len(''.join(lines[line])) - 1 > width:
            min_length = max(len(lines) , floor(len(files) / (len(lines[line]) - 1)))
            lines = [[] for _ in range(min_length + 1)]
            break

        restart = False

        if cols[-1] < len(file_formatted):
            for l in lines:
                if restart:
                    break
                for j in range(len(l)):
                    l[j] = l[j].ljust(len(file_formatted), ' ')
                if len(''.join(l)) - 1 > width:
                    restart = True
                    break
                else:
                    cols[-1] = len(file_formatted)

        if restart:
            break
        line = (line + 1) % len(lines)
    else:
        break


# Remove trailing space from each filename on the end of its line
for line in lines:
    if line:
        line[-1] = line[-1][:-1]
# Display every filename line by line
for i, line in enumerate(lines):
    if line:
        for j, file in enumerate(line):
            # Calculate true index of file/dir in question
            true_index = len(lines) * j + i
            # Default color, for special types
            color = Fore.YELLOW
            # If the item's true index is < the amount of dirs (which come 1st)... 
            if true_index < len(types['dirs']):
                # then it's a dir, style it accordingly
                color = Fore.GREEN
            # If the item's true index is < the amount of dirs + files...                 
            elif true_index < len(types['dirs'] + types['files']):
                # then it's a file, style it accordingly            
                color = Fore.CYAN
            print(f'{color}{file}{Style.RESET_ALL}', end='')
        # Print newline char after each line of filenames
        print()

# Store the unmodified filenames into a json file for use by the sister 'c' script
files_json = json.dumps(files_backend, indent=4)
with open(os.path.join(os.path.dirname(__file__), "l.json"), "w") as outfile:
    outfile.write(files_json)

# Loop until a blank or a valid response
while True:
    # User can select a filename by its index
    index = input(f'\n{Back.WHITE}{Fore.BLUE}Choice:{Style.RESET_ALL} ')
    # None selected, exit
    if not index:
        exit()
    # Ensure input is a valid number
    try:
        index = int(index) 
    except ValueError:
        print(f"{Back.WHITE}{Fore.RED}Choice must be a number{Style.RESET_ALL}")
        continue
    # Ensure input is within range, if so, copy the corresponding filename to the clipboard
    try:
        copy_text = files_backend[index]
        # Only copy full path to clipboard if user requested a dir listing outside of current dir
        if len(sys.argv) == 2 and ((os.sep in path and '*' not in path) or os.path.isdir(path)):
            copy_text = os.path.join(os.path.abspath(path), copy_text) 
        pyperclip.copy(f"'{copy_text}'")
        print(f"'{Fore.YELLOW}{copy_text}{Style.RESET_ALL}' copied to clipboard!")
        exit()
    except IndexError:
        print(f"{Fore.RED}Choice must be in range{Style.RESET_ALL}")