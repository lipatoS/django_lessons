# reads words from the /source/ file that have at least four letters

# TODO: CHANGE FILE PATH
destination = open('path_to_destination', 'w')

with open('path_to_dataset', 'r') as word_file:
    for word in word_file:
        if len(word) >= 5:
            destination.write(word)
    word_file.close()
    destination.close()
