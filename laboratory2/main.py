from tkinter import *
from shapes import *
from edit.delete import ShapeDeleter
from save.openFile import ProjectOpener
from save.saveFile import ProjectSaver



def colorPicker():
    if Global.shape is None:
        return 
    Global.shape.change_color()

def shapeSize(event):
    if Global.resize is None:
        return
    Global.resize.resize_shape(event)

def MoveAndZoom(event):
    if Global.move_and_zome is None:
        return
    Global.move_and_zome.start_move(event)  

def saveProject():
    Save_project.save_project()

def openProject():
    openFile.open_project() 




window = Tk()
window.title("Shapes Drawer")

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

menubar = Menu(window)
window.config(menu=menubar)

shapesMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Shape", menu = shapesMenu)
shapesMenu.add_command(label="Square", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: squareDrawer.draw_shape(event)))
shapesMenu.add_command(label="Rectangle", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: rectangleDrawer.draw_shape(event)))
shapesMenu.add_command(label="Circle", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: circleDrawer.draw_shape(event)))
shapesMenu.add_command(label="Triangle", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: triangleDrawer.draw_shape(event)))
shapesMenu.add_separator()
shapesMenu.add_command(label="Exit")

file_menu = Menu(menubar, tearoff=0,bg='#ffffff',fg='#000000')
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=  openProject)
file_menu.add_command(label='Save As', command= saveProject)

canvas = Canvas(frame, width=600, height=400, bg='grey')
canvas.pack(fill=BOTH, expand=True)


selected_shape = None

circleDrawer = CircleDrawer(canvas)
squareDrawer = SquareDrawer(canvas)
triangleDrawer =TriangleDrawer(canvas)
shapeDeleter = ShapeDeleter(canvas)
rectangleDrawer = RectangleDrawer(canvas)

Save_project =  ProjectSaver(canvas)
openFile = ProjectOpener(canvas)




window.bind('<BackSpace>', shapeDeleter.delete_last_shape)
window.bind('<KeyPress-Up>',shapeSize)
window.bind('<KeyPress-Down>',shapeSize)
window.bind('<KeyPress-Left>',shapeSize)
window.bind('<KeyPress-Right>',shapeSize)
window.bind('<ButtonPress-3>', MoveAndZoom)  



window.mainloop()
