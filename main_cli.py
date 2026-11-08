import random, time

from storage import load_data, save_data

data = load_data()

existing_strings = data["existing_strings"]
blocked_strings = data["blocked_strings"]

words = []

with open('eff_large_wordlist.txt') as f:
    for line in f:
        word = line.split("\t")[1].strip()
        words.append(word)

def generate_random_string(existing_strings, blocked_strings, words):
    reserved_strings = existing_strings + blocked_strings
    random.seed(time.time_ns())

    while True:
        candidate = f"{random.choice(words)}-{random.choice(words)}-{random.choice(words)}"

        if candidate not in reserved_strings:
            print(candidate)
            return candidate


def new_unique_string():
    """Generate a string, record it in assets.json, and return it."""
    data = load_data()
    new_string = generate_random_string(data["existing_strings"], data["blocked_strings"], words)
    data["existing_strings"].append(new_string)
    save_data(data)
    return new_string

def main():
    new_string = generate_random_string(existing_strings, blocked_strings, words)

    existing_strings.append(new_string)

    data["existing_strings"] = existing_strings
    asset_name = input("Enter asset name: ")
    while True:
        asset_description = input("Enter asset description: ")
        if len(asset_description.split()) >=10:
            break
        print("asset description needs to be min 10 words")


    data["assets"][new_string] = {
          "asset_name": asset_name,
          "asset_description": asset_description,
          "custom_fields": {},
      }

    while True:
        new_row = input("add field (key:value) or enter 'no' to continue")
        if new_row == "no":
            break
        value = input(f'value {new_row}')
        data['assets'][new_string]['custom_fields'][new_row] = value

    save_data(data)

if __name__ == '__main__':
    main()