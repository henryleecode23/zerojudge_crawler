import bs4

def get_title(bs4: bs4.BeautifulSoup):
    problem_title = bs4.find(id= "problem_title")
    problem_id = bs4.find("div", class_="h1")
    title = ""
    for t in range(5):
        title += problem_id.text[t]
    title+=problem_title.string
    return title