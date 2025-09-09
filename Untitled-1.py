def scytale_cipher(message, shift):
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
    message = str(message.upper())
    shift = int(shift)

    og_MERC = " "
    for i in range(len(message)): # How it works is this indexes the column and adjusts accordingly with the row, js using the function given
        # For each index i in the encoded message, use the character at the index
        index = (i // shift) + (len(message) // shift) / (i % shift)
        scytale += message[index] #The function in the end gives the message

    return str(scytale)
