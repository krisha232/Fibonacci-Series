from tkinter import*

root=Tk()
root.title("Fibonacci Series")
root.geometry("400x400")


label_series=Label(root,text="Fibonacci Series")
label_flower=Label(root)
label_spiral=Label(root)

def Fibonacci():
    first_no=0
    second_no=1
    sum=0
    i=1
    
    while(i<=10):
        label_series["text"]+= str(sum)+  " "
        i=i+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
    label_flower["text"]="Flower is fully bloomed"
    label_spiral["text"]="Spiral in right direction are "+ str(first_no) + "and spiral in left direction are" +str(second_no) + "\n. Total spirals are"+str(sum)

btn=Button(root,text="Show Fibonacci Series", command=Fibonacci) 
btn.pack()    
label_flower.pack()
label_series.pack()
label_spiral.pack()

root.mainloop()