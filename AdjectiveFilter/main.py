import re  # regular expression
"""
This class reads through a text file ("Article.txt") and writes all the adjectives from it into a "Result.txt" file.

How to use:
    1. Copy an article's text and paste it into the "Article.txt" file.
    2. Click Run
    3. Open the "Result.txt" folder to see all the adjectives that were in your article.

Author: Shem Snow
Created: 11/19/2022
Last Edited: 11/20/2022
"""

# If you want the Result file to contain duplicates for words that appear in the article more than once, set this to "True". If you don't want duplicates, set it to "False".
allow_duplicates = False

# set the file paths
adj_path = "Adjectives.txt"
article_path = "Article.txt"
result_path = "Result.txt"

# Create a dictionary big enough to hold all adjectives.
adjectives = dict()
for i in range(10_000):
  adjectives[i] = None

# Read through the "Adjectives" file and save each adjective into the dictionary
adj_file = open(adj_path, 'r')
for line in adj_file:
  adj = line.split("\n")[0].lower()
  adjectives[hash(adj)] = adj  # key = hash(adj), value = adj.
adj_file.close()

# Open the "Article" and "Result" files.
article_file = open(article_path, 'r')
result_file = open(result_path, 'w')

# Save all the words from the article into a collection (lists allow duplicates and sets do not).
words = re.sub(r'[^a-zA-Z\-]+', ' ', article_file.read()).split() if allow_duplicates \
    else set(re.sub(r'[^a-zA-Z\-]+', ' ', article_file.read()).split())
article_file.close()

# Convert all words to lower case
lower_case_words = list() if allow_duplicates else set()
for word in words:
  if allow_duplicates:
    lower_case_words.append(word.lower())
  else:
    lower_case_words.add(word.lower())

# For each word in the collection, if it's an adjective, write it to the "Result" file.
for word in lower_case_words:
  if hash(word) in adjectives:
    result_file.write(word + "\n")
result_file.close()
