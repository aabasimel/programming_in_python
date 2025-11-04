# test_article.py
# CTMS-14
# a9 p8.py
# Ahmed Abasimel
# aabasimel@constructor.university

from article import Article

def main():
    # Read the number of articles
    n = int(input("Enter the number of articles: "))

    articles = []

    # Create n articles from user input
    for i in range(n):
        print(f"\nEnter details for article {i + 1}:")
        name = input("Name: ")
        category = input("Category: ")
        brand = input("Brand: ")
        stock = int(input("Stock: "))
        price = float(input("Price: "))
        
        article = Article(name, category, brand, stock, price)
        articles.append(article)

   
    for idx, article in enumerate(articles, start=1):
        print(f"\nArticle {idx}:")
        article.printInfo()

if __name__ == "__main__":
    main()
