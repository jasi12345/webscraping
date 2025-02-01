from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Anime List"
sheet.append(['No', 'Anime Title', 'Date', 'Episodes','Rates','Story','Creators'])  


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    url = "https://www.imdb.com/list/ls528834346/"
    driver.get(url)  
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    container = soup.find("div", attrs={"data-testid": "list-page-mc-list-content"})

    if container:
        for index, item in enumerate(container.find_all("li", class_="ipc-metadata-list-summary-item"), start=1):
            
            title_div = item.find("h3")
            title = title_div.get_text(strip=True) if title_div else "N/A"

            
            metadata = item.find_all("span", class_="dli-title-metadata-item")
            date = metadata[0].get_text(strip=True) if len(metadata) > 0 else "N/A"
            episodes = metadata[1].get_text(strip=True) if len(metadata) > 1 else "N/A"
    
            rating_span = item.find("span", attrs={"data-testid": "ratingGroup--imdb-rating"})
            rating = rating_span.get_text(strip=True) if rating_span else "N/A"

            story_span = item.find("div", attrs={"class": "ipc-html-content"})
            story = story_span.get_text(strip=True) if story_span else "N/A"

            creators_span = item.find("a", attrs={"class": "ipc-link"})
            creators = creators_span.get_text(strip=True) if creators_span else "N/A"

            
            sheet.append([index, title, date, episodes,rating,story,creators])

    print("✅ Successfully scraped IMDB Anime List!")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()  

excel.save("anime_list.xlsx")
print("✅ Anime list saved to anime_list.xlsx")
