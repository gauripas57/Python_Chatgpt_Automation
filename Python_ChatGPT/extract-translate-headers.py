

# Importing required modules 
import requests 
from bs4 import BeautifulSoup 
from googletrans import Translator

# URL of the web page 
URL = "https://www.growthmachine.com/blog/should-you-publish-on-medium"

# Make a GET request to fetch the raw HTML content 
html_content = requests.get(URL).text

# Parse the html content 
soup = BeautifulSoup(html_content, "lxml") 

# Extract all headers from the web page 
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) 

# Initialize the translator 
translator = Translator() 

# Translate the headers to Hindi 
translated_headers = [translator.translate(header.text, dest='hi').text for header in headers] 

# Write the translated headers to an HTML file 
with open('translated_headers.html', 'w') as f: 
    f.write('<html>\n') 
    f.write('<head><title>Translated Headers</title></head>\n') 
    f.write('<body>\n') 
    for header in translated_headers: 
        f.write('<h1>' + header + '</h1>\n') 
    f.write('</body>\n') 
    f.write('</html>\n')