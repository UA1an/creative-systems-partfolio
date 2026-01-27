For this task, I created a Python web scraper using the requests library and BeautifulSoup. The purpose of the task was to collect and display creative data from a public website. I chose to scrape short quotes from *quotes.toscrape.com*, as quotes represent creative textual content that can be reused in generative or artistic projects.

The script begins by importing the required libraries. The `requests` library is used to send an HTTP request to the website and retrieve its HTML content. BeautifulSoup is then used to parse and navigate this HTML structure.

```python
import requests
from bs4 import BeautifulSoup
```

Next, the script sends a request to the target URL and stores the response. This allows the program to access the raw HTML of the webpage.

```python

response = requests.get(url)
```

The HTML content is then parsed using BeautifulSoup. By specifying **`"html.parser"`**, the script converts the HTML into a structure that can be searched and navigated.

```python
soup = BeautifulSoup(response.text, "html.parser")
```

The script searches for specific HTML elements that contain the quotes. In this case, each quote is stored inside a div element with the class name "quote". This step is essential for targeting only the relevant creative content on the page.

```python
quotes = soup.find_all("div", class_="quote")
```

Each quote is then processed inside a loop. The text of the quote and the name of the author are extracted separately using their HTML tags. This data is printed in the terminal and also written to a text file so that it can be reused later.

```python

with open("quotes.txt", "w", encoding="utf-8") as file:
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        file.write(f"{text} — {author}\n\n")
```

One of the main challenges of this task was understanding how to inspect a webpage and identify the correct HTML elements to scrape. I also encountered issues related to Python versions and missing libraries, which helped me better understand how Python environments and package installation work.

Overall, this task helped me learn the fundamentals of web scraping and data extraction. I can see how this approach could be extended for creative coding projects, such as generating text-based artworks, using scraped text as input for sound synthesis, or combining external data with interactive systems.

![[ScreenOfWork.png]]
*screen of work*

![[TerminalResult.png]]
*terminal result*

