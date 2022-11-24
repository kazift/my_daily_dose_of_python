def random_word_generator():
    import random
    words_list = ["Python", "Java", "Django", "Ubuntu", "KUbuntu", "Windows", "QWERTY",
                  "Alpha", "Beta", "Gamma", "Toyota", "Banana", "Ergonomics", "Amazon",
                  "India", "Charlie", "Delta", "Echo", "Jupiter", "Neptune", "Uranus"]
    selected_word = random.choice(words_list)
    # print(selected_word)
    return selected_word


def dash_printer(selected_word):
    length_of_selected_word = len(selected_word)
    dash_printing_worker = ""
    for i in range(0, length_of_selected_word):
        dash_printing_worker += " _ "
    return dash_printing_worker



generated_word = random_word_generator()
dashes_generated = dash_printer(generated_word)
print(f'Welcome to the Guessing Game!!\nYou Have to guess:{dashes_generated}')
