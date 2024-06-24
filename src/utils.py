def yn_input(question: str) -> bool:
    '''
    Function that waits for input. Additionally waits for a valid yes or no answer.
    Prints a given string if passed as argument.
    Valid responses are: y, n, yes, no - case insensitive\n
    Returns a boolean:
        yes -> true\n
        no -> false\n

    Based on default input() function.
    '''
    InputError = ValueError("Input response contains an inappropriate response. \
                         This should not occur. Report to the developer.")

    valid_responses = ['y', 'n', 'yes', 'no']
    first_attempt = False
    is_valid = False
    response = ""
    while not is_valid:
        if not first_attempt:
            print("Unrecognised response: try again")
        response = input(question + "\n")
        response.lower()
        if response in valid_responses:
            break
    
    if response.strip() == "":
        raise InputError
    
    if response == 'y' or response == 'yes':
        return True
    elif response == 'n' or response == 'no':
        return False
    else:
        raise InputError