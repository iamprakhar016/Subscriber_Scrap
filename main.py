import requests
from bs4 import BeautifulSoup

while True:
    url = input("Enter A YouTube Channel URL To Know Subscribers \n")
    response = requests.get(url)
    if response.status_code != 200:
        print(
            f"\nInvalid URL. Response Status Code Is {response.status_code}\n")
        continue

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.find(
        'a', {"class": "spf-link branded-page-header-title-link yt-uix-sessionlink"})

    subsriber = soup.find('span', {
        'class': 'yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip'})

    print("\n"+name.attrs['title'] + ' have ' +
          subsriber.attrs['aria-label']+"\n")

    inp = (input("Press Y to proceed \n")).lower()
    if inp != 'y':
        break
