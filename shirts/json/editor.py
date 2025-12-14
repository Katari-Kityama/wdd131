# By Jett
# Generates a JSON file from user inputs
# I wanted to create this entirely without JSON related outside libaries. I parse everything myself with my own code and my own exceptions.
# It's made completely obsolete by a text editor but this program was only meant to be useful in a vacuum.

# this is the basic structure of a product and these are the corrisponding index values for the variable they are saved in
ID = 0
NAME = 1
PRICE = 2
IMAGEURL = 3
SIZES = 4
COLORS = 5
TAGS = 6
INSTOCK = 7
PRODUCTURL = 8
DESCRIPTION = 9

# selector index values
PRODUCT = 0
TAG = 1
MODE = 2

# -------------------------------------------------------------------------------------------------------------------

def main():
    # main function for calling other functions, UI, and user input
    print()
    print("--------------------------------------------------------------------------------")

    print(" \033[93m --- JSON Editor --- \033[97m")
    print("\033[90mUse this script to generate and edit a JSON file for the shirt selling website. \033[97m")

    init()

def init():
    # gather and process input
    while True:
        print()
        print("\033[36m What is the name of the JSON file? \033[97m")
        file = input(" > ")
        file = file.strip()

        # checks if the file extension is there and throws an exception if not | also checks whether to edit or create a json file and saves it to a variable
        try:
            is_new = parse_file_name_input(file)
            break
        except ValueError as e:
            print(f"\033[91mError:\033[97m {e}")

    # Start editor
    print('type "?h" for help and commands')
    if not is_new:
        try:
            json_dictionary = scan_existing_json(file) # needs tested, will likely break if there is a misnumbered amount of product ID's in the input json
            editor(json_dictionary, file, ["NONE", "NONE", "NONE"])
        except OSError as e:
            print(f"\033[91mError:\033[97m {e}")
        except IndexError as e:
            print(f"\033[91mError:\033[97m {e}")
            print("The JSON file failed to load into memory. Is the formatting very broken?")

    if is_new:
        init_json_template(file)
        json_dictionary = {}
        json_dictionary[0] = product_template()
        editor(json_dictionary, file, ["NONE", "NONE", "NONE"])

# -------------------------------------------------------------------------------------------------------------------
# input and setup

def print_working_json(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")

def parse_file_name_input(file):
    # first we check if the user inputed a .json extention correctly
    if not file.endswith(".json"):
        raise ValueError("Input must must have correct file extension: \".json\"")

    # Now we check whether to edit or create a new JSON file
    try:
        with open(file, "rt"):
            is_new = False
            print("\033[90mFile found - editing existing JSON.\033[97m")

    except:
        is_new = True
        print("\033[90mFile not found - creating new JSON.\033[97m")
    return is_new

def init_json_template(filename):
    with open(filename, "x"): # create file
        print(f"\033[90m{filename} created.\033[97m")

def tag_list_def():
    tag_list = ["id", "name", "price", "imageUrl", "sizes", "colors", "tags", "inStock", "productUrl", "description"]
    return tag_list

def id_list_def():
    id_list = [ID, NAME, PRICE, IMAGEURL, SIZES, COLORS, TAGS, INSTOCK, PRODUCTURL, DESCRIPTION]
    return id_list

def product_template():
    template = ['', '', '', '', '', '', '', '', '', '']
    return template

# -------------------------------------------------------------------------------------------------------------------
# file and text processing functions
# generates a list of line data from the raw json file and then organizes it into a dictionary
def scan_existing_json(filename):
    json_dictionary = {}
    raw_json_list = []
    id_list = id_list_def()
    product_list = []
    clean_product_list = []

    with open(filename, "r") as file: # convert each line into a entry in the raw_json_list
        for line in file:
            raw_json_list.append(line)

    product_id = 0
    for raw_index, each in enumerate(raw_json_list): # ai taught me enumerate (I still wrote this code! it just taught me enumerate can be used to get an index value of a list)
        if "\"id\":" in each:
            product_list = [] # reset helper list
            clean_product_list = [] # reset helper list
            for tag_index in id_list:
                product_list.append(raw_json_list[tag_index + raw_index]) # appends the line for each tag in a product. Does this by adding the index of the found tag plus the index of each tag

            for each in product_list:
                clean_product_list.append(clean_data(each))

            json_dictionary[product_id] = clean_product_list
            product_id = product_id + 1

    return json_dictionary

def clean_num(num_string):
    num_string = ''.join(c for c in num_string if c.isdigit() or c == '.')
    if str(num_string) != "":
        num_string = float(num_string)
        num_string = f"{num_string:.2f}"
    num_string = str(num_string)
    return num_string

def clean_tf(string):
    if str(string) != "":
        string = str(string)
        string = string.lower()
        if string[0] == "t":
            string = "true"
        elif string[0] == "f":
            string = "false"
        else:
            allowed_true = "tru"
            allowed_false = "fals"
            string_true = ''.join(c for c in string if c in allowed_true)
            string_false = ''.join(c for c in string if c in allowed_false)

            if len(string_true) > len(string_false):
                string = "true"
            elif len(string_true) < len(string_false):
                string = "false"
            else:
                string = ""

    return string

# cleans full json input into just the json values
def clean_data(string):
    is_list_string = False

    string = string.strip()

    if "[" in string:
        is_list_string = True
        string = string[string.find("[")+1 : string.find("]")] # https://stackoverflow.com/questions/15043326/getting-string-between-2-characters-in-python
        string = string.translate(str.maketrans('', '', ",\":[]")) # https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

    if not is_list_string:
        string = string.translate(str.maketrans('', '', ",\":[]")) # https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
        string = string[string.find(" ")+1 : len(string)]

    return string

# builds json syntax from the dictionary
def concat_data(json_dictionary):
    tag_list = tag_list_def()
    concatenated_json_dictionary = {}
    concatenated_data = []
    comma = ","
    quote = "\""
    bracket_l = "["
    bracket_r = "]"

    for index, data in json_dictionary.items():
        for i, each in enumerate(data):

            if tag_list[i] == tag_list[2]:
                each = clean_num(each)

            if tag_list[i] == tag_list[7]:
                each = clean_tf(each)

            if tag_list[i] != tag_list[9]:
                comma = ","
            else:
                comma = ""

            if tag_list[i] in [tag_list[2], tag_list[4], tag_list[5], tag_list[6], tag_list[7]]:
                quote = ""
            else:
                quote = "\""

            if tag_list[i] in [tag_list[4], tag_list[5], tag_list[6]]:
                bracket_l = "["
                bracket_r = "]"
                each = parse_list_input(each)
            else:
                bracket_l = ""
                bracket_r = ""

            concatenated_data.append(f'      "{tag_list[i]}": {quote}{bracket_l}{each}{bracket_r}{quote}{comma}') # restores json formatting
        concatenated_json_dictionary[index] = concatenated_data # creates and returns a dictionary with this formatting
        concatenated_data = []

    return concatenated_json_dictionary

# builds a list ready to be saved to a json file
def build_json(json_dictionary):
    build = ['{', '  "products": [']
    end_build = ['    }', '  ]', '}']
    concatenated_json_dictionary = concat_data(json_dictionary)

    for index, data in concatenated_json_dictionary.items():
        build.append("    {")
        for each in data:
            build.append(each)
        build.append("    },")

    build.pop() # https://www.w3schools.com/python/ref_list_pop.asp removes the last list item which is expected to have a comma

    for each in end_build:
        build.append(each)

    return build

def clean_print_dictionary(json_dictionary, product_index):
    tag_list = tag_list_def()
    data = json_dictionary[product_index]
    print_formatted_json = []
    quote = "\""
    bracket_l = "["
    bracket_r = "]"
    color = "\033[95m"

    for i, data in enumerate(data):
        if tag_list[i] == tag_list[2]:
            data = clean_num(data)

        if tag_list[i] == tag_list[7]:
            data = clean_tf(data)

        if tag_list[i] in [tag_list[2], tag_list[4], tag_list[5], tag_list[6], tag_list[7]]:
            quote = ""
        else:
            quote = "\""

        if tag_list[i] in [tag_list[4], tag_list[5], tag_list[6]]:
            bracket_l = "["
            bracket_r = "]"
            data = parse_list_input(data)
        else:
            bracket_l = ""
            bracket_r = ""

        if tag_list[i] in [tag_list[2], tag_list[7]]:
            color = "\033[95m"
        else:
            color = ""

        print_formatted_json.append(f"\033[36m{tag_list[i]}\033[97m: {bracket_l}\033[32m{quote}\033[92m{color}{data}\033[32m{quote}\033[97m{bracket_r}\033[97m")

    return print_formatted_json

def check_selection(selection):
    if not selection[TAG] == "NONE" and selection[PRODUCT] == "NONE":
        selection[TAG] = "NONE"
        print("\033[90mProduct and tag deselected.\033[97m")

def parse_list_input(user_input):
    user_input = clean_data(user_input)
    split_input = user_input.split(" ")
    user_input = ""
    for each in split_input:
        user_input = user_input + f'"{each}", '
    user_input = user_input[:-2]
    return user_input

# -------------------------------------------------------------------------------------------------------------------
# editor functions and editor commands
def editor(json_dictionary, filename, selection):
    selected_list = []

    while True:
        user_input, selection = parse_input(json_dictionary, filename, selection)
        check_selection(selection)

        if selection[TAG] != "NONE":
            if selection[TAG] in [4,5,6]:
               user_input = parse_list_input(user_input)
            selected_list = json_dictionary[selection[PRODUCT]]
            selected_list[selection[TAG]] = user_input
            json_dictionary[selection[PRODUCT]] = selected_list
            if selection[MODE] == "ALL":
                selection[TAG] = selection[TAG] + 1

        if selection[MODE] == "ALL-INIT":
            selection[TAG] = 0
            selection[MODE] = "ALL"
        if selection[TAG] == 10:
            selection[TAG] = "NONE"

def gather_input(json_dictionary, filename, selection):
    tag_list = tag_list_def()
    product = selection[PRODUCT]
    tag = selection[TAG]
    if selection[PRODUCT] == "NONE":
        product = "\033[90mproduct\033[97m"
    else:
        for index, data in json_dictionary.items():
            if index == product:
                product = data[0]
    if selection[TAG] == "NONE":
        tag = "\033[90mtag\033[97m"
    else:
        tag = tag_list[int(selection[TAG])]
    user_input = input(f"[\033[33m{filename}\033[97m] [\033[93m{product}\033[97m | \033[36m{tag}\033[97m] > ")

    return user_input

def parse_input(json_dictionary, filename, selection):
    while True:
        check_selection(selection)
        user_input = gather_input(json_dictionary, filename, selection)
        user_input = user_input.translate(str.maketrans('', '', ",\""))
        lower_input = user_input.lower()
        lower_input = lower_input.strip()

        if lower_input in ["?help", "?h"]:
            h()

        elif lower_input == "?p":
            """print all products in memory"""
            p(json_dictionary)

        elif lower_input == "?pf":
            """full print all products in memory"""
            pf(json_dictionary)

        elif lower_input == "?pi":
            """print current product being edited"""
            pi(json_dictionary)

        elif lower_input == "?pb":
            """print built file"""
            pb(json_dictionary)

        elif lower_input == "?pw":
            """print written file"""
            print_working_json(filename)

        elif lower_input == "?s":
            """write working json to file"""
            s(json_dictionary, filename)

        elif lower_input == "?q":
            """quit without saving"""
            print("\033[90mDiscarding configuration...\033[97m")
            q()

        elif lower_input == "?wq":
            """write and quit editor"""
            wq(json_dictionary, filename)

        elif lower_input == "?r":
            json_dictionary = scan_existing_json(filename)


        elif lower_input == "?rf":
            init()

        elif "?e" in lower_input:
            """select a product to edit"""
            if lower_input == "?e" and selection[PRODUCT] != "NONE":
                selection[PRODUCT] = "NONE"
            else:
                try:
                    if check_arguments(lower_input):
                        e(user_input, json_dictionary, selection)
                except ValueError as error:
                    print(f"\033[91mError:\033[97m {error}")

        elif "?t" in lower_input:
            if lower_input == "?t":
                selection[MODE] = "ALL-INIT"
                break
            else:
                try:
                    if check_arguments(lower_input):
                        t(user_input, selection)
                except ValueError as error:
                    print(f"\033[91mError:\033[97m {error}")

        elif lower_input == "?pj":
            print(json_dictionary)

        elif "?" in lower_input:
            print(f'\033[91mInvalid Command\033[97m: "{user_input}"')

        else:
            break

    return user_input, selection

def h():
    print("Use ?e and ?t to edit a product and a tag.")
    print()
    print("Commands:")
    print("?h  : print commands")
    print("?p  : print all products in memory")
    print("?pf : full print all products in memory")
    print("?pi : print current product being edited")
    print("?pb : print built file")
    print("?pw : print written file")
    print("?s  : write working json to file")
    print("?q  : quit without saving")
    print("?wq : write to json and quit editor")
    print("?r  : discard changes and reload file into editor")
    print("?rf : discard changes and reload new file into editor")
    print()
    print("?e           : Deselect product and tag")
    print("?e {product} : select a product to edit")
    print("?e {n}       : deselect current produc")
    print("?e {c}       : create a product")
    print("?e {d}       : deletes selected product")
    print()
    print("?t       : edit all tags one by one for a selected product")
    print("?t {tag} : edit specific tag")
    print()
    print('["filename"] ["selected product" | "selected tag"] > "value" or "list value 1" "list value 2"...')
    print()

def p(json_dictionary):
    """print all products in memory"""
    for index, data in json_dictionary.items():
        print(f"\033[93m{data[0]}\033[97m ", end="") # chatGPT taught me "end="""
    print()

def pf(json_dictionary):
    """full print all products in memory"""
    print()
    for index, data in json_dictionary.items():
        print_formatted_json = clean_print_dictionary(json_dictionary, index)
        for each in print_formatted_json:
            print(each)
        print()

def pi(json_dictionary, selection):
    """print current product being edited"""
    if selection[PRODUCT] != "NONE":
        print()
        print_formatted_json = clean_print_dictionary(json_dictionary, selection[PRODUCT])
        """0 IS A PLACEHOLDER AND NEEDS FIXED"""
        for each in print_formatted_json:
            print(each)
        print()
    else:
        print("\033[90mNo product selected. See products with ?p and select one with ?e {product}.\033[97m")

def pb(json_dictionary):
    """print written file"""
    build = build_json(json_dictionary)
    for each in build:
        print(each)

def s(json_dictionary, filename):
    build = build_json(json_dictionary)
    with open(filename, "w") as file:
        for each in build:
            file.write(each + "\n")
    print(f"\033[90mConfiguration written to {filename}.\033[97m")

def q():
    """quit editor"""
    print("\033[90mExiting program...\033[97m")
    raise SystemExit # https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used

def wq(json_dictionary, filename):
    """write and quit editor"""
    s(json_dictionary, filename)
    q()

def e(user_input, json_dictionary, selection):
    """handles product selection, creation, and deletion"""
    helper_dictionary = {}

    user_input = user_input.strip()
    user_input = user_input.split(" ")
    user_input = user_input[1]
    argument = user_input

    if argument == "n": # different command options run different functions
        selection[PRODUCT] = "NONE" # reset product selection
    else:
        product_names = []
        product_ids = []
        for index, data in json_dictionary.items(): # generate lists to compare the argument
            product_names.append(data[0])
            product_ids.append(str(index))

        if argument == "c":
            """create product"""
            json_dictionary[len(json_dictionary)] = product_template()
        elif argument == "d":
            """delete product"""
            try:
                del json_dictionary[selection[PRODUCT]] # https://stackoverflow.com/questions/9754729/remove-object-from-a-list-of-objects-in-python
            except KeyError as e:
                print(f"\033[91mError:\033[97m {e}")
                print("Is a product selected?")

            print("silly")

            for index, (key, item) in enumerate(json_dictionary.items()): # normalize index
                helper_dictionary[index] = item
            json_dictionary = helper_dictionary
            selection[PRODUCT] = "NONE"  # reset product selection

        else:
            if user_input not in product_names and user_input not in product_ids: # check if the input is actually in the dictionary
                print("select product in:", product_names, "or", product_ids)
                raise ValueError("ID/name of product not found. Input an existing number or name.")

            for i, each in enumerate(product_names): # normalize input and then process it depending on the argument
                if user_input == each:
                    user_input = i
                for each in product_ids:
                    if str(user_input) == each:
                        user_input = int(user_input)
                        selection[PRODUCT] = user_input

def t(user_input, selection):
    """handles tag edit | no argument behavior is to iterate through all tags one by one"""
    tag_list = tag_list_def()
    id_list = id_list_def()
    user_input = user_input.strip()
    user_input = user_input.split(" ")
    user_input = user_input[1]
    selection[MODE] = "SINGLE"

    if user_input == "n":
        selection[TAG] = "NONE"
    else:
        if user_input not in tag_list and user_input not in str(id_list): # check if the input is actually in the dictionary
            print("select tag in:", tag_list, "or:", id_list)
            raise ValueError("Invalid tag!")

        if user_input in tag_list:
            for i, each in enumerate(tag_list): # normalize with id_list
                if user_input == each:
                    user_input = i
        else:
            user_input = int(user_input)

        selection[TAG] = user_input

def check_arguments(user_input):
    split_input = user_input.split(" ")
    if len(split_input) == 2:
        return True
    else:
        print(f'\033[91mInvalid Command\033[97m: "{user_input}" has {len(split_input) - 1} arguments when 1 was expected!')
        return False

# -------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# todo:
# / doesn't work in inputs when it needs to
# fix comments

# Unused Code
"""
# comments here include where I learned how to use these libaries
import platform # https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on
import threading # https://docs.python.org/3/library/threading.html, https://www.stratascratch.com/blog/python-threading-like-a-pro/
import keyboard # https://github.com/boppreh/keyboard?tab=readme-ov-file#keyboard.on_press
"""

"""
os = platform.system()
if not os == "Darwin": # macOS doesn't support the keyboard libary so this feature is linux / windows only
    print("\033[90mPress the opening curly brace anytime to view the saved JSON file configuration (\"{\"). \033[97m")
    t = threading.Thread(target=key_listener, args=(file)) # https://docs.python.org/3/library/threading.html, https://www.stratascratch.com/blog/python-threading-like-a-pro/
    t.start() # creates a thread for the "{" listener to operate seperately from the rest of the code
"""

"""
def key_listener(filename):
    while True:
        if keyboard.is_pressed("shift+[") or keyboard.is_pressed("["):
            print_working_json(filename)
"""