from tkinter import*

root=Tk()
root.title("Fibonacci Series")
root.geometry("400x400")


label_series=Label(root,text="Fibonacci Series")
label_fibonacci_series=Label(root)
label_sum=Label(root)
entry_input=Entry(root)



def Fibonacci():
    t=int(entry_input.get())
    first_no=0
    second_no=1
    sum=0
    i=1
    sum2=0
    
    while(i <= t):
        label_series["text"]+= str(sum)+  " "
        label_sum["text"]="Sum:"+ str(sum2)
        i=i+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        sum2=sum2+sum
    


btn=Button(root,text="Show Fibonacci Series", command=Fibonacci) 
btn.pack()    
entry_input.pack()
label_fibonacci_series.pack()
label_series.pack()
label_sum.pack()

root.mainloop()