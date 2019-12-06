#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import pronouncing
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import random
import re


NBR_ITER = 10000


# Args
if len(sys.argv) != 2:
    print("Please select a dataset.")
    print("Usage: python text_predictor.py <dataset>")
    print("Available datasets: kanye")
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

def strip_nonalpha_chars(word):
    return re.sub(r'[\[\]\(\)\,]', '', word)


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

def CountSyllables(word, isName=True):
    vowels = "aeiouy"
    #single syllables in words like bread and lead, but split in names like Breanne and Adreann
    specials = ["ia","ea"] if isName else ["ia"]
    specials_except_end = ["ie","ya","es","ed"]  #seperate syllables unless ending the word
    currentWord = word.lower()
    numVowels = 0
    lastWasVowel = False
    last_letter = ""

    for letter in currentWord:
        if letter in vowels:
            #don't count diphthongs unless special cases
            combo = last_letter+letter
            if lastWasVowel and combo not in specials and combo not in specials_except_end:
                lastWasVowel = True
            else:
                numVowels += 1
                lastWasVowel = True
        else:
            lastWasVowel = False

        last_letter = letter

    #remove es & ed which are usually silent
    if len(currentWord) > 2 and currentWord[-2:] in specials_except_end:
        numVowels -= 1

    #remove silent single e, but not ee since it counted it before and we should be correct
    elif len(currentWord) > 2 and currentWord[-1:] == "e" and currentWord[-2:] != "ee":
        numVowels -= 1

    return numVowels

def get_linguistic_analysis(original, generated):
    data = {
        "nbr_sylable_gen" : 0,
        "nbr_sylable_origin" : 0,
        "line_length_gen" : 0,
        "line_length_ori" : 0,
        "uniq_words_gen" : 0,
        "uniq_words_ori" : 0
    }

    # print(original)
    # print(generated)
    # # Number of syllabes
    # phones = [pronouncing.phones_for_word(p) for p in original.split()]
    # print(phones)
    nbr_syl = 0;
    for p in original.split():
        nbr_syl += CountSyllables(p)
    data["nbr_sylable_origin"] = nbr_syl

    # phones = [pronouncing.phones_for_word(p) for p in generated.split()]
    nbr_syl = 0;
    for p in generated.split():
        nbr_syl += CountSyllables(p)
    data["nbr_sylable_gen"] = nbr_syl


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

    # Word map
    # need to sort and cleanup this dict
    # TODO: Make the whole word lowercase (test against Let Me Hold You)
    # words_map = dict()
    # for word in original:
    #     plain_word = strip_nonalpha_chars(word)
    #     if plain_word in words_map:
    #         words_map[plain_word] += 1
    #     else:
    #         words_map[plain_word] = 1
    # data["word_freq_ori"] = words_map
    #
    # words_map = dict()
    # for word in generated:
    #     plain_word = strip_nonalpha_chars(word)
    #     if plain_word in words_map:
    #         words_map[plain_word] += 1
    #     else:
    #         words_map[plain_word] = 1
    # data["word_freq_gen"] = words_map


    # Unique words
    data["uniq_words_gen"] = len(set(generated.split(" ")))
    data["uniq_words_ori"] = len(set(original.split(" ")))

    # Verse similarity

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
    plt.savefig(data_dir + "/" + title + ".png", bbox_inches="tight")
    plt.close()


def main():
    d = analysis_of_generation()
    for i in range(0,NBR_ITER):
        tmp = analysis_of_generation()
        for x, y in tmp.items():
            if type(d[x]) is set or type(y) is set:
                d[x] = (d[x].union(tmp[x]))
            d[x] = (d[x] + tmp[x]) / 2

    print("Number of iterations of the analysis : " + str(NBR_ITER))
    print("-------------------------------------------------")
    for x, y in d.items():
        print(str(x) + " : " + str(y))

if __name__ == '__main__':
    main()
