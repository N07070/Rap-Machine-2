À ajouter dans le programme

w ij = fij log(N/ nj ) : this formulas allows us to calculate the similarity beteen produced lyrics and all verses from the same arist. Here, N is the nomber of all the verses, nj is the number of verses containing term j and fij is the freuency of term j in the ith verse : this formulas allows us to calculate the cosine distance between verses, being a measure of similary. The more the score obtained is low, the more novel are the lyrics (Peter Potash, Alexey Romanov, Anna Rumshisky)

Rhyme density = total nb of rhymed syllables / total nb of syllables : goal : produce rhyme types and rhyme frequency that are similar to the artist, or even better to the artist’s average rhyme density.

“ EndRhyme = the number of matching vowel phonemes at the end of lines L and sm−1, i.e., the line before the last in B. This feature captures alternating rhyme schemes of the form “abab.” OtherRhyme = the average number of matching vowel phonemes per word. For each word in L, we ﬁnd the longest matching vowel sequence in sm and average the lengths of these sequences. This captures other than end rhymes.

LineLength. Typically, consecutive lines are roughly the same length since they need to be spoken out within one musical bar of a ﬁxed length. The length similarity of two lines L and s is computed as 1− |len(L)−len(s)| / max(len(L),len(s)) where len(.) is the function that return the nb of characters in a line. We compute the length similarity between a candidate line and the last line sm of the song preﬁx B.
https://pronouncing.readthedocs.io/en/latest/tutorial.html : comment exploiter le CMU dictionary avec des formules de code à inclure dans le programme (si non, pas d’aspect linguistique) :

- word pronunciations : pour les prononciations générales des mots
- pronunciation search : permet de connaître les prononciation des mots suivant des contextes différents
- counting syllables : permet de connaître le nb de syllabes par vers / ligne, très important pour l’analyse métrique
- meter : permet de représenter des rhytmes réguliers qu’on va retrouver par vers / strophe
Toutes les formules sont expliquées sur le lien.
À ajouter dans l’abstract
Mention de l’utilisation de l’utilisation dans notre programme de CMU Pronouncing Dictionary.
