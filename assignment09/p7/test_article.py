# test_article.py
# student.py
# CTMS-14
# a9 p7.py
# Ahmed Abasimel
# aabasimel@constructor.university
from article import Article

def main():
    
    article1 = Article("Laptop", "Electronics", "Dell", 10, 899.99)
    article2 = Article("Smartphone", "Electronics", "Samsung", 25, 699.50)

    print("Article 1 Info:")
    article1.printInfo()
    print("\nArticle 2 Info:")
    article2.printInfo()

if __name__ == "__main__":
    main()
