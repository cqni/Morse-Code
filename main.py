# Morse Code Translator

import requests
import json

dictionary_url = "https://raw.githubusercontent.com/cqni/Morse-Translator/main/morse-dictionary.json"

def get_dictionary(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error trying to get dictionary: {e}")


def translate_to_morse(user_input, dictionary):
    translated_text = []

    for char in user_input:
        if char in dictionary:
            translated_text.append(dictionary[char])
        else:
            translated_text.append('?')

    return " ".join(translated_text)


def main():
    try:
        dictionary = get_dictionary(dictionary_url)
        if not dictionary:
            raise Exception("Dictionary is empty.")

        user_input = input("What do you want to translate?: ").lower().replace(" ", "")
        translated_text = translate_to_morse(user_input, dictionary)

        print(f"Your translated text is: {translated_text}")

    except Exception as err:
        print(f"Exception: {err}")


if __name__ == "__main__":
    main()
