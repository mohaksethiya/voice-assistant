from customtkinter import *
import threading
import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from response import gen_output


BACKGROUND = "#636363"
CANVAS_COLOR = "#82aba0"
TEXT_COLOR = "#f6d38e"
BUTTON_COLOR = "#737c96"
BUTTON_ON_COLOR = "#62cb66"
BUTTON_OFF_COLOR = "#C64E4E"
TEXT_BOX_COLOR = "#000000"
TEXT_BOX_TEXT_COLOR = "#ffffff"
FONT = ("Arial", 16, "normal")
OUT_FONT = ("Arial", 20, "normal")
MIC_ON = False

class AppUi:
    def __init__(self):
        self.model = Model("vosk-model-small-en-us-0.15")
        self.q = queue.Queue()

        self.stream = None
        self.listening = False

        self.payload = {}

        self.window = CTk()
        self.window.title("Tars")
        self.window.configure(width=1000, height=750, fg_color=BACKGROUND)

        self.text_box = CTkTextbox(self.window, width=600, height=64, fg_color=TEXT_BOX_COLOR,
                                 text_color=TEXT_BOX_TEXT_COLOR, corner_radius=10, activate_scrollbars=True, wrap="word",
                                   border_width=0, font=FONT, border_spacing=0)
        self.text_box.place(x=100, y=663)

        self.mic_button = CTkButton(self.window, text="Mic", command=self.toggle_mic, width=54, height=54,
                                    fg_color=BUTTON_OFF_COLOR, text_color="black", corner_radius=10, border_width=0,
                                    bg_color=BACKGROUND)
        self.mic_button.place(x=710, y=670)

        self.enter_button = CTkButton(self.window, text="Enter", command=self.upload_input, width=96, height=54,
                                      fg_color=BUTTON_COLOR, text_color="black", corner_radius=10, border_width=0,
                                      bg_color=BACKGROUND)
        self.enter_button.place(x=773, y=670)

        self.out_text = CTkTextbox(self.window, state="disable", width=900, height=600, fg_color=CANVAS_COLOR,
                                   text_color=TEXT_COLOR, font=OUT_FONT, corner_radius=10,
                                   activate_scrollbars=True, wrap="word", border_width=0, border_spacing=0)
        self.out_text.place(x=45, y=50)

    def toggle_mic(self):
        global MIC_ON
        if not MIC_ON:
            MIC_ON = True
            self.mic_button.configure(fg_color=BUTTON_ON_COLOR)
            self.turn_on_mic()
            return
        if MIC_ON:
            MIC_ON = False
            self.mic_button.configure(fg_color=BUTTON_OFF_COLOR)
            self.turn_off_mic()
            return

    def upload_input(self):
        data = gen_output(text=self.text_box.get(index1="1.0", index2=END))
        self.out_text.configure(state="normal")
        output = data["steps"][1]["content"][0]["text"]
        self.out_text.insert("end", text=f"{output}\n")

    def update_textbox(self, text):
        self.text_box.insert("end", text=f"{text} ")

    def run(self):
        self.window.mainloop()

    # ---------------- VOSK ---------------- #

    def callback(self, indata, frames, time, status):
        self.q.put(bytes(indata))

    def listen(self):
        recognizer = KaldiRecognizer(self.model, 16000)

        while self.listening:
            data = self.q.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result["text"]

                if text:
                    self.update_textbox(text)

    def turn_on_mic(self):
        if self.listening:
            return

        self.listening = True

        # Clear old audio
        while not self.q.empty():
            self.q.get()

        self.stream = sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self.callback,
        )

        self.stream.start()

        threading.Thread(target=self.listen, daemon=True).start()

    def turn_off_mic(self):
        if not self.listening:
            return

        self.listening = False

        if self.stream is not None:
            self.stream.stop()
            self.stream.close()
            self.stream = None

    #------------Vosk Done---------------#
