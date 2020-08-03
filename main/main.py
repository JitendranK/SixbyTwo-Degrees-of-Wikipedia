import articlename as an
import findlink as fl

def main():
    print('\nEnter an article to start from:')
    start_article = an.get_article_name()
    print('Enter an article to search for:')
    end_article = an.get_article_name()
    print("\nSit back and relax while we find the articles for you....")
    fl.find_link(start_article, end_article)

if __name__ == '__main__':
    main()