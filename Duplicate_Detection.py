
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from lxml import html
import requests
import tkinter as tk
from functools import partial
def function_des():
    Top.destroy()
    root = tk.Tk()
    def fun(str1,str2):
     #print(str1,str2)
     
     str1_list = word_tokenize(str1)
     str2_list = word_tokenize(str2)
     sw = stopwords.words('english')  
     l1 =[];l2 =[]
     # remove stop words from string
     str1_set = {w for w in str1_list if not w in sw}  
     str2_set = {w for w in str2_list if not w in sw}
     
    # form a set containing keywords of both strings  
     rvector = str1_set.union(str2_set)  
     for w in rvector:
        if w in str1_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in str2_set: l2.append(1)
        else: l2.append(0)
     c = 0

       
    # cosine formula  
     for i in range(len(rvector)):
            c+= l1[i]*l2[i]
     cosine = c / float((sum(l1)*sum(l2))**0.5)
    # print("similarity: ", cosine)
     return cosine
   
    def res(url,class_name):
        root.destroy()
        url1 = (url.get())
        class_name1 = (class_name.get())
        page = requests.get(url1)
        tree = html.fromstring(page.content)
        prices = tree.xpath('//'+class_name1+'[@class="'+class_name1+'"]/text()')
        print('Prices: ')
        #print(prices[0])
        list_20=[]
        list_50=[]
        list_70=[]
        list_100=[]
        for x in prices:
          for y in prices:
            if(x == y):
              continue
            t = fun(x,y)
            t = t*100
            #print(t)
            if(t >= 0 and t <= 25):
              list_20.append(x)
              list_20.append(y)
            if(t > 25 and t <= 50 ):
              list_50.append(x)
              list_50.append(y)  
            if(t > 50 and t <= 70 ):
              list_70.append(x)
              list_70.append(y)
            if(t > 70 and t <= 100 ):
              list_100.append(x)
              list_100.append(y)
        list_20 = list(set(list_20))
        list_50 = list(set(list_50))
        list_70 = list(set(list_70))
        list_100 = list(set(list_100))
        
        root1 = tk.Tk()
        from tkinter import ttk
        container = ttk.Frame(root1)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        ttk.Label(scrollable_frame,text = "Bucket-20").pack()
        for i in list_20:
            ttk.Label(scrollable_frame,text = i).pack()
        ttk.Label(scrollable_frame,text = "Bucket-50").pack()
        for i in list_50:
            ttk.Label(scrollable_frame,text = i).pack()
        ttk.Label(scrollable_frame,text = "Bucket-70").pack()
        for i in list_70:
            ttk.Label(scrollable_frame,text = i).pack()
        ttk.Label(scrollable_frame,text = "Bucket-100").pack()
        for i in list_100:
            ttk.Label(scrollable_frame,text = i).pack()
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        root1.mainloop()

    tk.Label(root,
    text="Enter URL here :  ",
    fg = "red",
    font = "Times").pack()
    url = tk.StringVar()  
    entry = tk.Entry(root, bd =5,textvariable=url)
    entry.pack()
    tk.Label(root,
    text="Enter container/class name  here :  ",
    fg = "red",
    font = "Times").pack()
    class_name = tk.StringVar()  
    entry = tk.Entry(root, bd =5,textvariable=class_name)
    entry.pack()
    res = partial(res, url,class_name)
    button = tk.Button(root, text='Next', width=25,command=res)
    button.pack()

     

    root.mainloop()
Top=tk.Tk()
tk.Label(Top,
text="WELCOME!!!!",
fg = "red",
font = "Times").pack()
tk.Label(Top,
text="Find your duplicate questions here",
fg = "red",
font = "Helvetica 16 bold italic").pack()


button = tk.Button(Top, text='Start', width=25, command=function_des)
button.pack()

Top.mainloop()
#Top.destroy()