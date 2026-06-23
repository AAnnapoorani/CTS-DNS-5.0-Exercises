class EmailNotifier:
    def send(self):
        print("Email Notification Sent")

class SMSNotifier:
    def __init__(self, notifier):
        self.notifier = notifier
    def send(self):
        self.notifier.send()
        print("SMS Notification Sent")

class SlackNotifier:
    def __init__(self, notifier):
        self.notifier = notifier
    def send(self):
        self.notifier.send()
        print("Slack Notification Sent")

notification = EmailNotifier()
notification = SMSNotifier(notification)
notification = SlackNotifier(notification)
notification.send()