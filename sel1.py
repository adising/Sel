from selenium import webdriver
from flask import Flask, render_template, request, redirect
# from time import sleep
# from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open',methods=['POST'])
def open():
    browser=request.form['browser']
    url=request.form['url']

    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='edge':
        driver=webdriver.Edge()
    else:
        return "Unsupported browser"
    
    driver.get(url)

    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)

    while(True):
        pass
    # sleep(30)
    return f"Opened {url} in {browser}"

if __name__ == '__main__':
    app.run(debug=True)