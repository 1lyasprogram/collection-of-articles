import json


def get_articles():
    with open('../articles.json', 'r', encoding='utf-8') as f:
        load = json.load(f)
    return load


def save_article(name, text):
    articles = get_articles()
    articles[name] = text
    with open('../articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False)


print(get_articles())
save_article('статья', 'крутая статья')


def delete_article(name):
    articles = get_articles()
    del articles[name]
    with open('../articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False)


delete_article('статья')
