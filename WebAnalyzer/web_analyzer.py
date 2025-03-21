import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

# Printing out the prettify text:
print(soup.prettify())

#Step 3
headings = sum(len(soup.find_all(f'h{i}')) for i in range(1, 7))

links = len(soup.find_all('a'))

paragraphs = len(soup.find_all('p'))

print(f"Number of headings: {headings}")
print(f"Number of links: {links}")
print(f"Number of pargraphs: {paragraphs}")

#Step 4
text = soup.get_text()
text = text.split()
lower_text = [texts.lower() for texts in text]

keyword = input("Enter a keyword to search for: ").lower()

count = lower_text.count(keyword)

print(f"The keyword '{keyword}' appears {count} times in the webpage.")

#Step 5
text_content = soup.get_text()
words = text_content.split()
words = [word.lower() for word in words]
word_counts = {word: words.count(word) for word in words}

print("Top 5 Words With Counts:")
# Get all of the values and sort them in a list. Get the top 5 values and return their word which is their key.
word_count_list = list(word_counts.values())
word_count_list.sort(reverse=True)
top_word_counts = word_count_list[:5]
for i in top_word_counts:
    for j in word_counts.keys():
        if(word_counts[j]==i):
            print(str(j)+" : "+str(word_counts[j]))

#Step 6
paragraphs2 = [p.get_text() for p in soup.find_all("p")]
print("")
print("Longest Paragraph:")

most_words = 0
longest_paragraph = None
for paragraph in paragraphs2:
    words_in_paragraph = paragraph.split()
    num_words = len(words_in_paragraph)
    if num_words >= 5:
        if num_words > most_words:
            most_words = num_words
            longest_paragraph = paragraph

print(f"Number of words: {most_words}")
print(f"Paragraph:\n{longest_paragraph}")

#Step 7
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group 17')
plt.ylabel('Count')
plt.show()