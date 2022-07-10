from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from fileShare import FileSharer
from kivy.core.clipboard import Clipboard
import time
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        """Start camera and changes Button test"""
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        """ Creates a file name with the surrent time and captures and saves a photo image that file name  """
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message = 'Create a link First'
    def create_link(self):
        """Access the photo filepath, uploads it to the web and inserts the link in the Label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileShare = FileSharer(filepath=file_path)
        self.url = fileShare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy Link to the clipboard available for pasting"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message
    def open_link(self):
        """ Open Link with default browser """
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text= self.link_message




class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
