import requests
import bs4
import pandas as pd

df = pd.read_csv('channels.csv',encoding= 'unicode_escape')

f = open(r'extracted_informa.csv','wb')
f.write('TEXT EXTRACTED\n'.encode())
 
for i in range(0, len(df.appbundleid)):
    text = str(df.appbundleid.loc[i])
    
    url = 'https://google.com/search?q=' + text

    # Fetch the URL data using requests.get(url) and storing it in a variable name request_result.
    request_result=requests.get(url)

    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,"html.parser")
  
    # finding first heading
    heading_object=soup.find('h3')
    
    info_extracted = heading_object.getText()
    print(info_extracted)
    f.write("\n".encode())
    f.write(info_extracted.encode())
f.close()
