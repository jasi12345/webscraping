Web Scraping Anime Data from IMDb
Overview
This project is an automated web scraper that extracts anime data from IMDb and organizes it into an Excel sheet. It pulls essential details like title, release date, episodes, ratings, storylines, and creators using a combination of powerful Python libraries:

Selenium: For automating web browsing.
BeautifulSoup: For parsing HTML and extracting the data.
OpenPyXL: For storing and organizing the data in an Excel file.

Features

Scrapes a list of anime titles from IMDb.
Extracts details such as title, release date, episodes, ratings, storyline, and creators.
Stores the extracted data in an organized Excel sheet for easy access and management.

Tools & Libraries Used
Selenium: Automates web browsing and handles dynamic content.
BeautifulSoup: Parses HTML and extracts relevant data.
OpenPyXL: Organizes the extracted data into an Excel file.
Python 3.x: The primary programming language for building the scraper.

Installation
To run this project, you'll need Python 3.x and the following libraries. Follow these steps to get started:

1. Clone the repository:
First, clone this repository to your local machine using the following command:

bash
Copy
Edit
git clone https://github.com/your-username/your-repository-name.git
2. Install dependencies:
Navigate to the project directory and install the required libraries using pip:

bash
Copy
Edit
cd your-repository-name
pip install -r requirements.txt
Alternatively, you can manually install the dependencies with the following commands:

bash
Copy
Edit
pip install selenium
pip install beautifulsoup4
pip install openpyxl
pip install webdriver-manager
3. Install ChromeDriver:
The project uses Selenium for browser automation, so you’ll need ChromeDriver installed.

You can install ChromeDriver automatically using the webdriver-manager package, which is included in the requirements.

Alternatively, you can download ChromeDriver manually from here and add it to your system’s PATH.

4. Run the script:
Once the dependencies are installed, you can run the script to start extracting anime data:

bash
Copy
Edit
python scrape_anime.py
The script will fetch data from IMDb and save it in an Excel file named anime_list.xlsx.
