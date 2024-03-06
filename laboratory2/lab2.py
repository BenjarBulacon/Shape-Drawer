import tkinter as tk
 

class ShapeDrawer:
    def __init__(self, master):
        self.master = master
        self.master.title("Shape Drawer")

        self.canvas = tk.Canvas(self.master, width=900, height=600, bg="grey")
        self.canvas.pack()

        self.shapeType = tk.StringVar()
        self.shapeType.set("Rectangle")
        self.shapeMenu = tk.OptionMenu(self.master, self.shapeType, "Rectangle", "Circle", "Line", "Triangle", "Square")
        self.shapeMenu.pack()

        self.colorLabel = tk.Label(self.master, text="Color:")
        self.colorLabel.pack()
        self.colorEntry = tk.Entry(self.master)
        self.colorEntry.pack()

        self.drawButton = tk.Button(self.master, text="Draw", command=self.drawShape)
        self.drawButton.pack()

        self.selectedShape = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<Button-1>", self.startShape)
        self.canvas.bind("<B1-Motion>", self.drawTempShape)
        self.canvas.bind("<ButtonRelease-1>", self.endShape)

    def startShape(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drawTempShape(self, event):
        if self.selectedShape:
            self.canvas.delete(self.selectedShape)
            if self.shapeType.get() == "Rectangle":
                self.selectedShape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="black")
            elif self.shapeType.get() == "Circle":
                self.selectedShape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline="black")
            elif self.shapeType.get() == "Line":
                self.selectedShape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill="black")
                
            elif self.shapeType.get() == "Triangle":
                self.selectedShape = self.canvas.create_polygon(self.start_x, event.y, event.x, event.y, (self.start_x + event.x) // 2, self.start_y, outline="black")
            elif self.shapeType.get() == "Square":
                self.selectedShape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="black")

    def endShape(self, event):
        if self.selectedShape:
            self.canvas.delete(self.selectedShape)
            if self.shapeType.get() == "Rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="black", fill=self.colorEntry.get())
            elif self.shapeType.get() == "Circle":
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline="black", fill=self.colorEntry.get())
            elif self.shapeType.get() == "Line":
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.colorEntry.get())
            elif self.shapeType.get() == "Triangle":
                self.canvas.create_polygon(self.start_x, event.y, event.x, event.y, (self.start_x + event.x) // 2, self.start_y, outline="black", fill=self.colorEntry.get())
            elif self.shapeType.get() == "Square":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="black", fill=self.colorEntry.get())

    def drawShape(self):
        if self.shapeType.get() == "Rectangle":
            self.selectedShape = self.canvas.create_rectangle(50, 50, 150, 100, outline="black", fill=self.colorEntry.get())
        elif self.shapeType.get() == "Circle":
            self.selectedShape = self.canvas.create_oval(50, 50, 150, 100, outline="black", fill=self.colorEntry.get())
        elif self.shapeType.get() == "Line":
            self.selectedShape = self.canvas.create_line(50, 50, 150, 100, fill=self.colorEntry.get())
        elif self.shapeType.get() == "Triangle":
            self.selectedShape = self.canvas.create_polygon(50, 50, 100, 150, 150, 50, outline="black", fill=self.colorEntry.get())
        elif self.shapeType.get() == "Square":
            self.selectedShape = self.canvas.create_rectangle(50, 50, 150, 150, outline="black", fill=self.colorEntry.get())

def main():
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
