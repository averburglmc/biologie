from src.pages.base_page import *
from tkinter import *

class DnaPage(BaseFrame):
    chromosome = None

    previous_value = ""

    def __init__(self, root, controller, chromosome):
        super().__init__(root, controller)

        self.chromosome = chromosome

        self.reset()
        
    def reset(self):
        self.canvas.delete("all")

        self.locus = self.chromosome.get_random()

        self.init_widgets()

    def init_widgets(self):
        current_y = 25

        self.background = PhotoImage(file="src/images/dna.png")
        self.canvas.create_image(0, 0, image=self.background, anchor=NW)

        for locus in self.chromosome.loci:
            if locus == self.locus:
                self.canvas.create_rectangle(250, current_y, 550, current_y + 250, outline="black", width=4, fill=locus.color)
                        
                self.canvas.create_text(260, current_y + 10, text="allel_x", fill="#444444", font=("Times", 12), anchor=NW)
                self.canvas.create_text(260, current_y + 25, text=locus.allel_x, fill="#444444", font=("Times", 24), anchor=NW)
                self.canvas.create_text(540, current_y + 10, text="allel_y", fill="#444444", font=("Times", 12), anchor=NE)
                self.canvas.create_text(540, current_y + 25, text=locus.allel_y, fill="#444444", font=("Times", 24), anchor=NE)
                self.canvas.create_text(400, current_y + 10, text="heterozygoot", fill="#888844", font=("Times", 12), anchor=N)
                self.canvas.create_text(400, current_y + 25, text=locus.name, fill="#888844", font=("Times", 24), anchor=N)

                self.input = Text(self.canvas, background="#333333", foreground="#DDDDDD")
                self.input.insert("1.0", self.locus.code)
                self.input.bind("<KeyRelease>", self.code_changed)

                self.previous_value = self.locus.code

                self.button = Button(self.canvas, text="Send!", command=self.send)

                self.canvas.create_window(400, current_y + 162.5, window=self.input, width=300, height=175)
                self.canvas.create_window(400, current_y + 237.5, window=self.button, width=300, height=25)

                current_y += 275
            else:
                self.canvas.create_rectangle(250, current_y, 550, current_y + 75, outline="black", width=4, fill=locus.color)
                self.canvas.create_text(260, current_y + 10, text="allel_x", fill="#444444", font=("Times", 12), anchor=NW)
                self.canvas.create_text(260, current_y + 25, text=locus.locus, fill="#444444", font=("Times", 24), anchor=NW)
                self.canvas.create_text(540, current_y + 10, text="allel_y", fill="#444444", font=("Times", 12), anchor=NE)
                self.canvas.create_text(540, current_y + 25, text=locus.locus, fill="#444444", font=("Times", 24), anchor=NE)
                self.canvas.create_text(400, current_y + 10, text="homozygoot", fill="#444444", font=("Times", 12), anchor=N)
                self.canvas.create_text(400, current_y + 25, text=locus.name, fill="#444444", font=("Times", 24), anchor=N)

                current_y += 100


    def code_changed(self, event):
        value = self.input.get("1.0", END)

        if len(value) > self.chromosome.get(INTELLECT).locus + 1:
            self.input.delete("1.0", END)
            self.input.insert(END, self.previous_value)
        else:
            self.previous_value = value
            self.locus.code = value

    def send(self):
        executed = self.locus.run()
        if executed:
            self.input.unbind("<KeyRelease>")
            self.controller.level += 1
            self.controller.to_page(1)