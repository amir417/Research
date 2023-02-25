import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

filename = "mainTorrent.csv"
# Make a request to the Demonoid website
response = requests.get("https://www.demonoid.is/top_torrents.php")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the top torrents
table = soup.find("table", "font_12px")

# Extract the rows from the table
rows = table.find_all("tr")[2:]  # Ignore the first row, which contains headers
# print (rows)
flag1, flag2 = False, False
categoriesList = ['Music', 'TV', 'Books', 'Comics', 'Movies', 'Applications']


row = []
totalCount  = 0
dividerCount = 0
titleCount = 0
extraDataCount = 0

if __name__ == '__main__':
    while True :
        
        with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                current_time = datetime.now().strftime("%H:%M:%S")
                file.write(f"\n\n\n\ndata tracked at current time : {current_time} => \n")

        for line in rows:
                cells = line.find_all("td")
                
                totalCount += 1
                
                # Open the CSV file in append mode
                with open(filename, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file, delimiter=',')
                    
                    

                    if len(cells) == 1:
                        dividerCount += 1
                        flag1 =  True
                        flag2 =  True
                        # row.append ("Here is a divider")
                        break
                    elif len(cells) == 2:
                        titleCount += 1
                        flag1 =  True
                        for td in cells:
                            if td.has_attr('class') and ('tone_1_pad' in td['class'] or 'tone_3_pad' in td['class'] ) :
                                a_tag = td.find('a')
                                if a_tag:
                                    content = a_tag.text.strip()
                                    row.append(content.encode("utf-8"))  # add content to the row
                                    # print (content)
                            elif td.has_attr('class') and ('tone_2_bl' in td['class'] or 'tone_1_bl' in td['class']) :
                                img_tag = td.find('img')
                                if img_tag:
                                    alt_text = img_tag.get('alt')
                                    row.append(alt_text)  # add alt_text to the row
                                    # print (alt_text)
                    elif len(cells) == 8:
                        extraDataCount += 1
                        flag2 =  True
                        for tag in cells:
                            # print(tag.text.strip())
                            row.append(tag.text.strip())
                        # num_data(cells)


                    # write the row to the CSV file
                    if row and flag1 and flag2:
                        writer.writerow(row)
                        
                        print (row)
                        flag1, flag2 = False, False
                        row = []  # reeset an empty list for the row
                
                
        delay = 20
        print ("waiting for 20 mins...")
        time.sleep (delay * 60)


# COunts
print (totalCount)
print (dividerCount)
print (titleCount)
print (extraDataCount)




