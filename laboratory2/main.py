from tkinter import *
from shapes import *
from edit.delete import ShapeDeleter
from save.openFile import ProjectOpener
from save.saveFile import ProjectSaver



def pick_color():
    if Global.shape is None:
        return 
    Global.shape.change_color()

def size_shape(event):
    if Global.resize is None:
        return
    Global.resize.resize_shape(event)

def Move_Zome(event):
    if Global.move_and_zome is None:
        return
    Global.move_and_zome.start_move(event)  

def save_proj():
    Save_project.save_project()

def open_project():
    openFile.open_project() 




window = Tk()
window.title("Shapes Drawer")

frame = Frame(window)
frame.pack(fill=BOTH, expand=True)

menubar = Menu(window)
window.config(menu=menubar)

shapesMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Shape", menu = shapesMenu)
shapesMenu.add_command(label="Square", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: square_drawer.draw_shape(event)))
shapesMenu.add_command(label="Rectangle", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: rectangle_drawer.draw_shape(event)))
shapesMenu.add_command(label="Circle", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: circle_drawer.draw_shape(event)))
shapesMenu.add_command(label="Triangle", command=lambda: canvas.bind('<ButtonPress-1>', lambda event: triangle_drawer.draw_shape(event)))
shapesMenu.add_separator()
shapesMenu.add_command(label="Exit")

file_menu = Menu(menubar, tearoff=0,bg='#ffffff',fg='#000000')
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=  open_project)
file_menu.add_command(label='Save As', command= save_proj)

canvas = Canvas(frame, width=600, height=400, bg='grey')
canvas.pack(fill=BOTH, expand=True)


selected_shape = None

circle_drawer = CircleDrawer(canvas)
square_drawer = SquareDrawer(canvas)
triangle_drawer =TriangleDrawer(canvas)
shape_deleter = ShapeDeleter(canvas)
rectangle_drawer = RectangleDrawer(canvas)

Save_project =  ProjectSaver(canvas)
openFile = ProjectOpener(canvas)




window.bind('<BackSpace>', shape_deleter.delete_last_shape)
window.bind('<KeyPress-Up>',size_shape)
window.bind('<KeyPress-Down>',size_shape)
window.bind('<KeyPress-Left>',size_shape)
window.bind('<KeyPress-Right>',size_shape)
window.bind('<ButtonPress-3>', Move_Zome)  



window.mainloop()