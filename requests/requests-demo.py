from bs4 import BeautifulSoup
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO





# Example: Fetch HTML content from a webpage
url = "https://mp.weixin.qq.com/s/bqSinsiToxsVGvDyd2YP2g"
response = requests.get(url)
html_content = response.content






# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')


# Example: Find the title tag
title_tag = soup.title
print(title_tag)

# Example: Find all <a> tags (links)
a_tags = soup.find_all('img')
for a in a_tags:
    # print(a.get('data-src'))
    img_url = a.get('data-src')

    if img_url is not None:
        print(img_url)
        response = requests.get(img_url)

        if response.status_code == 200:
            # Get current time
            current_time = datetime.now()
            current_time_str = current_time.strftime('%H%M%S')

            with Image.open(BytesIO(response.content)) as img:
                img.save(current_time_str + ".png")

            print("download successfully")
        else:
            print("failed to download")
