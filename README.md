# Desktop News Notifier in Python

A Desktop Notifier application built using Python that fetches top news headlines from an RSS feed and displays them as real-time desktop notifications.

---

## 📌 Features
- Fetches live news headlines using RSS
- Parses XML data in Python
- Displays system notifications
- Customizable notification urgency and timeout

---

## 🛠️ Technologies Used
- Python
- requests
- notify2
- XML Parsing

---

## 📂 Project Structure
python-desktop-news-notifier/
├── main.py
├── topnews.py
├── requirements.txt

---

## ▶️ How It Works
- topnews.py fetches top news headlines from Hindustan Times RSS feed.
- XML data is parsed using xml.etree.ElementTree.
- main.py initializes a D-Bus connection using notify2.
- Each news headline is displayed as a desktop notification every 15 seconds.

---

## 🔔 Notification Configuration
- Urgency Levels
- URGENCY_LOW
- URGENCY_NORMAL
- URGENCY_CRITICAL

---

## 📌 Notes
- Ensure D-Bus is running on your system.
- Update the ICON_PATH in main.py with a valid image path.
