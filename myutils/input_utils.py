def Tokenizer(userInput: str) -> list[str]:
    """Turns a string with spaces into a list of strings.
    Removes empty words in case of superfluous spaces."""
    assert isinstance(userInput, str), "Tokenizer can only accept a string as input."
    try:
        processed = userInput.split()
        processed = list(filter(None, processed))
        return processed
    except Exception as e:
        raise Exception(f"An unexpected error occurred with the input tokenizer: {e}")
    
def Helper(inputList: list[str]) -> str:
    """Manager for pulling help info.

    If the :list:`inputList` length is 1 (or, one "word"), asks for a particular name of a command or program, then returns the first "word".

    If the length is 2 or longer, the second "word" must be the name of the command or program itself, so it returns that.
    
    Returns nothing if :list:`inputList` has no length."""
    assert isinstance(inputList, list), "Helper can only accept a list of words as input."
    assert all(isinstance(a, str) for a in inputList), "Helper can only accept a list of words as input."
    try:
        match len(inputList):
            case 0:
                return None
            case 1:
                helpInput = input("With what command or program?:\n>>> ").split()
                print()
                return helpInput[0].lower()
            case _:
                return inputList[1].lower()
    except Exception as e:
        raise Exception(f"An unexpected error occurred with the helper util: {e}")