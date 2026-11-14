
import string


def analyze_text(text):

    if text.strip() == "":
        print("\nNo text to analyse.")
        return

    total_characters = len(text)

    text = text.lower()

    words = text.split()

    clean_words = []

    for word in words:
        word = word.strip(string.punctuation)

        if word:
            clean_words.append(word)

    total_words = len(clean_words)

    total_sentences = 0

    for char in text:
        if char == "." or char == "!" or char == "?":
            total_sentences += 1

    if total_sentences == 0 and total_words > 0:
        total_sentences = 1

    unique_words = set(clean_words)

    total_unique_words = len(unique_words)

    word_frequency = {}

    for word in clean_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    sorted_words = sorted(
        word_frequency.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\n========== ANALYSIS REPORT ==========")

    print("Total Words:", total_words)
    print("Total Characters:", total_characters)
    print("Total Sentences:", total_sentences)
    print("Unique Words:", total_unique_words)

    print("\nWord Frequency:")

    for word, count in sorted_words:
        print(word, ":", count)

    print("\nTop Words:")

    for word, count in sorted_words[:2]:
        print(word, ":", count)

    print("\nUnique Words List:")

    for word in sorted(unique_words):
        print(word)

    print("\n=====================================")


def main():

    print("===================================")
    print("     WORD COUNTER AND ANALYZER")
    print("===================================")

    print("\n1. Enter Text")
    print("2. Read Text From File")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        text = input("\nEnter your paragraph: ")
        analyze_text(text)

    elif choice == "2":

        filename = input("\nEnter file name: ")

        try:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()

            analyze_text(text)

        except FileNotFoundError:
            print("File '" + filename + "' not found.")

        except PermissionError:
            print("Permission denied.")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
