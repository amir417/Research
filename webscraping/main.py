import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv
import struct

filename = 'categories.csv'



# Define the struct format with variable-length strings
my_struct = struct.Struct('s s 4i')

# Define struct members with variable-length strings
title = "My Title"
category = "My Category"
size = 100
completed = 50
seeders = 10
leechers = 5

# Pack data into a bytes object
packed_data = my_struct.pack(
    title.encode('utf-8'), category.encode('utf-8'), size, completed, seeders, leechers)

# Unpack the data
unpacked_data = my_struct.unpack(packed_data)

print("Title:", unpacked_data[0].decode('utf-8'))
print("Category:", unpacked_data[1].decode('utf-8'))
print("Size:", unpacked_data[2])
print("Completed:", unpacked_data[3])
print("Seeders:", unpacked_data[4])
print("Leechers:", unpacked_data[5])






def find_categories():
    url = "https://www.demonoid.is/top_torrents.php"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", "font_12px") # This table holds all the information required. It is a table of all the famous videos.
    categoriesList = ['Music', 'TV', 'Books', 'Comics', 'Movies', 'Applications']

    imgs = [a.find('img') for a in table.find_all("a") if a.find('img')]
    category = [img.get('alt') for img in imgs if img.get('alt') in categoriesList]
    

    return category
    # The snippet code below scrapes the title of all the posted files in the table. 
    """ 
    titles = table.find_all ("a", class_="")
    for title in titles:
        print(title.text)
    """

def fileWriter(category, current_time):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        file.write(f"data tracked at current time : {current_time} => \n")
        writer.writerow(category)
        file.write('Waiting 20 mins for the next set of data...\n\n\n\n\n')


if __name__ == '__main__':
    # while True:
        category = find_categories()
        print (category)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        fileWriter (category, current_time)
        delay = 20
        time.sleep (delay * 60)





# video_titles = [video.find("a", class_="ytd-video-renderer").text
#                 for video in soup.find_all("ytd-video-renderer")][:20]

# for title in video_titles:
#     print(title)


