"""
Developer   : Naman Dave
College ID  : 201801439
About       : Recomendation algorithm, with pre HASH <-> I_HASH builders and loaders
Sources     :
1) LCS: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
2) Recombyte(Recom) : https://colab.research.google.com/drive/1kc5_IT0hSBM2ge1UsiOWwjVKLERba12g?usp=sharing
"""



import os
import sys
import math
import tqdm
import pickle
import enchant
import numpy as np

DATA_STORAGE_FILENAME = "data_storage.p"
HASH_DUMP_FILE_NAME = "words_total.txt"


def hash_build(query_list: "List of queries") -> "HASH":
    total_words = set()
    for query_word in tqdm.tqdm(query_list, leave=True, position=0):
        s1 = set(list(map(str.lower, query_word.replace("_", " ").split())))
        s2 = set(list(map(str.lower, query_word.split())))
        total_words = total_words.union(s1, s2)
    return total_words


def inv_hash_build(
    query_list: "List of queries", total_words: "HASH"
) -> "Inverse HASH":
    words_dict = dict()
    for word in tqdm.tqdm(total_words, leave=True, position=0):
        words_dict[word] = [[], np.zeros(len(query_list))]
        for cnt, med in enumerate(query_list, start=0):
            words1 = str.lower(med).split()
            words2 = str.lower(med).split("_")
            if word in words1 or word in words2:
                words_dict[word][0].append(cnt)
                words_dict[word][1][cnt] = 1
    return words_dict


def save_hash(total_words: "HASH") -> None:
    if os.path.exists(HASH_DUMP_FILE_NAME):
        os.remove(HASH_DUMP_FILE_NAME)

    with open(HASH_DUMP_FILE_NAME, "a") as f:
        f.write("\n".join(list(total_words)))


load_hash = lambda: enchant.PyPWL(HASH_DUMP_FILE_NAME)


def save_data(query_list: "List of queries") -> list:
    total_words = hash_build(query_list)

    words_dict = inv_hash_build(query_list, total_words)
    save_hash(total_words)

    tot_words_dict = load_hash()
    pickle.dump(
        (query_list, total_words, words_dict, tot_words_dict),
        open(DATA_STORAGE_FILENAME, "wb"),
    )
    return query_list, total_words, words_dict, tot_words_dict


def load_data() -> list:
    if not os.path.exists(DATA_STORAGE_FILENAME):
        raise FileNotFoundError(
            DATA_STORAGE_FILENAME + "does not exists, pleaes save hash once"
            "using save_data in Recombyte"
        )
    query_list, total_words, words_dict, tot_words_dict = pickle.load(
        open(DATA_STORAGE_FILENAME, "rb")
    )
    return query_list, total_words, words_dict, tot_words_dict


def autocorrect_word(
    input_query_word_name: "Input Query", tot_words_dict: "Enchant object"
) -> "Best fit word":
    input_query_word_name = str.lower(input_query_word_name)
    # check if the word exists in the dictionary
    word_exists = tot_words_dict.check(input_query_word_name)
    if not word_exists:
        # get suggestions for the input word
        suggestions = tot_words_dict.suggest(input_query_word_name)
        return suggestions
    return input_query_word_name


def lcs(X: "iterable object", Y: "iterable object") -> "LCS score":

    """
    Dynamic Programming implementation of LCS problem
    """

    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


def validate_accuracy(input_string: str, evaluate: callable = lcs) -> None:
    l1 = autocorrect_word(input_string)
    print(len(l1), "matches:\nscores:")
    for i in l1:
        print(i, evaluate(i, input_string) / len(input_string))


def recombyte_q(
    sentence: str,
    query_list: "List of queries",
    words_dict: "Inverse Hash",
    tot_words_dict: "enchant dict object",
    t1: float = 0.7,
    t2: float = 0.5,
    c3: float = 0.9,
    t4: float = 0.55,
    evaluate: callable = lcs,
    evaluate2: callable = lcs,
    take_best: bool = False,
    tbt1: float = 0.8,
    tbt2: float = 0.6,
) -> list:

    """
    Prescriber: Prescribes the best query_words with the help of
                search engine algorithms, and NLP (error-correction).

    Input:
        sentence: str, sentence / space separated words

        t1: Hyperparameter 1-Threshold Value for the best word
            selection (take_best=False), default=0.7, depends upon evaluate method

        t2: Hyperparameter 2-Threshold Value for an average word
            selection (take_best=False), default=0.5, depends upon evaluate method

        c3: Hyperparameter 3-Criteria(%) for selection amongst all the
            query_word scores, default=0.9

        t4: Hyperparameter 4-Threshold Value for the evaluation2 method for
            selection, default=0.7, depends upon evaluate2 method

        evaluate: Evaluation method for assigning the score for individual words,
                must be proportional to the input string or
                (might) need to change the Hyperparameters and Criteria (t1, t2),
                default=lcs

        evaluate2: Evaluation method for assigning the score for sentence,
                must be proportional to the input string or
                (might) need to change the Hyperparameters and Criteria (c3, t4),
                default=lcs

        take_best: Boolean value to consider only the best value,
                uses evaluate method for the score assignment

        tbt1: Take best t1, Hyperparameter 1-Threshold Value in take_best case,
            default=0.8

        tbt2: Take best t2, Hyperparameter 2-Threshold Value in take_best case,
            default=0.6

    Output:
        returns: List of best matched query_words

    """
    sentence = sentence.lower()
    answer_vector = np.zeros(len(query_list))
    words_set = sentence.split()

    for word in words_set:

        flag = False
        suggestions = autocorrect_word(word, tot_words_dict)
        # print(suggestions)
        if suggestions == []:
            continue

        if isinstance(suggestions, list) and len(suggestions) > 1:
            if take_best:
                # print("hi")
                best_word = None
                best_score = 0.0
                for i in suggestions:
                    score = evaluate(i, word) / len(word)
                    if score > best_score:
                        best_score = score
                        best_word = i
                # print(best_word)
                if best_score > tbt1 and len(word) + len(best_word) > 5:
                    return [[query_list[words_dict[best_word][0][0]], best_score]]
                elif best_score > tbt2:
                    answer_vector += words_dict[best_word][1]
            else:

                for suggestion in suggestions:
                    suggestion = suggestion.lower()
                    score = evaluate(suggestion, word) / len(word)
                    if not flag:
                        if score > t1:
                            flag = True
                            answer_vector += words_dict[suggestion][1]
                        elif score > t2:
                            answer_vector += score * words_dict[suggestion][1]
                    else:
                        if score > t1:
                            answer_vector += words_dict[suggestion][1]

        else:
            if isinstance(suggestions, list):
                suggestions = suggestions[0]
            # print(type(suggestions), suggestions)
            if len(words_dict[suggestions][0]) == 1:
                return [[query_list[words_dict[suggestions][0][0]], 1.0]]
            else:
                # print(sum(words_dict[suggestions][1]))
                answer_vector += words_dict[suggestions][1]
    # print(sum(answer_vector))
    if np.sum(answer_vector) == 0:
        return []
    answer_new_vector = np.argsort(answer_vector)
    t3 = answer_vector[answer_new_vector[-1]]
    answer = [query_list[answer_new_vector[-1]]]
    i = 1
    while answer_vector[answer_new_vector[-1 - i]] > c3 * t3:
        answer.append(query_list[answer_new_vector[-i - 1]])
        i += 1
    final_answer = []
    for ans in answer:
        score = evaluate2(ans.lower(), sentence.lower()) / len(ans)
        #print(ans, sentence, score, sep="|")

        if score > t4:
            final_answer.append([ans, score])

    final_answer = sorted(final_answer, key=lambda x: x[1], reverse=True)
    #print("Here", final_answer)
    return final_answer


if __name__ == "__main__":

    my_list = [
        "Open Chrome",
        "Open text editor",
        "Open Mozila firefox",
        "Evaluate string",
        "Search Online",
        "Search File",
        "Play music",
        "Play Song ",
        "Open Youtube",
    ]
    query_list = list(my_list)
    if not os.path.exists(DATA_STORAGE_FILENAME):
        save_data(query_list)
    query_list, total_words, words_dict, tot_words_dict = load_data()

    print("tests...")
    print(
        recombyte_q(
            "Opun the Chroma", query_list, words_dict, tot_words_dict, take_best=True
        )
    )
    print(
        recombyte_q(
            "Hey badman, don go upa n dan jass opan the Chrame",
            query_list,
            words_dict,
            tot_words_dict,
            take_best=True,
        )
    )
