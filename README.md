# selenium-task
# El País Opinion Scraper

This project automates the extraction and analysis of articles from the **Opinion** section of *El País*, a major Spanish news outlet. It includes web scraping, translation, and cross-browser testing using Selenium and BrowserStack.

---

## Features

- **Language Verification**: Ensures the website content is displayed in Spanish.
- **Web Scraping**: Extracts titles, article content, and cover images (if available) from the first five Opinion articles.
- **Title Translation**: Translates Spanish article titles into English using a translation API (Google Translate or Rapid API).
- **Keyword Analysis**: Identifies words repeated more than twice across all translated titles.
- **Cross-Browser Testing**: Validates the script both locally and on BrowserStack using five parallel threads across desktop and mobile browsers.

---

## Tech Stack

- Python
- Selenium WebDriver
- BeautifulSoup
- Translation APIs (Google / Rapid Translate)
- BrowserStack (for automated cross-browser testing)

scraper.git
 
