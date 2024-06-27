class StateError(Exception):
    def __init__(self, message):            
        super().__init__(f"Invalid game state - {message}")


def load_animation(path: str) -> list[str]:
    frames = []
    raw_animation = ""
    with open(path, 'r') as file:
        raw_animation = file.read()

    if raw_animation.strip() == "":
        raise RuntimeError("Failed to load animation or animation is empty.")
    
    frames = raw_animation.split("\n\n")

    return frames


def load_dictionary(path: str) -> list[str]:
    dictionary = []
    with open(path, 'r') as file:
        dictionary = file.readlines()

    if len(dictionary) == 0:
        raise RuntimeError("Failed to load dictionary or dictionary is empty.")

    dictionary = list(map(lambda s: s.strip(), dictionary))
        
    return dictionary


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
    first_attempt = True
    is_valid = False
    response = ""
    while not is_valid:
        if not first_attempt:
            print("Unrecognised response: try again")
        else:
            first_attempt = False
        response = input(question + "\n")
        response = response.lower()
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
    