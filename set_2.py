'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    letter = str(letter.upper())
    shift = int(shift)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #indexes the letters
    for i, letter_place in enumerate(alphabet):
        if letter_place == letter:
            shifted = alphabet[(i + shift) % len(alphabet)]
            break
        elif letter == " ":
            shifted = letter

    return (str(shifted))

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = str((message.upper()))
    shift = int(shift)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new_message = ""
    for letter in message: #Separates the letters and creates a variable 'letter'
        if letter == " ":  # keep spaces
            new_message += " "
            continue
        for i, letter_place in enumerate(alphabet): #then it will begin indexing the alphabet 
            if letter_place == letter: #then match it with each letter
                shifted_letter = alphabet[(i + shift) % len(alphabet)] #then shift it accordingly
                new_message = new_message + shifted_letter

    return(str(new_message))
    

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    letter = str(letter.upper())
    letter_shift = str(letter_shift.upper())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i1, letter_place1 in enumerate(alphabet):
        if letter_place1 == letter:
           for i2, letter_place2 in enumerate(alphabet):   #looking for the place of the second letter
                if letter_place2 == letter_shift:
                     shifted = alphabet[(i2 + i1) % len(alphabet)]                   
                     break
        elif letter == " ":
            shifted = letter

    return (str(shifted))

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the key is extended to match the length of the message.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = str(message.upper())
    key = str(key.upper())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Build new key regardless if it shorter or longer. More importantly it takes spaces into account
    new_key = ""
    k = 0 #k is the position of the character on the 'key' string, beginning with zero
    while len(new_key) < len(message):
        new_key = new_key + key[k % len(key)]  
        k = k + 1 #by adding +1 it will move to the right and cycle back to complete a new key

    # Encrypting into a cypher
    #1. Separate the messasge and the key into letters
    #2. Then create an index and perform a function similar to Caesar and Shift by a letter
    #3. That loops afterwards, similar to Caesar in order to build a new message
    cipher = ""
    i = 0       
    while i < len(message):
        message_L = message[i]
        key_L = new_key[i]

        if message_L == " ": #To keep the space in the final message
            cipher = cipher + " "   
            i = i + 1
            continue

        # find positions 
        i1 = 0
        for t, a in enumerate(alphabet):
            if a == message_L:
                i1 = t
                break

        i2 = 0
        for t, a in enumerate(alphabet):
            if a == key_L:
                i2 = t
                break

        cipher = cipher + alphabet[(i1 + i2) % len(alphabet)]
        i = i + 1

    return str(cipher)

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.   
    message = str(message.upper())
    shift = int(shift)

 # Step 1: Should be divisible by shift to be a multiple
 # Step 2: Loop adding underscore if the length is not a multiple of shift
    while len(message) % shift != 0:
        message += "_"

    # Step 3: Encode 
    scytale = ""
    for i in range(len(message)): # How it works is this indexes the column and adjusts accordingly with the row, js using the function given
        # For each index i in the encoded message, use the character at the index
        index = (i // shift) + (len(message) // shift)  * (i % shift)
        scytale += message[index] #The function in the end gives the message

    return str(scytale)

def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = str(message.upper())
    shift = int(shift)
    rows = len(message) // shift 

    og_MERC = ""
    for i in range(len(message)):
        # For each index i in the encoded message, use the character at the index
        index = (i // rows) + shift * (i % rows)
        og_MERC += message[index] #The function in the end gives the message

    return str(og_MERC)