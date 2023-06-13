import string
import wikipediaapi


def read_wiki_titles(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title, lang="en") -> str:
    w_api = wikipediaapi.Wikipedia(lang)
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def read_articles() -> str:
    titles = read_wiki_titles('small.txt')
    for title in titles:
        yield get_article(title)


letters = list(string.ascii_lowercase)


def count_avg(chars: list[str] = letters) -> dict[str, float]:
    """
    Liczy srednia liczbe wystapien podanych znakow w artukolach.

    Po wszelkich optymalizacjach kod nadal potrzebuje okolo 5 minut na zakonczenie
    :param chars: znaki, ktore trzeba policzyc
    :return: slownik z literami i srednia iloscia wystapien
    """
    all_arts = 0
    counter = {letter: 0 for letter in chars}
    for art in read_articles():
        all_arts += 1
        for c in chars:
            counter[c] += art.count(c)
    if all_arts != 0:
        for c, n in counter.items():
            counter[c] /= all_arts
    return counter


print("Average:", *[f"{c} -> {n}" for c, n in count_avg().items()], sep="\n")
