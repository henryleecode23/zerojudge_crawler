import urllib.request as request
import ssl
import bs4

class zj_crawler():
    def __init__(self,id):
        self.zj_url = f"https://zerojudge.tw/ShowProblem?problemid={id}"
        self.context = ssl._create_unverified_context()

        self.request_data = request.Request(self.zj_url,
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
            })

        with request.urlopen(self.request_data,context=self.context) as response:
            self.data = response.read().decode("utf-8")

        self.soup = bs4.BeautifulSoup(self.data, "html.parser")
    
    # 標題
    def get_title(self):
        problem_title = self.soup.find(id= "problem_title")
        problem_id = self.soup.find("div", class_="h1")
        title = ""
        for t in range(5):
            title += problem_id.text[t]
        title+=problem_title.string
        return title

    # 敘述
    def get_problem_content(self):
        problem_content = self.soup.find(id = "problem_content").text
        return problem_content

    # 輸入說明
    def get_input_illustrate(self):
        input_illustrate = self.soup.find(id = "problem_theinput").text
        return input_illustrate

    # 輸出說明
    def get_output_illustrate(self):
        output_illustrate = self.soup.find(id = "problem_theoutput").text
        return output_illustrate

    # 範例輸入
    def get_ex_input(self):
        items = self.soup.find_all("pre")
        counter = 0
        for i in range(0,len(items), 2):
            counter += 1
            print(f"範例輸入#{counter}: ",end="")
            print(items[i].text.replace("\n",""))

    # 範例輸出
    def get_ex_output(self):
        items = self.soup.find_all("pre")
        counter = 0
        for i in range(1,len(items), 2):
            counter += 1
            print(f"範例輸出#{counter}: ",end="")
            print(items[i].text.replace("\n",""))

    # 測資長度
    def get_test_case_quantity(self):
        items = self.soup.find_all("pre")
        return int(len(items)/2)


a001 = zj_crawler("a001")

