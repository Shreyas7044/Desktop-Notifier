import time
import notify2
from topnews import topStories

# Replace this with the full path to your icon image
ICON_PATH = "/full/path/to/icon.png"

# Fetch news items
newsitems = topStories()

# Initialize the notification system
notify2.init("News Notifier")

# Create notification object
notification = notify2.Notification(None, icon=ICON_PATH)

# Set urgency and timeout
notification.set_urgency(notify2.URGENCY_NORMAL)
notification.set_timeout(10000)

# Display notifications
for news in newsitems:
    notification.update(news.get('title', 'News Update'),
                        news.get('description', ''))
    notification.show()
    time.sleep(15)