#Regular expressions are patterns used to match character combinations in strings.
#
import re
from itertools import permutations

test_case_count = int(input(""))

for i in range(0, test_case_count):
    sample = input("")
    paragraph = input("")

    list_of_perm = list(permutations(sample))

    regex_str = "("
    for text in list_of_perm:
        regex_str = regex_str + "".join(text) + "|"

    regex_str = regex_str[:len(regex_str) - 1]  + ")"

    regex_sample = re.compile(regex_str)
    search_result = regex_sample.search(paragraph)


    if (search_result):
        print("YES")
    else:
        print("NO")

#First we take the number of comparisons that we have to perform,if we choose for example 3 comparisons then we can test three sets of words.
#For this instance we are typing out the required comparisons just to keep things simple.If we had to compare the entire book then we would've provided the data
#of the entire book.Regex is efficient and one of most simple ways to compare the strings.


