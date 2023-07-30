import requests
from bs4 import BeautifulSoup
import time,datetime

f=open("E:\OneDrive - IIT Delhi\CODE\Deadly_Python\Web Scraper\IPL.txt","r+")

x = datetime.datetime.now()
daate = x.strftime("%x")
taime = x.strftime("%X")

# Fetch the HTML Content
url = 'https://www.cricbuzz.com/live-cricket-scores/69568/gt-vs-mi-qualifier-2-indian-premier-league-2023'
response = requests.get(url)
html_content = response.text

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
score_element = soup.find('div', class_='cb-col-100 cb-col cb-col-scores')
score = score_element.text.strip()

# Initialize previous_score
previous_score = score
print(score+' '+str(daate)+' '+str(taime))
f.write(score+' '+str(daate)+' '+str(taime))

while True:
    
    # Fetch the HTML Content
    response = requests.get(url)
    html_content = response.text

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    score_element = soup.find('div', class_='cb-col-100 cb-col cb-col-scores')
    score = score_element.text.strip()
    
    # Check if the score has changed
    if score != previous_score:
        print(score+' '+str(daate)+' '+str(taime))
        f.write(score+' '+str(daate)+' '+str(taime))
        f.write('\n')
        f.flush()
        previous_score = score

    # Wait for a specific interval before checking for updates again
    time.sleep(10)  # Wait for 10 seconds before the next check
