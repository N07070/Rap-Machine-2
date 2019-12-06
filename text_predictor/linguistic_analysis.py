import matplotlib
import pronouncing
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import random


#!/usr/bin/env python
# -*- coding: utf-8 -*-

NBR_ITER = 10000


# Args
if len(sys.argv) != 2:
    print("Please select a dataset.")
    print("Usage: python text_predictor.py <dataset>")
    print("Available datasets: kanye, shakespeare, wikipedia, reuters, hackernews, war_and_peace, sherlock")
    exit(1)
else:
    dataset = sys.argv[1]


# I/O
data_dir = "./data/" + dataset
input_file = data_dir + "/input.txt"
output_file = data_dir + "/output.txt"
output = open(output_file, "a") # Create the file if not exist
output.close()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_sample_of_text(file):
    if not file:
        print("No file found.")
        sys.exit(0)
    with open(file, "r") as f :
    #     list_from_text = list(f)
    #     number_of_lines_to_read = int(file_len(file) * 0.3) # We take 30% of the text
    #     while number_of_lines_to_read > 0:
    #         sample += random.choice(list_from_text)
    #         number_of_lines_to_read -= 1
    # return str(sample)
        sample = random.choice(list(f))
        while sample is None or sample is "":
            sample = random.choice(list(f))
    return str(sample).rstrip()

def get_linguistic_analysis(original, generated):
    data = {
        "nbr_sylable_gen" : 0,
        "nbr_sylable_origin" : 0,
        "line_length_gen" : 0,
        "line_length_ori" : 0,
        "similarity_produced_verse" : 0
    }

    # print(original)
    # print(generated)
    # # Number of syllabes
    # phones = [pronouncing.phones_for_word(p) for p in original.split()]
    # data["nbr_sylable_text_origin"] = sum([pronouncing.syllable_count(p) for p in phones])
    #
    # phones = [pronouncing.phones_for_word(p) for p in generated.split()]
    # data["nbr_sylable_text_gen"] = sum([pronouncing.syllable_count(p) for p in phones])

    # Average Line length
    ll = 0
    nbr_line = 0
    for line in original.split("\n"):
        ll += len(line)
        nbr_line += 1
    data["line_length_ori"] = ll / nbr_line

    ll = 0
    nbr_line = 0
    for line in generated.split("\n"):
        ll += len(line)
        nbr_line += 1
    data["line_length_gen"] = ll / nbr_line

    # Rhyme density

    return data


def analysis_of_generation():
    analysis = get_linguistic_analysis(get_sample_of_text(input_file), get_sample_of_text(output_file))
    # print("\n---------------\n")
    # for x, y in analysis.items():
    #     print(str(x) + " : " + str(y))
    # print("\n---------------\n")
    with open(data_dir + "/analysis.txt", mode = "a", encoding = 'utf-8') as analysis_file:
        analysis_file.write(str(analysis))
        analysis_file.write("\n")
    return analysis


def plot(data, x_label, y_label, title):
    plt.plot(range(len(data)), data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(data_dir + "/" + y_label + ".png", bbox_inches="tight")
    plt.close()


def main():
    d = analysis_of_generation()
    for i in range(0,NBR_ITER):
        tmp = analysis_of_generation()
        for x, y in tmp.items():
            d[x] = (d[x] + tmp[x]) / 2

    print("Number of iterations of the analysis : " + str(NBR_ITER))
    print("-------------------------------------------------")
    for x, y in d.items():
        print(str(x) + " : " + str(y))

if __name__ == '__main__':
    main()
