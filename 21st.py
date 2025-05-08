import sys
import time
import random
import os
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

# ANSI simulation as HTML
BLUE = "<span style='color:#3399FF'>"
ORANGE = "<span style='color:#FFA500'>"
GREEN = "<span style='color:#00FF00'>"
YELLOW = "<span style='color:#FFFF00'>"
RED = "<span style='color:#FF5555'>"
WHITE = "<span style='color:#FFFFFF'>"
RESET = "</span>"

# Countdown target
target_date = datetime(2025, 9, 21, 0, 0, 0)

class MurinApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("21st September")
        self.setGeometry(520, 90, 720, 920)

        # Layouts
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Terminal-like area
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setLineWrapMode(QTextEdit.NoWrap)
        self.terminal.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.terminal.setStyleSheet("""
            background-color: black;
            color: white;
            font-family: Courier;
            font-size: 15px;
            padding-bottom: 20px;
        """)
        self.layout.addWidget(self.terminal)

        # Buttons
        button_layout = QHBoxLayout()
        self.mute_button = QPushButton("🔇 Mute")
        self.exit_button = QPushButton("❌ Chiudi")
        button_layout.addWidget(self.mute_button)
        button_layout.addWidget(self.exit_button)
        self.layout.addLayout(button_layout)

        # Media Player
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        mp3_path = os.path.join(base_path, "september.mp3")

        self.player.setSource(QUrl.fromLocalFile(mp3_path))
        self.audio_output.setVolume(0.5)
        self.player.setLoops(-1)

        # Events
        self.exit_button.clicked.connect(self.close)
        self.mute_button.clicked.connect(self.toggle_mute)

        # Launch sequence
        self.glitch_messages = [
            "Initializing DaFister Subsystem...<br>",
            "Decrypting Rizz Layers...<br>",
            "[ ERR ] Harem Detected! Stabilizing...<br>",
            "Compiling 21st Protocol - Phase 1...<br>",
            "Injecting Gonathon with a Gi Engine...<br>",
            "Aligning with Shoebox Coordinates...<br>",
            "Loading September Eternity Core...<br>",
            "[ ERR ] New boat found! Action prepared...<br>",
            "BOAT GOES BINTED..<br>"
        ]
        self.glitch_index = 0
        self.glitch_timer = QTimer()
        self.glitch_timer.timeout.connect(self.show_glitch)
        self.glitch_timer.start(1200)

    def toggle_mute(self):
        if self.audio_output.volume() > 0:
            self.audio_output.setVolume(0)
            self.mute_button.setText("🔊 Unmute")
        else:
            self.audio_output.setVolume(0.5)
            self.mute_button.setText("🔇 Mute")

    def show_glitch(self):
        if self.glitch_index < len(self.glitch_messages):
            garbage = ''.join(random.choice("▒░▓█▌▐▄▀■¤Ø#%&$@¥") for _ in range(50))
            self.terminal.append(f"{RED}{garbage}{RESET}")
            msg = self.glitch_messages[self.glitch_index]
            prefix = "<br>[ OK ]" if not msg.startswith("[ ERR ]") else "<br>[ ERR ]"
            color = GREEN if prefix == "<br>[ OK ]" else RED
            clean_msg = msg.replace("[ ERR ] ", "")
            self.terminal.append(f"{color}{prefix}{RESET} {clean_msg}")
            self.glitch_index += 1
        else:
            self.glitch_timer.stop()
            self.show_ready()

    def show_ready(self):
        self.terminal.append(f"\n{ORANGE}[ READY ]{RESET} <b><span style='text-decoration:blink;'>GIGI SYSTEM ONLINE</span></b>\n")

        # Attendi 3 secondi (3000 ms) prima di mostrare il countdown
        QTimer.singleShot(3000, self.start_countdown)

    def start_countdown(self):
        self.show_countdown_block()
        self.player.play()
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)


    def get_remember_ascii(self):
        return """<pre style='color:lime'>
________           _____.___.                                             
\______ \   ____   \__  |   | ____  __ __                                 
 |    |  \ /  _ \   /   |   |/  _ \|  |  \                                
 |    `   (  <_> )  \____   (  <_> )  |  /                                
/_______  /\____/   / ______|\____/|____/                                 
        \/          \/                                                    
__________                             ___.                ._._________._.
\______   \ ____   _____   ____   _____\_ |__   ___________| |\_____   \ |
 |       _// __ \ /     \_/ __ \ /     \| __ \_/ __ \_  __ \ |   /   __/ |
 |    |   \  ___/|  Y Y  \  ___/|  Y Y  \ \_\ \  ___/|  | \/\|  |   |   \|
 |____|_  /\___  >__|_|  /\___  >__|_|  /___  /\___  >__|   __  |___|   __
        \/     \/      \/     \/      \/    \/     \/       \/  <___>   \/
</pre>"""  

    def get_gigi_ascii(self):
        return """<pre style='color:#FFA500'>
                    XXXX$$$$$
                  XXXX&      X
                XXXXX$        $
               $XXXXX
                $$$XX         +;;
                  $$$   x+++++++++;;;
        +;;;;;;;;  XX+xx;;;;;;;;++++++++    ;;;;;;+++
        X+;;;;;;;;++;+++;;;;;;;;;;+++++++x++;;+++++xX
        XX+;;;+++++;;;$$+;;;;;;;;++++++++++++++++XXX$$
        $XX++;;++;;;;;;;;;;;;;;+++X$$$X$$+xx+++++XxXX+
        XXXX++++;;;;;;;;;;;;++++++++X$$$X+;+x++++XXXX
       XXXXXx++;;+;;;;;;;++++++++++$$$xX$$;;;++++XXXX$
   X  $$$XX$X+++;;;X;;;;;+++++++;+++x++::::;++++X$X$$ $
    :::xXXXX$x+;;+::++;;;+++xxx++++x+;++;; ..++xX$XXX+:;;+
     +XXXX$X+x;;;::+;;x+;++;xx+xxxXXXX;X;;;;+++X$$XXXX;+X
 X+;+X:XX;;::;:;;:;x;;::;x+;;;.;+;+X+x$X$x+++++++;XXxX+;::+X
   ;:+XX;;;;;:+;:;Xx:;;;+;;:.;.:;;+X++xx$$+;;+++x+:+;;X+:;
   ;:;:+:;::::;;X$x+;;+.x+x:..:..:++x.X+$$X+;++;x+;x::;:::
   ;;;     +:;:XXXX;:;:::;;...:..:;;:;+XXX$Xxx;;;x$    ;:;
    X      ;+:;XXXX;;+;::::...::::::;+XxXXXXXX;;;;     +++
          X;:;XXXXX;;++x....::.::.:;:xXXXXXXXx;+:;+
          +++;XXXXXx;XxXXX:.......:xXXXXXXXXXX:+;:;
         X+x++++xXXX;XXXXXXX+;:;+XXXXXXXXXXXx;+++;
          +xxX+++;;+::;;;;;XXXXXXX;;;;++++;++++X$&&
         $++;$&$$$$x;;;::::;;;:;;+::::::;x$$$$$$$$&&
         +x++X&$$XX$$$X;;;;;;:::::;;;;X$$$$$$$$$$$$&
        +x++++&$$$$$$$$$Xx;+;;;;;;+xX$$$$$$$$$$$$$&
        +++;+;$$$$$$XXx++++XXXXXXX++;+XXXX$$$$$$$$
</pre>"""

    def show_countdown_block(self):
        remember_ascii = self.get_remember_ascii()
        signature = "<div style='color:lime; font-size:13px;'>by TheNiYu – instagram – tiktok @niyuthe</div>"
        ascii_art = self.get_gigi_ascii()
        spacer = "&nbsp;" * 14
        html = (
            
            f"{remember_ascii}"

            f"{signature}"
            f"{ascii_art}<br><br>"
            f"{spacer}{ORANGE}Calculating time remaining...{RESET}"
        )
        self.terminal.setHtml(html)

    def update_countdown(self):
        now = datetime.now()
        delta = target_date - now

        if delta.total_seconds() <= 0:
            self.terminal.setHtml("🎉 IT'S THE 21st OF SEPTEMBER! DO YOU REMEMBER?!?")
            self.countdown_timer.stop()
            return

        days = delta.days
        hours, rem = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        remember_ascii = self.get_remember_ascii()
        signature = "<div style='color:lime; font-size:13px;'>by TheNiYu – instagram – tiktok @niyuthe</div>"
        ascii_art = self.get_gigi_ascii()

        spacer = "&nbsp;" * 8
        countdown_block = (f"{spacer}{BLUE}{days:02}{GREEN} days, "
                           f"{YELLOW}{hours:02}{GREEN} hours, "
                           f"{RED}{minutes:02}{GREEN} minutes, "
                           f"{WHITE}{seconds:02}{GREEN} seconds left<br><br>{RESET}")

        html = (
            f"{remember_ascii}"
            f"{signature}"
            f"{ascii_art}<br><br>"
            f"{countdown_block}"
        )
        self.terminal.setHtml(html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MurinApp()
    window.show()
    sys.exit(app.exec())
