import webbrowser
import requests
import extractlinks as el

# Fetches the status code for an article.
# A valid page returns '200' whereas an invalid page returns '404'
def status_code(article_name):
    url = el.get_url(article_name)
    page_response = requests.get(url)
    return page_response.status_code

 
# This function modifies the article name so that it matches the URL.
# Spaces are converted to '_' and the words following spaces are capitalized. 
def refine_article_name(article_name):
    article_name.strip()
    refined_name = article_name[0].upper()
    for i in range(1, len(article_name)):
        if(article_name[i] == ' '):
            refined_name = refined_name + '_'
        elif(article_name[i-1] == ' '):
            refined_name = refined_name + article_name[i].upper()
        else:
            refined_name = refined_name + article_name[i]
    return refined_name


# Gets the user input for the article name.
# Checks whether the article exists or else asks the user to enter a correct article name.
def get_article_name():
    article_name = input()
    print('\n')
    article_name = refine_article_name(article_name)
    error_code = status_code(article_name)
    while(error_code == 404):
        article_name = input('Enter a valid article name:\n')
        article_name = refine_article_name(article_name)
        error_code = status_code(article_name)
    return article_name