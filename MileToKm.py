
#first import the tkinter module
import tkinter as tk
#then import the ttk module from tkinter
from tkinter import ttk
#pip innstall ttkbootstrap
#this is that lets us style
import ttkbootstrap as ttk

#here we will create a window
#window = tk.Tk()
#this is how we creat a window with style to it
window = ttk.Window(themename = "darkly")
#here we will be giving the window a title
window.title("Miles --> Kilometers")
#here is the size of the window the formate inside the () is ("widthxheight")
window.geometry("300x150")


#now the first widget we are creating a widget label
#this master is where its going to be placed
#the text is what the label will say
#the font is what the font will be including the size and if its bold or not
title_label = ttk.Label(master = window, text = "Miles --> Kilometers", font = "Times 20 bold")
#this is how we pack the label into the window
title_label.pack()

#math functions
def convert():
    #first we want to get the value from the entry widget(number we entered)
    mile_input = entry_int.get()
    km_output = mile_input * 1.60934
    #this is where output the final results
    output_string.set(km_output)


#now we are going to create a entry widget
#this is where the user will input the data
#and we want it inside the window
input_frame = ttk.Frame(master = window)
#this is basically a seperate variable that will hold the value of the entry
entry_int = tk.IntVar()
#for the entry button this will be in the input frame
#text variable basically means that the value of the entry will be stored in entryInt
entry = ttk.Entry(master = input_frame, textvariable= entry_int)
#this is also in the input frame and then for the text inside the button it will say convert
#the command goes to our function that we created
button = ttk.Button(master= input_frame, text = "Convert", command = convert)
#this is how we put it on the input frame and to move the button to the left side
#if you want to add space between the button and the entry you can add padx = 10
entry.pack(side = "left")
button.pack()
#this is how we pack the input frame into the window
#if you want to add space between the input frame and the title label you can add pady = 10
input_frame.pack(pady = 10)

#output frame
#this basically stores thes tring
output_string = tk.StringVar()
#text variable overrides what the text says and makes it the value of the string
output_frame = ttk.Label(master = window, text = "output", font = "Times 20 bold", textvariable = output_string)
output_frame.pack()
#this is what lets the window actually run
window.mainloop()