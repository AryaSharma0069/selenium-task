# 📰 El País Opinion Scraper

This project automates the extraction and analysis of articles from the **Opinion** section of *El País*, a major Spanish news outlet. It includes web scraping, translation, and cross-browser testing using Selenium and BrowserStack.

---

## ✅ Features

- 🌍 **Language Check**: Confirms the site is displayed in Spanish.
- 📰 **Scraping**: Extracts titles, content, and cover images (if available) from the first 5 Opinion articles.
- 🌐 **Translation**: Translates article titles to English using a translation API (e.g., Google Translate or Rapid API).
- 🧠 **Analysis**: Identifies and counts words repeated more than twice in the translated headers.
- 🧪 **Cross-Browser Testing**: Runs tests locally and in **5 parallel threads** on BrowserStack across desktop and mobile browsers.

---

## 🛠️ Tech Stack

- **Python**
- **Selenium WebDriver**
- **BeautifulSoup**
- **Translation API** (Google / Rapid API)
- **BrowserStack** (Parallel automation testing)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/elpais-opinion-scraper.git
