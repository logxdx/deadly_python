import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the IPL match page
url = 'https://www.cricbuzz.com/live-cricket-scores/69568/gt-vs-mi-qualifier-2-indian-premier-league-2023'  # Replace with the actual URL of the IPL match page
response = requests.get(url)
html_content = response.text

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract match details
match_details = soup.find('div', class_='match-details').text.strip()
print('Match Details:', match_details)

# Extract runs and wickets
runs = soup.find('span', class_='runs').text
wickets = soup.find('span', class_='wickets').text
print('Runs:', runs)
print('Wickets:', wickets)

# Extract commentary
commentary_section = soup.find('div', class_='commentary-section')
commentary = commentary_section.text.strip()
print('Commentary:', commentary)

# Extract bowler details
bowler_section = soup.find('div', class_='bowler-section')
bowlers = bowler_section.find_all('div', class_='bowler')
print('Bowler Details:')
for bowler in bowlers:
    bowler_name = bowler.find('span', class_='name').text
    bowler_stats = bowler.find('span', class_='stats').text
    print(f'Bowler: {bowler_name}, Stats: {bowler_stats}')

# Extract batsman details
batsman_section = soup.find('div', class_='batsman-section')
batsmen = batsman_section.find_all('div', class_='batsman')
print('Batsman Details:')
for batsman in batsmen:
    batsman_name = batsman.find('span', class_='name').text
    batsman_stats = batsman.find('span', class_='stats').text
    print(f'Batsman: {batsman_name}, Stats: {batsman_stats}')
