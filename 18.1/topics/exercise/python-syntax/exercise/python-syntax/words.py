def print_upper_words(words, must_start_with ):
    """
    Converts the words in an array to uppercase and prints each one in a line
    Only the words started with a letter (case insensitive) defined on must_start_with will be printed
    :param words:
    :return:
    """
    lower_must_start_with = [c.lower() for c in must_start_with]
    for w in words:
        if w[0].lower() in lower_must_start_with:
            print(w.upper())


print_upper_words(["eventually", "fried", "Chicken", "with", "corn bake", "is", "GOOD", "end of comment"],
                  must_start_with={"e", "f"})
