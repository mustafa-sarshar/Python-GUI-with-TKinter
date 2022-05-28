"""
Source: https://www.youtube.com/watch?v=wRx3_4JR6Ss&ab_channel=SubhranilSarkar
"""
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from libs.screens.home_page import HomePage

class InstagramApp(MDApp):
    def build(self):
        Window.size = (300, 600)
        self.load_all_kv_files()
        # return super().build()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file("libs/screens/home_page.kv")
        Builder.load_file("libs/components/appbar.kv")
        Builder.load_file("libs/components/story_creator.kv")

if __name__ == "__main__":
    InstagramApp().run()