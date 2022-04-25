from tkinter import *
from PIL import ImageTk,Image
from Graphs import *
from Floyd import *


root = Tk()
root.title('Gdelivery')
root.geometry('800x600')
root.config(background = 'black')
root.resizable(width = False, height = False)
root.iconbitmap('assets/delivey.ico')

imag_1 = PhotoImage(file= "assets/backgroundDelivery.png")
imag_2 = PhotoImage(file = "assets/Va_va_land_city.png")
imag_3 = PhotoImage(file = "assets/va_va_land_city.png")
imag_4 = PhotoImage(file = "assets/Va_va_land_nodes_km.png")

imageList = [imag_1, imag_2, imag_3, imag_4]

# Imagem de fundo
background = Label(image=imag_1)
background.grid(row = 0, column = 0, columnspan = 3)
#background.place(x=0,y=0, relwidth=1,relheight=1)

def show_map():
    global background
    background.grid_forget()
    background = Label(image=imag_2)
    background.grid(row = 1, column = 0, columnspan = 3)

    button_back = Button(root,text='Back',padx=117,pady=5,fg='snow',bg='black',command=back)
    button_back.place(relx=0.5,rely=0.9,anchor=CENTER)

def show_path():
    # graph = init_graph()

    # path = BFS_short_path(graph, '16')
    # print(path)

    global background
    global e
    background.grid_forget()
    background = Label(image=imag_3)
    background.grid(row = 1, column = 0, columnspan = 3)

    e = Entry(root, width=15, bg="#1B1918", fg = "snow")
    e.place(relx=0.92,rely=0.9,anchor=CENTER)

    button_enter = Button(root,text='Buscar',padx=30,pady=5,fg='snow',bg='black',command=show_small_path)
    button_enter.place(relx=0.92,rely=0.95,anchor=CENTER)

    button_back = Button(root,text='Back',padx=30,pady=5,fg='snow',bg='black',command=back)
    button_back.place(relx=0.075,rely=0.05,anchor=CENTER)

def show_small_path():

    global background
    global e
    background.grid_forget()
    background = Label(image=imag_4)
    background.grid(row = 1, column = 0, columnspan = 3)

    goal = e.get()
    #print(goal)
    
    graph = init_graph()
    path = dijkstra(graph, goal)
    #print(path)

    button_back = Button(root,text='Back',padx=30,pady=5,fg='snow',bg='black',command=back)
    button_back.place(relx=0.075,rely=0.05,anchor=CENTER)

    text=Text(root, width=20, height=10,fg='snow',bg='black')
    text.place(relx=0.5,rely=0.625,anchor=CENTER)
    text.insert(END, 'Menor Caminho:\n')

    for day in path:
        if int(day) < 50 :
            text.insert(END, day + '\n')
        else:
            dis = float(day)/100
            text.insert(END,'Distância:' + str(dis) + ' Km\n')

    # MyLabel = Label(root, text="Menor Caminho encontrado:  " + str(path),padx=30,pady=5,fg='snow',bg='black')
    # MyLabel.place(relx=0.5,rely=0.9,anchor=CENTER)

    # for i in range(len(path)):
    #     exec('Label%d=Label(root,text="%s")\nLabel%d.pack()' % (i,path[i],i))

def back():
    
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row = 0, column = 0, columnspan = 3)

    butaoNew = Button(root, text='Visualizar Mapa',padx=85,pady=5,fg='snow',bg='black',command = show_map)
    butaoNew.place(relx=0.5,rely=0.1,anchor=CENTER)

    butaoPvP = Button(root,text='Calcular Rota',padx=90,pady=5,fg='snow',bg='black',command = show_path)
    butaoPvP.place(relx=0.5,rely=0.2,anchor=CENTER)

    butaoExit = Button(root,text='SAIR',padx=117,pady=5,fg='snow',bg='black',command=root.quit)
    butaoExit.place(relx=0.5,rely=0.5,anchor=CENTER)
   

# Butões do Menu
butaoNew = Button(root, text='Visualizar Mapa',padx=85,pady=5,fg='snow',bg='black',command = show_map)
butaoNew.place(relx=0.5,rely=0.1,anchor=CENTER)

butaoPvP = Button(root,text='Calcular Rota',padx=90,pady=5,fg='snow',bg='black',command = show_path)
butaoPvP.place(relx=0.5,rely=0.2,anchor=CENTER)

butaoExit = Button(root,text='SAIR',padx=117,pady=5,fg='snow',bg='black',command=root.quit)
butaoExit.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()