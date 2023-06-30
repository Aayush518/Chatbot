import csv

input_file = "dialogs.txt"
output_file = "conversation_pairs.csv"

pairs = []

with open(input_file, "r") as file:
    lines = file.readlines()

    for i in range(0, len(lines), 2):
        if i+1 < len(lines):
            question = lines[i].strip()
            answer = lines[i+1].strip()
            pair = [question, answer]
            pairs.append(pair)

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(pairs)

print("Conversion complete. Pairs are saved in 'conversation_pairs.csv'.")
