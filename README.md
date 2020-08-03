# SixbyTwo-Degrees-of-Wikipedia

SixByTwo Degrees of Wikipedia is a website which traverses hyperlinks on Wikipedia to find whether two articles can be reached within three clicks.

## How does it work?
SixByTwo Degrees of Wikipedia checks whether an article can be reached from a source article within three clicks. It opens the Wikipedia page of the given article and then parses the HTML page to find the hyperlinks to other articles. Breath-First Search is used to find the hyperlinked path between the two articles. After finding the path between the articles, they are opened in the Google Chrome browser. 

**Note:** Since the articles are fetched directly from Wikipedia website, the application is feasible only up to three levels of connection. Anything more than that will take significant time.

## Tech Stack
* **Python** programming langauge 
* **BeautifulSoup** library for parsing wikipedia page
* **urllib** package for handling URLs
* **Selenium WebDriver** framework for automatically opening articles

## Inspiration
* I got the idea for this project after reading about the theory of **Six Degrees of Separation**, which states that all the people in the world are six connections from each other.
* After doing some research I found these awesome websites which pushed me to do this project
  - [Orcale of Bacon](https://oracleofbacon.org/)
  - [Six Degrees of Wikipedia](https://www.sixdegreesofwikipedia.com/)
