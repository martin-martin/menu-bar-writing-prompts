#from datetime import datetime
import webbrowser
import rumps


class WritingPromptApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Writing Prompts",
            "morning": "🌤 Morning",
            "evening": "🌙 Evening",
            "write": "📃 750 Words",
            "base_url": "https://write-750.herokuapp.com/",
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        # TODO: could refactor to bring up different prompts depending on the time of day with datetime.now()
        self.morning = rumps.MenuItem(title=self.config["morning"], callback=self.open_morning_pages)
        self.evening = rumps.MenuItem(title=self.config["evening"], callback=self.open_evening_pages)
        self.write = rumps.MenuItem(title=self.config["write"], callback=self.open_750_words)
        self.app.menu = [self.morning, self.evening, self.write]

    def set_up_menu(self):
        self.app.title = "✏️"

    def open_morning_pages(self, sender):  # sender needs to be passed even if it's not used explicitly
        rumps.notification(title=self.config["app_name"], subtitle=self.config["morning"], message='Time to write')
        webbrowser.open(self.config["base_url"] + "write/morning")

    def open_evening_pages(self, sender):
        rumps.notification(title=self.config["app_name"], subtitle=self.config["evening"], message='Time to write')
        webbrowser.open(self.config["base_url"] + "write/evening")

    def open_750_words(self, sender):
        rumps.notification(title=self.config["app_name"], subtitle=self.config["write"], message='Time to write')
        webbrowser.open(self.config["base_url"] + "canvas")

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = WritingPromptApp()
    app.run()
