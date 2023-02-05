from cjklib.characterlookup import CharacterLookup

chars = ['土', '心', '手']
char_lookup = CharacterLookup('C')


def get_stroke_count(char):
    stroke_count = char_lookup.getStrokeCount(char)
    return stroke_count


def main():
    stroke_count_dict = {char: get_stroke_count(char) for char in chars}
    print(stroke_count_dict)


if __name__ == "__main__":
    main()
