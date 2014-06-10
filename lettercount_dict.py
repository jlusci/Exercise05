from sys import argv

script, input_file = argv

def main():
    letter_count = {}
    myfile = open(input_file)
    content = myfile.read()
    content = content.lower()

    for character in content:
        if character.isalpha():
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1

    for item in sorted(letter_count.iteritems()):
        print item[1]#, item[1]



if __name__ == "__main__":
    main()