import customtkinter
import os
import tkinter
from tkinter import *


# App for managing your PC
class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()

        customtkinter.set_appearance_mode("dark")

        self.geometry("300x200+750+350")

        self.resizable(
            width=False,
            height=False
        )

        self.title("PC manager")

        self.off = customtkinter.CTkButton(
            self,
            text="Turn off PC",
            text_color="yellow",
            border_width=2,
            border_color="yellow",
            width=290,
            height=90,
            command=self.turnoff
        )

        self.off.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )

        self.rest = customtkinter.CTkButton(
            self,
            text="Restart PC",
            text_color="yellow",
            border_width=2,
            border_color="yellow",
            width=290,
            height=90,
            command=self.restart
        )

        self.rest.grid(
            column=0,
            row=1,
            padx=5,
            pady=3
        )

    @staticmethod
    def turnoff():
        os.system("shutdown /s /t 0")

    @staticmethod
    def restart():
        os.system("shutdown /r /t 0")


if __name__ == "__main__":
    app = App()
    app.mainloop()
