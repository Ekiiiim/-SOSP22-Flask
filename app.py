# import flask libraries
from flask import Flask, jsonify, request, render_template
from bs4 import BeautifulSoup
import requests
import random
app = Flask(__name__)

# flask run -> server runs at http://127.0.0.1:24000/ 
@app.route("/")
def get_random_riddle():
    # generate the number of brain teaser
    num = random.randint(1, 999)
    # extract the teaser from a riddles website
    page = requests.get(f"https://www.riddles.com/{num}")
    soup = BeautifulSoup(page.text, "lxml")
    strs = soup.find_all("strong")
    str1 = str(strs[0].parent)
    str2 = str(strs[1].parent)
    str1 = str1[str1.find('</strong>')+len('</strong>'):str1.rfind('</div>')]
    str2 = str2[str2.find('</strong>:')+len('</strong>:'):str2.rfind('</div>')]
    # return a web page
    return render_template('template.html', number=num, question=str1, answer=str2)

@app.route("/<num>")
def get_a_riddle(num):
    num = int(num)
    # extract the teaser from a riddles website
    page = requests.get(f"https://www.riddles.com/{num}")
    soup = BeautifulSoup(page.text, "lxml")
    strs = soup.find_all("strong")
    str1 = str(strs[0].parent)
    str2 = str(strs[1].parent)
    str1 = str1[str1.find('</strong>')+len('</strong>'):str1.rfind('</div>')]
    str2 = str2[str2.find('</strong>:')+len('</strong>:'):str2.rfind('</div>')]
    # return a web page
    return render_template('template.html', number=num, question=str1, answer=str2)
