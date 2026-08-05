from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from gtts import gTTS
import os
class ManouApp(App):
    def build(self):
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title_label = Label(
            text="Advanced AI Voice & Art Assistant",
            font_size=20,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title_label)
        
        # Input Field
        self.input_field = TextInput(
            text='',
            hint_text='Enter text here (Voice message or Art prompt)...',
            size_hint_y=None,
            height=100,
            multiline=True
        )
        layout.add_widget(self.input_field)
        
        # Voice Button
        btn_voice = Button(
            text='1. Run Voice Assistant',
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        btn_voice.bind(on_press=self.on_voice_click)
        layout.add_widget(btn_voice)
        
        # Art Button
        btn_image = Button(
            text='2. Generate AI Image',
            size_hint_y=None,
            height=60,
            background_color=(0.8, 0.4, 0.1, 1)
        )
        btn_image.bind(on_press=self.on_image_click)
        layout.add_widget(btn_image)
        
        # Status Label
        self.status_label = Label(
            text='Status: Ready',
            font_size=16,
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        return layout

    def on_voice_click(self, instance):
        message = self.input_field.text.strip()
        if not message:
            message = "Hello! Welcome to Manou Assistant."
        
        self.status_label.text = "[Voice]: Processing audio..."
        try:
            tts = gTTS(text=message, lang='en', slow=False)
            audio_file = "assistant_voice.mp3"
            tts.save(audio_file)
            self.status_label.text = f"Success: Audio saved as {audio_file}"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

    def on_image_click(self, instance):
        prompt = self.input_field.text.strip()
        if not prompt:
            prompt = "A futuristic cyberpunk cityscape"
            
        self.status_label.text = f"[Art]: Processing prompt...\n'{prompt}'"

if __name__ == '__main__':
    ManouApp().run()
