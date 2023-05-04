# This is a project to analyse Shakespeare's poem of Macbeth to find the most common words and plotting the answer.
# First step is importing important libraries
import matplotlib.pyplot as plt
import seaborn as sns
import requests  # This library is used to get information from the internet.
import string
sns.set_context("talk")
sns.set_style("whitegrid")

# Importing info from the net
response = requests.get('https://www.gutenberg.org/cache/epub/2264/pg2264.txt')
full_text = response.text

# The beginning describes the source/copyright, it isn't the actual text
# of the play until the 16648th character
macbeth = full_text[16648:]

# Print string summary
print("Data type:", type(macbeth))
print()
print("Number of characters:", len(macbeth))
print()
print("First 500 characters:")
print(macbeth[:500])

# First we split the whole play into lines and put them in a list
words_raw = list(macbeth.splitlines())

# Seeing length of the whole file
word_count = len(words_raw)
print('Here are the individual words')

# Since it's been put into lines we put each line in its own list
individual_sentences = []
for i in words_raw:
    # We then separate each word from each line and place them as elements in the list.
    i = i.split()
    individual_sentences.append(i)

# Now we have many lists within one list containing all the words of the play
individual_words = []
# We use a nested loop to extract each word from each list within the list and put it in a final list
for t in individual_sentences:
    for i in t:
        individual_words.append(i)

print('The first 100 individual words are', individual_words[:100])
print('Individual sentences are', individual_sentences[:100])
print("Macbeth contains {} words".format(len(individual_words)))
print("Here are the first 500 words", words_raw[: 500])
print("Here are some examples:", words_raw[11:21])

# You can use this punctuation string for defining what characters to remove

punctuated = string.punctuation
print(punctuated)

words_cleaned = []

for word in individual_words:
    # Remove punctuation
    word = word.strip(string.punctuation)
    # Make lowercase
    word = word.lower()
    # Append to words_cleaned
    words_cleaned.append(word)

# Use this print statement to double-check that everything
# is lowercase and has punctuation removed
print("Cleaned word examples:", words_cleaned[11:21])

# Building a dictionary which checks how many times a word appears in the play.
word_counts = {}
for i in words_cleaned:
    if i in word_counts:
        word_counts[i] += 1
    else:
        word_counts[i] = 1
print(type(word_counts))  # <class 'dict'>
print(len(word_counts))  # 3577

# Here is the maximum value
maximum = max(word_counts.values())

# Here is the minimum value
minimum = min(word_counts.values())

word_counts_list = list(word_counts.items())

# Here we want to check the most used word and the least used word.
for i in word_counts:
    if word_counts[i] == maximum:
        most_frequent_word = i
    elif word_counts[i] == minimum:
        least_frequent_word = i
    else:
        pass
print("The most frequent word in Macbeth is '{}', which appears {} times".format(
    most_frequent_word, word_counts[most_frequent_word]
))
print("The least frequent word in Macbeth is '{}', which appears {} times".format(
    least_frequent_word, word_counts[least_frequent_word]
))

# Plotting a histogram to show these values.
fig, ax = plt.subplots(figsize=(15, 5))
ax.hist(word_counts.values())
plt.show()

# This converts word_counts into a list of tuples,
# similar to student_tuples
counts_list = list(word_counts.items())

# Sort the list of tuples by the frequency (second element in each tuple)
# Make sure it goes from most to the least frequent
print('Here is the sorted dictionary')
counts_list_sorted = sorted(counts_list, key=lambda x: x[1], reverse=True)
word_counts = dict(counts_list_sorted)
print(word_counts)
print('Here is the sorted list')
print(counts_list_sorted)

# Slice the sorted list to just the first 25 tuples
top_25 = counts_list_sorted[0:25]
print('Here are the top 25 words and how frequently they occur')
print(top_25)

# Make a list of dummy numbers to populate the axis with the words
ticks = None

# Get just the words from top_25 and assign to labels
labels = []
for i in top_25:
    labels.append(i[0])

# Get just the frequencies from top_25 and assign to frequencies
frequencies = []
for i in top_25:
    frequencies.append(i[1])

print("Tick values:", ticks)
print()
print("Labels:", labels)
print()
print("Frequencies:", frequencies)

fig, ax = plt.subplots(figsize=(15, 15))
plt.barh(labels, frequencies)
plt.xlabel('Frequency of occurrence')
plt.ylabel('Words')
plt.title('Frequency of word occurrence in MacBeth for the 25 top words')
plt.show()
