from test import evaluate_test
tests = [
    {
        "inputs":"ab-cd",
        "outputs":"dc-ba"
    },
    {   "inputs":"a-bc-def=ghij!!",
        "outputs":"j-ih-gfe=dcba!!"
    }
    ]

def pos_of_non_letters(s):
    mydict = {}
    pos = 0
    for char in s:
        pos += 1
        if not(isletter(char)):
            mydict[pos - 1] = char
    return mydict

def isletter(character):
    let = ord(character)
    if ((let >= 65 and let <= 90) or (let >= 97 and let <= 122)):
        return True

def reverse_letters_string(s, mydict):
    new_string = ""
    for char in s:
        if char  not in mydict.values():
            new_string = new_string + char
    return new_string[::-1]

def add_non_letters(reversed_string, mydict):
    positions = mydict.keys()
    new_string = ""
    count = 0
    lengths = len(positions) + len(reversed_string)
    for epoch  in range(lengths):
        if epoch in positions:
            new_string += mydict[epoch]
            count += 1
        elif count < len(reversed_string):
            new_string += reversed_string[epoch - count]
        elif count == len(positions) and epoch >= len(reversed_string):
            newString += reversed_string[epoch - count:]
            break
    return new_string

def reverse_letters_only(string):
    my_dict = pos_of_non_letters(string)
    reversed_string_without_non_letters = reverse_letters_string(string, my_dict)
    #print(f"reversed no nons -> {reversed_string_without_non_letters}")
    reversed_string_with_non_letters = add_non_letters(reversed_string_without_non_letters, my_dict)
    return reversed_string_with_non_letters
    
evaluate_test(reverse_letters_only,tests)
