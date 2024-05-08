# run every few minutes / Main Loop
import time
from bs4 import BeautifulSoup
import requests
from PIL import Image
from win10toast import ToastNotifier

while True:
    # Web scraping
    html_text = requests.get("https://covid-19.ontario.ca").text
    soup = BeautifulSoup(html_text, 'html')
    cases = soup.find_all('div', class_ = 'ontario-infographic-number')[0].text
    posted_date = soup.find_all('div', class_="ontario-column ontario-small-12 ontario-section__covid-stats")[-1]
    posted_date = posted_date.find('p').text

    # Convert png to ico for icon in notification
    filename = "canada.png"
    img = Image.open(filename)
    img.save('logo.ico')
    
    # Notifier
    notifier = ToastNotifier()
    title = "COVID ALERT"
    publish = "Updated " + f"{' '.join(posted_date.split(' ')[15:23])} \n"
    message = f"Total Cases: {' '.join(cases.split(' ')[18:19])}"
    notifier.show_toast(title=title, msg= publish + message, duration=5, icon_path='logo.ico')

    # Timer
    time.sleep(15)
